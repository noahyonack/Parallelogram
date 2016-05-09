# This is Parallelogram.

Parallelogram is a parallelization package that distributes computationally intensive programs across machines in a distributed system using a distribution model similar to that of the ride-sharing service Uber.

## Documentation:

Before you begin reading the README, please note that extensive documentation of the code itself can be found in documentation/pydoc. There you will find autogenerated HTML files corresponding to our code and dependencies. To view these files, simply open them in your web browser of choice.

## To begin using:

Clone and `cd` into the repository. Simply run `sudo python setup.py install` to install the package. Running this command will install all the necessary external dependencies. Note that parallelogram currently only supports the Windows platform.

To use this library, execute:

`python parallelogram_server.py`

Then, in another window, navigate to the root directory and execute your program, via:

`python filename.py`

All `filename.py` needs to do is import Parallelogram and call one of the three exposed methods, like so:

```python
from parallelogram import parallelogram

data = range(1000)

def foo(elt, index):
	'''
	A function to map over a list of data.
	Increments every element in the list by 1.
	'''
	return elt + 1

# port 1001 is currently hardcoded into Parallelogram's
# configuration file. If you'd rather not use port 1001,
# you may change it in parallelogram/config.py
result = parallelogram.p_map(foo, range(10000), 1001, 30)
print result
```

## What is the idea behind Parallelogram?

Parallelogram is modeled after the popular ride-sharing service, Uber. Uber has a pool of users that can be classified as
either passengers or drivers. When a passenger Sarah requires a lift, she broadcasts a request, which alerts nearby drivers who can then decide to either accept or ignore the request. Drivers who are already carrying passengers oftentimes do not accept the request, and only those drivers who are completely available (and ideally nearby) consider picking up Sarah. Once an Uber driver confirms Sarah’s request, all other available drivers are notified that Sarah no longer needs a ride.

This ride­sharing system will serve as the foundation of our parallelization model. Our library will, on a single machine, partition pieces of the client’s program into parallelizable chunks.

## What methods does this library expose?
* ```python
	p_map(foo, data, port, timeout)
	```
    * Map a function `foo()` over `data` (of type list). `p_map()` modifies `data` in place
and supplies `foo()` with both the current element of the list and its
respective index. Communication happens over port `port`and `timeout` is the time to wait for the data to be returned before assuming failure and redistributing chunks. 
* `p_filter(foo, data, port, timeout)`
    * Filter `data` (of type list) via a predicate formatted as a function. Communication happens over port `port`and `timeout`is the time to wait for the data to be returned before assuming failure and redistributing chunks. 
* `p_reduce(foo, data, port, timeout)`
    * Reduce `data` (of type list) by continually applying `foo()` to subsequent
	elements of `data`. Communication happens over port `port`and `timeout`is the time to wait for the data to be returned before assuming failure and redistributing chunks. 

## How exactly does this distribution work?
Please see the documentation folder and the Implementation Details and Design Choices section of the written report for a detailed description of how Parallelogram works. 

## Package Structure

* `documentation/pydoc`
	* Autogenerated pydoc documentation for our code and its dependencies
* `parallelogram`
	* `config.py`
		* This file contains config values (like the port numbers) used by our library
	* `helpers.py`
		* This file defines helper functions, methods, and classes for in our implementations of p_map(), p_filter(), and p_reduce(), in addition to our server implementation.
	* `parallelogram.py`
		* This file contains our library's implementations of p_map(), p_filter(), and p_reduce(). We use the letter "p" because it indicates that the method is paralellized and because doing so ensures that our functions are properly namespaced
	* `parallelogram_server.py`
		* This file defines a Server class, which allows machines to listen on a port for jobs. This class should be instantiated by every machine in the distributed system that is meant to process jobs.
* `tests`
	* `distributed`
		* Three different nosetests which ensure correctness of `p_map()`, `p_filter()`, and `p_reduce()`
	* `local`
		* Three different nosetests which ensure correctness of our local implementations of `map()`,
				`filter()`, and `reduce()`

## How can I run or write tests?

Nose is a Python package that makes running the tests themselves easy. It automatically gets installed when you run `python setup.py install`. To run tests, navigate to the root directory. Then execute:

`nosetests`

Test files live in `/tests/local` and `/tests/distributed` and can be validated by running `nosetests` from the root directory.
'''
Ensures correctness for p_map() using the PyUnit (unittest) package
'''

import unittest # our test package
from parallelogram.config import PORT # PORT on which the server should listen
from parallelogram import parallelogram # library methods 
from parallelogram.parallelogram_server import Server # server api

class TestMap_Distributed(unittest.TestCase):
    #setUp and tearDown BROKEN
    # def setUp(self):
    #     self.server = Server(PORT)
    #     self.server.start()
    #     print('started')
    #
    # def tearDown(self):
    #     self.server.stop()
    #     print('stopped')

    def test_map_1(self):
        '''
        Test a basic map case by mapping an incremental 
        function over a small list
        '''

        def foo_1(elt, index):
            '''
            Increments an element by 1
            '''
            return elt + 1

        output = parallelogram.p_map(foo_1, [1,2,3,4,5,6], PORT, 10)
        self.assertEqual(output, range(2, 8))
    
    def test_map_2(self):
        '''
        Test a basic map case by mapping an incremental 
        function over a big list
        '''

        def foo_1(elt, index):
            '''
            Increments an element by 1
            '''
            return elt + 1
<<<<<<< HEAD

        output = parallelogram.p_map(foo_1, range(10000), PORT, 30)
        self.assertEqual(output, range(1, 10001))
=======
        output = parallelogram.p_map(foo_1, range(100), PORT, 30)
        self.assertEqual(output, range(1, 101))
>>>>>>> 935750d29eb26e86b33b720697096b346803b58e

    def test_map_3(self):
        '''
        Ensure that map operates correctly on empty lists.
        '''
        def foo_1(elt, index):
            '''
            Increments an element by 1
            '''
            return elt + 1

        output = parallelogram.p_map(foo_1, [], PORT, 10)
        self.assertEqual(output, [])

    #check if cloudpickle can handle libraries that aren't imported
    #success, seems to be able to import and deal with modules it knows
    # def test_cloudpickle_library(self):
    #
    #     def test1(elt, index):
    #         return np.sum(np.arange(elt, 5))
    #
    #     print('map')
    #     output = parallelogram.p_map(test1, [1,2,3], PORT, 10)
    #     self.assertEqual(output, [10,9,7])


    # #check if cloudpickle can handle externally defined classes
    # # IT CAN'T, TEST FAILED, COULDN'T FIND EXTERNAL MODULE
    # def test_cloudpickle_external_class(self):
    #
    #     def test1(elt, index):
    #         a = helpers_test.testClass(elt)
    #         return a.add()
    #
    #     print('map')
    #     output = parallelogram.p_map(test1, [1,2,3], PORT)
    #     self.assertEqual(output, [2,3,4])

    #check if cloudpickle can handle internally defined classes
    # def test_cloudpickle_class(self):
    #
    #     class testClass():
    #         def __init__(self, value):
    #             self.value = value
    #
    #         def add(self):
    #             return(self.value + 1)
    #
    #     def test1(elt, index):
    #         a = testClass(elt)
    #         return a.add()
    #
    #     print('map')
    #     output = parallelogram.p_map(test1, [1,2,3], PORT, 10)
    #     self.assertEqual(output, [2,3,4])
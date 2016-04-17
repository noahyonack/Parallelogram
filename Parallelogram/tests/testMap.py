'''
Ensures correctness for map() using the PyUnit (unittest) package
'''

import unittest
from parallelogram import parallelogram

class TestMap(unittest.TestCase):

	def test_map(self):
		
		def test1(elt, index):
			return elt + 1
		
		output = parallelogram.map(test1, [1,2,3])
		self.assertEqual(output, [2,3,4])
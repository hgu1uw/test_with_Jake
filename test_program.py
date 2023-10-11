import pdb; pdb.set_trace() # debugger
from program import hello
import unittest


class TestFunctions(unittest.TestCase):
	def testHello(self):
		result = hello()
		self.assertTrue(result =="goodbye")

	def testHello(self):
		result = hello()
		self.assertTrue(result =="hello")


if __name__ == '__main__':
	unittest.main()
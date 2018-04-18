import unittest
from fibonacci import Fibonacci
import json

class TestFibonacci(unittest.TestCase):
	 
	def setUp(self):
		with open('config.json') as file:
			conf = json.load(file)

		self.f = Fibonacci(conf['redis_host'], conf['redis_db'])

	def test_numbers_generate(self):
		self.f.numbers(9,13)
		control_sequence = self.f.control(9,13)
		etalon_sequence = ["<div>[9] == b'34'</div>", "<div>[10] == b'55'</div>", "<div>[11] == b'89'</div>", "<div>[12] == b'144'</div>"]
		self.assertTrue(control_sequence, etalon_sequence)

	def test_starter_sequence(self):
		control_sequence = self.f.control(1,3)
		etalon_sequence = ["<div>[1] == b'1'</div>", "<div>[2] == b'1'</div>"]
		self.assertTrue(control_sequence, etalon_sequence)
	
if __name__ == '__main__':
	unittest.main()		


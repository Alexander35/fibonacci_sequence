import unittest
import http_server 
import json
import requests

class TestHttpServer(unittest.TestCase):
	
	def setUp(self):
		with open('config.json') as file:
			self.conf = json.load(file)	

	def test_fibonachi_fom_a_to_b(self):

		response = requests.get('http://localhost:{}/fibonachi?from=9&to=13'.format(self.conf['http_server_port']))
		control_sequence = response.content
		etalon_sequence = ["<div>[9] == b'34'</div>", "<div>[10] == b'55'</div>", "<div>[11] == b'89'</div>", "<div>[12] == b'144'</div>"]
		self.assertTrue(control_sequence, etalon_sequence)

	def test_get_sequence_fom_a_to_b(self):
		response = requests.get('http://localhost:{}/get-sequence?from=9&to=13'.format(self.conf['http_server_port']))		
		control_sequence = response.content
		etalon_sequence = ["<div>[9] == b'34'</div>", "<div>[10] == b'55'</div>", "<div>[11] == b'89'</div>", "<div>[12] == b'144'</div>"]
		self.assertTrue(control_sequence, etalon_sequence)

if __name__ == '__main__':
	unittest.main()			
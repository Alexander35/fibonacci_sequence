from  http.server import *
import socketserver
from urllib.parse import urlparse, parse_qs
import json
from fibonacci import Fibonacci

class RequestHandler(BaseHTTPRequestHandler):

	def request_parse(self, request):
		try:
			splitted_request = request.split(' ')
			parsed_request = urlparse(splitted_request[1])
			result = {}
			result['path'] = parsed_request[2]
			result['query'] = parse_qs(parsed_request[4])
			return result
		except Exception as exc:
			print('request_parse error: {}'.format(exc))	

	def request_process(self, request):
		if request['path'] == '/fibonachi':
			try:
				f = int(request['query']['from'][0])
				t = int(request['query']['to'][0])
				self.fibonucci.numbers(f, t)
				self.send_response(200)
				self.send_header('Content-type','text-html')
				self.end_headers()
				[self.wfile.write( item.encode()) for item in self.fibonucci.control(f, t)] 
				return

			except Exception as exc:
				print('/fibonachi error : {}'.format(exc))
				self.send_response(500)
				self.send_header('Content-type','text-html')
				self.end_headers()
				self.wfile.write(b'generate sequence error') 
				return
		
		if request['path'] == '/get-sequence':
			try:
				f = int(request['query']['from'][0])
				t = int(request['query']['to'][0])
				self.send_response(200)
				self.send_header('Content-type','text-html')
				self.end_headers()
				[self.wfile.write( item.encode()) for item in self.fibonucci.control(f, t)] 
				return
				
			except Exception as exc:	
				print('/get-sequence : {}'.format(exc))
				self.send_response(500)
				self.send_header('Content-type','text-html')
				self.end_headers()
				self.wfile.write(b'read sequence error')
				return

		self.send_response(404)
		self.send_header('Content-type','text-html')
		self.end_headers()
		self.wfile.write(b'page not found')		
		return

	def do_GET(self):
		parsed_request = self.request_parse(self.requestline)
		self.request_process(parsed_request)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000, redis_host='localhost', redis_db=1):
	try:
	    server_address = ('', port)
	    handler_class.fibonucci = Fibonacci(redis_host,redis_db)
	    httpd = server_class(server_address, handler_class)
	    httpd.serve_forever()
	except Exception as exc:
		print('run http server error : {}'.format(exc))    

if __name__ == '__main__':

	with open('config.json') as file:
		conf = json.load(file)

	run(port=int(conf['http_server_port']), redis_host=conf['redis_host'], redis_db=conf['redis_db'])    
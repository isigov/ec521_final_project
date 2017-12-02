#!/usr/bin/env python
"""
Usage::
    ./server.py [<port>]
Send a POST request::
    curl -d "request_type&url1&url2..." http://localhost
Available request types: 
    eval: evaluate given URLs
    update: send updated URL list
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer, re

def url_valid(url):
    regex = r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$'
    searchObj = re.search( regex, url, re.M|re.I)
    if searchObj:
        return True
    else:
        return False

def url_eval(url_list):
	num_urls = len(url_list)
	for i in range(0,num_urls):
		print(url_list[i])
		if (url_valid(url_list[i])):
			print("URL is valid")
		else:
			print("Invalid URL")	

def update_list():
	return True


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Go away</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
	content_len = int(self.headers.getheader('content-length'))
	post_body = self.rfile.read(content_len)
	#print(post_body)
	
	post_body_list = post_body.split("&")
	num_urls = len(post_body_list)-1
	req_type = post_body_list[0]
       
	if (req_type == "eval"):
		print("eval in progress")
		url_eval(post_body_list[1:])
	elif (req_type == "update"):
		print("sending update...")
		# send list here
	else:
		print("Invalid request type")

	self._set_headers()
        self.wfile.write("<html><body><h1>Request received!</h1></body></html>")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

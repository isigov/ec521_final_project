#!/usr/bin/env python
"""
*If eval request received:
Puts received URL bases to csv file and initiates crawler. Updates blacklist according to results
*If update request received:
Sends the blacklist to specified IP

TODO:
-loading a list of blacklisted url bases
-starting crawler
-getting crawl results back
-updating blacklist
-sending (compressed?) blacklist to soecified address/port 
-handling 2+ consecutive requests from extension, csv is reset otherwise
-race conditions concerning csv file and blacklist 

Usage:
    ./server.py [<port>]
Send a POST request::
    curl -d "request_type&url1&url2..." http://localhost
Available request types: 
    eval: evaluate given URLs
    update: send updated URL list
"""

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer, csv


#TODO we are never receiving multiple URL's, better handle it here
#TODO blacklist / whitelist / eval_queue
#TODO add to eval_queue if not in all above

def url_eval(url_list):
	num_urls = len(url_list)
	index_list = list(range(num_urls+1))[1:]
	for req in (url_list):
		print(req)
	
	# we should be keeping a local black/whitelist file copy here 
	#load them into url_list so that we don't evaluate twice
	with open('/home/ec521/modCrawler/etc/eval_list.csv', 'wb') as eval_csv:
		wr = csv.writer(eval_csv, quoting=csv.QUOTE_ALL)
		wr.writerows(zip(index_list, url_list))	

# TODO
def update_lists():
	return True


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>Go away</h1></body></html>")


    def do_GET(self):
	rootdir = '/'
	try:
		if self.path.endswith('.txt'):

			f = open(rootdir + self.path) #open requested file
			print("here")
			#send code 200 response
			self.send_response(200)

			#send header first
			self.send_header('Content-type','text-html')
			self.end_headers()

			#send file content to client
			self.wfile.write(f.read())
			f.close()
			return
	
	except Exception as e:
		print(e)
		self.send_error(404, 'file not found')

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
		print("eval requested")
		url_eval(post_body_list[1:])
	elif (req_type == "update"):
		print("sending update...")
		# send all list here
		# something wget compatible is better
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

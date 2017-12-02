#!/usr/bin/env python
"""
This script is to be called by crawler every time user visits a website
Gets the URL typed into search bar and checks if it's valid
Valid URLs are parsed to get the URL base
Values are put into POST request and sent to server
"""
from urlparse import urlsplit
import re, subprocess


def url_valid(url):
    regex = r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$'
    searchObj = re.search( regex, url, re.M|re.I)
    if searchObj:
        return True
    else:
        return False

def call_crawler():
	curl_args = ['curl', '--silent', url]
	grep_args = ['grep', 'HTTP']
 
	process_curl = subprocess.Popen(curl_args, stdout=subprocess.PIPE, shell=False)
	process_grep = subprocess.Popen(grep_args, stdin=process_curl.stdout, stdout=subprocess.PIPE, shell=False)
    
    # Allow process_curl to receive a SIGPIPE if process_grep exits.
    process_curl.stdout.close()
    return process_grep.communicate()[0].decode('utf-8').splitlines()


num_urls = len(url_list)

for i in range(0,num_urls):
	if (url_valid(url_list[i])):
		print("URL is valid")
	else:
		print("Invalid URL")

# I also like to live dangerously
os.system("curl -d \"eval&" + url_list[i] + "\" http://localhost")









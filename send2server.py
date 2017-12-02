#!/usr/bin/env python
"""
This script is to be called by crawler every time user visits a website
Gets the URL typed into search bar and checks if it's valid
Valid URLs are parsed to get the domain name
Domain name is put into POST request and sent to server

TODO:
-blacklist/whitelist check done in extension or here?

"""

import re, subprocess, sys, urlparse
from sys import argv
import tldextract

def url_valid(url):
    regex = r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$'
    searchObj = re.search( regex, url, re.M|re.I)
    if searchObj:
        return True
    else:
        return False


def main(url):

	extracted = tldextract.extract(url)
	domain = '{}.{}'.format(extracted.domain, extracted.suffix)
	server_ip = 'http://localhost'
	
	if url_valid(url):
		post_body = "eval&" + domain
		curl_args = ['curl', '-d', post_body , server_ip]
		print("Seding evaluation request: " + domain)
		process_curl = subprocess.call(curl_args, shell=False)
	else:
		print("URL is not valid")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: " + sys.argv[0] + " [url]")
    else:
	main(argv[1])









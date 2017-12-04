#!/usr/bin/python

from selenium import webdriver
import time, sys, pickle, os


def crawl_url(url):

	# profile.set_preference("browser.cache.disk.enable", False)
	# profile.set_preference("browser.cache.memory.enable", False)
	# profile.set_preference("browser.cache.offline.enable", False)
	# profile.set_preference("network.http.use-cache", False)
	# profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1")
	# driver = webdriver.Firefox(firefox_profile=profile)
	driver = webdriver.Firefox()
	# user_agent = driver.execute_script("return navigator.userAgent")



	def save_cookies(dumpName):
		cookies_list = driver.get_cookies()
		cookies_dict = {}
		for cookie in cookies_list:
			cookies_dict[cookie['name']] = cookie['value']
		#print(cookies_dict)

		pickle.dump( cookies_list, open(dumpName,"wb"))


	driver.get(url)
	if (url == "http://mary008-340stat01.bu.edu" or url =="http://samy.pl/evercookie"):
		create_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[1]")
		create_button[0].click()
	time.sleep(5)
	save_cookies("crawl1.pkl")

	#driver.execute_script('window.localStorage.clear();')
	driver.delete_all_cookies()

	driver.get(url)
	if (url == "http://mary008-340stat01.bu.edu" or url =="http://samy.pl/evercookie"):
		discover_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[2]")
		discover_button[0].click()
	time.sleep(5)
	save_cookies("crawl2.pkl")
	
	driver.quit()

	os.system("/home/ec521/ec521_final_project/clean_profile.sh")
	driver = webdriver.Firefox("/home/ec521/ec521_final_project/cleanProfile")

	driver.get(url)
	if (url == "http://mary008-340stat01.bu.edu" or url =="http://samy.pl/evercookie"):
		discover_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[2]")
		discover_button[0].click()
	time.sleep(5)
	save_cookies("crawl3.pkl")
	driver.quit()

def findCookieValue(cookie, name):
	for i in range(len(cookie)):
		if cookie[i]['name'] == name:
			return cookie[i]['value']
	return None

def memory_load(fileName):
	with open(fileName, 'rb') as handle:
		library = pickle.load(handle)
		return library

def everCookieFind(cookieDB1, cookieDB2, cookieDB3):
	evercookiePresent = False
	cookie_name=[0 for i in range(len(cookieDB1))]

	for cookie_index in range(0, len(cookieDB1)):
		cookie_name[cookie_index] = cookieDB1[cookie_index]['name']

# if cookie same in 1,2,3 then disregard
# if cookie same in 1 and 2 the evercookie
# if cookie different in all then normal cookie
	print "===================================="
	for cname in cookie_name:
		cookie1 = findCookieValue(cookieDB1, cname)
		cookie2 = findCookieValue(cookieDB2, cname)
		cookie3 = findCookieValue(cookieDB3, cname)
		if cookie1 != None and cookie2 != None and cookie3 != None:
			# disregard
			if cookie1 == cookie2 == cookie3:
				pass
			# evercookie
			if cookie1 == cookie2 != cookie3:
				print "Potential EverCookie!!!!   " + cname
				evercookiePresent = True
			# normal cookie
			if cookie1 != cookie2 != cookie3:
				print "Normal Cookie              " + cname

	return evercookiePresent


def printCookie(cookieDB):
	for cookie_index in range(0, len(cookieDB)):
		print(cookieDB[cookie_index]['name'], cookieDB[cookie_index]['value'])
	print("\n")

def detect_evercookie(url):

	file1 = "crawl1.pkl"
	file2 = "crawl2.pkl"
	file3 = "crawl3.pkl"

	crawl_url(url)

	lib1 = memory_load(file1)
	lib2 = memory_load(file2)
	lib3 = memory_load(file3)


	#for cookie_index in range(0, len(lib2)):
	#	print(lib2[cookie_index]['name'], lib2[cookie_index]['value'])

	#for cookie_index in range(0, len(lib3)):
	#	print(lib3[cookie_index]['name'], lib3[cookie_index]['value'])

	#printCookie(lib1)
	#printCookie(lib2)
	#printCookie(lib3)
			
	return everCookieFind(lib1,lib2,lib3)


if __name__ == "__main__":

	url = "http://yandex.ru"
	url2="http://mary008-340stat01.bu.edu"
	url3="http://samy.pl/evercookie"
	
	if(detect_evercookie(url)):
		print("evercookie found!")
	else:
		print("All good")


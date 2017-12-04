#!/usr/bin/python

from selenium import webdriver
import time, sys, pickle


def crawl_url(url):

	# profile = webdriver.FirefoxProfile()
	# profile.set_preference("browser.cache.disk.enable", False)
	# profile.set_preference("browser.cache.memory.enable", False)
	# profile.set_preference("browser.cache.offline.enable", False)
	# profile.set_preference("network.http.use-cache", False)
	# profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1")
	# driver = webdriver.Firefox(firefox_profile=profile)
	driver = webdriver.Firefox()
	# user_agent = driver.execute_script("return navigator.userAgent")

	driver.get(url)
	create_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[1]")
	

	def save_cookies(dumpName):
		cookies_list = driver.get_cookies()
		cookies_dict = {}
		for cookie in cookies_list:
			cookies_dict[cookie['name']] = cookie['value']
		print(cookies_dict)

		pickle.dump( cookies_list, open(dumpName,"wb"))

	create_button[0].click()
	time.sleep(5)
	save_cookies("crawl1.pkl")

	#driver.execute_script('window.localStorage.clear();')
	driver.delete_all_cookies()

	driver.get(url)
	discover_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[2]")
	discover_button[0].click()
	time.sleep(5)
	save_cookies("crawl2.pkl")


	driver.quit()

	driver = webdriver.Firefox("/home/ec521/Desktop/cleanProfile")
	driver.get(url)
	discover_button = driver.find_elements_by_xpath("//*[@id=\"pagecontent\"]/pre[3]/input[2]")
	discover_button[0].click()
	time.sleep(5)
	save_cookies("crawl3.pkl")
	driver.quit()



def memory_load(fileName):
	with open(fileName, 'rb') as handle:
		library = pickle.load(handle)
		return library


url = "http://mary008-340stat01.bu.edu"
url2 = "http://samy.pl/evercookie"
file1 = "crawl1.pkl"
file2 = "crawl2.pkl"
file3 = "crawl3.pkl"

#crawl_url(url2)


lib1 = memory_load(file1)
lib2 = memory_load(file2)
lib3 = memory_load(file3)

print("\n")

for cookie_index in range(0, len(lib1)):
	print(lib1[cookie_index]['name'], lib1[cookie_index]['value'])

print("\n")

for cookie_index in range(0, len(lib2)):
	print(lib2[cookie_index]['name'], lib2[cookie_index]['value'])

print("\n")

for cookie_index in range(0, len(lib3)):
	print(lib3[cookie_index]['name'], lib3[cookie_index]['value'])


# if cookie same in 1,2,3 then disregard
# if cookie same in 1 and 2 the evercookie
# if cookie different in all then normal cookie

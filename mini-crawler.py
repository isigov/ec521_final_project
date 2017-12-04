#!/usr/bin/python

from selenium import webdriver
import time, sys, pickle

def main(url, cleanSlate):

	if (cleanSlate): # if 1 then clean profile
		offlineSwitch = False
	else:
		offlineSwitch = True

	profile = webdriver.FirefoxProfile()
	profile.set_preference("browser.cache.disk.enable", offlineSwitch)
	profile.set_preference("browser.cache.memory.enable", offlineSwitch)
	profile.set_preference("browser.cache.offline.enable", offlineSwitch)
	profile.set_preference("network.http.use-cache", offlineSwitch)
	#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1")

	driver = webdriver.Firefox(firefox_profile=profile)

	# user_agent = driver.execute_script("return navigator.userAgent")
	# print(user_agent)

	driver.get(url)

	cookies_list = driver.get_cookies()
	cookies_dict = {}
	for cookie in cookies_list:
		cookies_dict[cookie['name']] = cookie['value']
	print(cookies_dict)
	#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

	if (cleanSlate):
		driver.execute_script('window.localStorage.clear();')
		driver.delete_all_cookies()

	driver.quit()


if __name__ == "__main__":

	main(url, 1)
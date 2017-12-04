#!/usr/bin/python

from selenium import webdriver
import time, sys, pickle

#def crawl_url(url, userAgentChange):

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", True)
profile.set_preference("browser.cache.memory.enable", True)
profile.set_preference("browser.cache.offline.enable", True)
profile.set_preference("network.http.use-cache", True)
#profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1")

driver = webdriver.Firefox(firefox_profile=profile)

# user_agent = driver.execute_script("return navigator.userAgent")
# print(user_agent)

driver.get('http://www.google.com')
print("Evaluating: "+driver.current_url)


#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
cookies_list = driver.get_cookies()
cookies_dict = {}
for cookie in cookies_list:
	cookies_dict[cookie['name']] = cookie['value']

print(cookies_dict)

driver.delete_all_cookies()
# driver.getSessionStorage().clear();
# driver.getLocalStorage().clear();
driver.execute_script('window.localStorage.clear();')
driver.quit()
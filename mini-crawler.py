#!/usr/bin/python


from selenium import webdriver
import time, sys


path2driver='/home/ec521/ec521_final_project/'

driver = webdriver.Firefox(path2driver+'geckodriver')

driver.get('http://www.google.com')
time.sleep(3)

driver.quit()
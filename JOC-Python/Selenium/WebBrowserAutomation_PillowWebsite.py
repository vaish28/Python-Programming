# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 06:54:53 2021
Web browser automation

@author: Supriya
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome('C:/Users/Supriya/Downloads/chromedriver.exe')

browser.get('https://pypi.org/project/Pillow/')

search=browser.find_element_by_class_name('search-form__search')

search.send_keys('Download'+Keys.ENTER)

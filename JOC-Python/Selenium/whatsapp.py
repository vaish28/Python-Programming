# -*- coding: utf-8 -*-
"""

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # waiting period to slow down because of internet speed hence import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser=webdriver.Chrome("C:/Users/Supriya/Downloads/chromedriver.exe")
browser.get("https://web.whatsapp.com/")#QR code for scanning
wait=WebDriverWait(browser,600) # wait for webdriver for slow internet connection

'''
target='"Abcd Efgh"' # name of your contact or friend to send message to

msg="message sent using Python!" # message to be sent
x_arg='//span[contains(@title, '+ target + ')]'# to locate the contact,target name of the friend
#span tag is where the contact is available. using title attribute you locate 
#the contact
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))# wait untill the the contact is found
target.click()# open the contact 
msg_box=browser.find_element_by_class_name('_1Plpp')# go to message box of the contact use class name
for i in range(3): # sending 3 times the msg
    msg_box.send_keys(msg+Keys.ENTER) # after msg is written Enter key to be pressed

'''

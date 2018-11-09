from selenium import webdriver
import os
import time
import json

os.environ["LANG"] = "en_US.UTF-8"


driver = webdriver.Chrome('C:/Users/Manisha/Downloads/chromedriver.exe')
driver.get('https://www.mwave.me/en/signin')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/a/span[2]').click()
driver.find_element_by_id('email').send_keys()
driver.find_element_by_id('pass').send_keys()
time.sleep(10)
driver.find_element_by_xpath('//*[@id="facebook"]/body').click()
driver.quit()
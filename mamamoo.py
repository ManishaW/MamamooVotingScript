from selenium import webdriver
import os
import time
import json

os.environ["LANG"] = "en_US.UTF-8"

with open('config.json') as json_data:
    driver = webdriver.Chrome('C:/Users/manis/Downloads/chromedriver.exe')
    driver.get('https://www.mwave.me/en/signin')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/a/span[2]').click()

    j = json.load(json_data)
    driver.find_element_by_id('email').send_keys(j['accounts']['facebook']['id'])
    driver.find_element_by_id('pass').send_keys(j['accounts']['facebook']['password'])
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
    driver.get('http://mama.mwave.me/en/vote')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click() #stray kids
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click() #next button
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[4]/div/label').click() #gidle
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[5]/div/label').click() #bts
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[4]/div/label').click() #MAMAMOO
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    driver.find_element_by_xpath()




    time.sleep(3)
    driver.quit()
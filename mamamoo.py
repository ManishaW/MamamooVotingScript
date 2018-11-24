from selenium import webdriver
import os
import time
import json

os.environ["LANG"] = "en_US.UTF-8"

with open('config.json') as json_data:
    driver = webdriver.Chrome('C:/Users/Manisha/Downloads/chromedriver.exe')
    driver.get('https://www.mwave.me/en/signin')
    driver.set_window_size(1024, 600)
    driver.maximize_window()

    j = json.load(json_data)

    # facebook login
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[5]/a/span[2]').click()

    driver.find_element_by_id('email').send_keys(j['accounts']['facebook']['id'])
    driver.find_element_by_id('pass').send_keys(j['accounts']['facebook']['password'])
    driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    # #gmail
    # driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[7]/a/span[2]').click()
    # driver.find_element_by_name('identifier').send_keys(j['accounts']['gmail']['id'])
    # driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()
    # driver.find_element_by_name('password').send_keys(j['accounts']['gmail']['password'])
    # driver.find_element_by_xpath('//*[@id="identifierNext"]/content').click()








    #vote
    driver.get('http://mama.mwave.me/en/vote')
    time.sleep(7)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click() #stray kids
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click() #next button
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[4]/div/label/div').click() #gidle
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[5]/div/label').click() #BTS
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[4]/div/label').click() #MAMAMOO
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[4]/div/label').click()  # ZIACO
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click()  # SUNMI
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[3]/div/label').click()  # CHUNHA
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click()  # GOT7
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[3]/div/label').click()  # BLACKPINK
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[5]/div/label').click()  # HEIZE
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click()  # MAMAMOO
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[1]/div/label').click()  # DAY 6
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[2]/div/label').click()  # jay park
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[5]/div/label').click()  # GG-subunit
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[5]/div/label').click()  # shinee
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[1]/div/label').click()  # nuest
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[17]/div/label').click()  # MAMAMOO
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)

    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/ul/li[16]/div/label').click()  # MAMAMOO
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/section/div[1]/button').click()
    time.sleep(1)


    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/section/div/button').click()
    time.sleep(1)
   # driver.save_screenshot('C:/Users/Manisha/Downloads/screenshotFBlogin.png')



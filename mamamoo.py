from selenium import webdriver
import os
os.environ["LANG"] = "en_US.UTF-8"

driver = webdriver.Chrome('C:/Users/Manisha/Downloads/chromedriver.exe')
driver.get('https://www.mwave.me/en/signin')
# driver.find_elements_by_tag_name()


driver.quit()
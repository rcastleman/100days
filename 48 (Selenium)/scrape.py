from cgitb import text
from typing import Iterable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#-------------- SCRAPE DATA ---------------#

URL = "https://www.python.org/"

x_path = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul'
class_name = None
date_selector = ".event-widget time" # a <time> within the event-widget
name_selector = ".event-widget li a"  # an <a> inside an <li> within the event-widget 
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)
# events = driver.find_elements(By.CLASS_NAME,class_name)
# events = driver.find_elements(By.XPATH,x_path)
dates = driver.find_elements(By.CSS_SELECTOR,date_selector)
names = driver.find_elements(By.CSS_SELECTOR,name_selector)

# events = []
# for item in driver.find_elements(By.XPATH,x_path):
#     date = item.find_element(By.CLASS_NAME,'say-no-more').text
#     event = item.find_element(By.CSS_SELECTOR,'a').text
#     events.append({'date': date, 'event name': event})

for item in names:
    print(item.text)
driver.quit() #closes the entire browser

#-------------- BUILD DICTIONARY ---------------#

# {key: value for (key, value) in iterable}

# event_dict = {k:v for (k,v) in iterable}

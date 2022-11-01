from cgitb import text
from typing import Iterable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#-------------- SCRAPE DATA ---------------#

URL = "https://www.python.org/"

x_path = '//*[@id="content"]/div/section/div[3]/div[2]/div/ul'
class_name = None
selector = None
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)
# events = driver.find_elements(By.CLASS_NAME,class_name)
# events = driver.find_elements(By.XPATH,x_path)
# events = driver.find_elements(By.CSS_SELECTOR,selector)

events = []
for item in driver.find_elements(By.XPATH,x_path):
    date = item.find_element(By.CLASS_NAME,'say-no-more').text
    event = item.find_element(By.CSS_SELECTOR,'a').text
    events.append({'date': date, 'event name': event})


print(events)
driver.quit() #closes the entire browser

#-------------- BUILD DICTIONARY ---------------#

# {key: value for (key, value) in iterable}

# event_dict = {k:v for (k,v) in iterable}

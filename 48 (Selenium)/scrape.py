from cgitb import text
from typing import Iterable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#-------------- SCRAPE DATA ---------------#

URL = "https://www.python.org/"

x_path = '//*[@id="bylineInfo"]'
class_name = "a-offscreen"
selector = "#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center > span > span.a-offscreen"
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)
# events = driver.find_elements(By.CLASS_NAME,class_name)
events = driver.find_elements(By.XPATH,x_path)
# events = driver.find_elements(By.CSS_SELECTOR,selector)
print(events.text)
driver.quit() #closes the entire browser

#-------------- BUILD DICTIONARY ---------------#

# {key: value for (key, value) in iterable}



event_dict = {k:v for (k,v) in iterable}
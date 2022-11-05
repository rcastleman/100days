from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'

s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

cookie = driver.find_element(By.ID,"cookie")

items = driver.find_elements(By.CSS_SELECTOR,"#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
TIMER = time.time() + 60*1 

while True:
    cookie.click()

    #Every 5 seconds:
    # if time.time() > timeout:

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > TIMER:
        cookie_per_s = driver.find_element(By.ID,"cps").text
        print(cookie_per_s)
        break

driver.quit()
# solution from https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b?permalink_comment_id=4106336#gistcomment-4106336

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'

s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

cookie_ID = 'cookie'
cookie = driver.find_element(By.ID,cookie_ID)

duration = 1    
timeout = time.time() + 5
TIMER = time.time() + 60 * duration

while True:
    cookie.click()
    if time.time() > timeout:
        buyable = []
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in store[:-1]:
            if item.get_attribute('class') != "grayed":
                buyable.append(item)
        buyable[-1].click()
        timeout = time.time() + 5
    if time.time() > TIMER:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break


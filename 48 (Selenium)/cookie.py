from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# URL = 'http://orteil.dashnet.org/experiments/cookie/'
URL = 'https://domdomegg.github.io/cookieclicker/'

cookie_ID = 'cookie'

# CPS_ID = "cookie" # for orteil
CPS_ID = "cookieCps" #for domdom


s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

cookie = driver.find_element(By.ID,cookie_ID)

# items = driver.find_elements(By.CSS_SELECTOR,"store")
# item_ids = [item.get_attribute("id") for item in items]

duration = 0.25
timeout = time.time() + 5
TIMER = time.time() + 60 * duration

while True:
    cookie.click()

    #Every 5 seconds:
    # if time.time() > timeout:

        # all_prices = driver.find_elements(By.CSS_SELECTOR,'store')
        # item_prices = []

        # for price in all_prices:
        #     element_text = price.text
        #     if element_text != "":
        #         cost = element_text.split('-').strip().replace(',','')
        #         item_prices.append(cost)

    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > TIMER:
        cookie_per_s = driver.find_element(By.ID,CPS_ID).text
        print(cookie_per_s)
        # print(item_prices)
        break

# driver.quit()
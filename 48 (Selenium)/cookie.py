from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://orteil.dashnet.org/experiments/cookie/'
# URL = 'https://domdomegg.github.io/cookieclicker/'

cookie_ID = 'cookie'

CPS_ID = 'cps' # for orteil
# CPS_ID = "cookieCps" #for domdom

store_ID = '#store'


s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

cookie = driver.find_element(By.ID,cookie_ID)

# items = driver.find_elements(By.CSS_SELECTOR,store_ID)
# item_ids = [item.get_attribute("id") for item in items]

# duration = 1    
# timeout = time.time() + 5
# TIMER = time.time() + 60 * duration

all_prices = driver.find_elements(By.CSS_SELECTOR,store_ID)
item_prices = []
print(item_prices)

# while True:
#     cookie.click()

#     #Every 5 seconds:
#     if time.time() > timeout:

#     #Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR,store_ID)
#         item_prices = []

#         #Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)

#         #Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]

#         #Get current cookie count
#         money_element = driver.find_element(By.ID,"money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)

#         #Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                  affordable_upgrades[cost] = id

#         #Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

#         driver.find_element(By.ID,to_purchase_id).click()
        
#         #Add another 5 seconds until the next check
#         timeout = time.time() + 5

#     #After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > TIMER:
#         cookie_per_s = float(driver.find_element(By.ID,CPS_ID).text)
#         print(cookie_per_s)
#         # print(item_prices)
#         break

# driver.quit()
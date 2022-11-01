from cgitb import text
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
# price = driver.find_element(By.CLASS_NAME,class_name)
price = driver.find_element(By.XPATH,x_path)
# price = driver.find_element(By.CSS_SELECTOR,selector)
print(price.text)
# driver.close() #closes a tab
driver.quit() #closes the entire browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = None

s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)


button.click()

driver.quit()
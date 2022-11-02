from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/Main_Page"

x_path = None
class_name = None
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)
# events = driver.find_elements(By.CLASS_NAME,class_name)
# events = driver.find_elements(By.XPATH,x_path)

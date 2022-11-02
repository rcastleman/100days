from pyexpat.errors import XML_ERROR_PARTIAL_CHAR
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = 'http://secure-retreat-92358.herokuapp.com/'
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

first_name = driver.find_element(By.NAME,"fName")
last_name = driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")
button = driver.find_element(By.CSS_SELECTOR,"form button")

first_name.send_keys("Joe")
last_name.send_keys("Dokes")
email.send_keys("jdokes@email.com")
button.click()

# driver.quit()
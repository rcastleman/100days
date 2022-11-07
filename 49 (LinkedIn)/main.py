from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3344172382&f_AL=true&f_C=21836&f_E=1&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=R'

x_path = '/html/body/div[1]/header/nav/div/a[2]'

s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

sign_in = driver.find_element(By.XPATH,x_path)

sign_in.click()

import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

INSTA = 'https://www.instagram.com/accounts/login/'
TARGET = 'https://www.instagram.com/paulsoninstitute/'

svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")

class newClass:
    def __init__(self):
        self.driver = webdriver.Chrome(service = svce)

USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASS')

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service = svce)

    def get_follower_count(self):
        self.driver.get(INSTA)
    
    def login(self):
        self.driver.get(INSTA)
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)


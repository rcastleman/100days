from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 1000
PROMISED_UP = 250

TWITTER_ID = os.environ.get("USER")
TWITTER_PASS = os.environ.get("PASS")

TWITTER_URL = 'https://twitter.com/home'
SPEEDTEST_URL = 'https://www.speedtest.net/'


svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
# driver = webdriver.Chrome(service = svce)
# driver.get(URL)

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service = svce)
        self.up = driver.get(SPEEDTEST_URL)
        self.down = 

bot = InternetSpeedTwitterBot()

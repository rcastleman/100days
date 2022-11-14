import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

PROMISED_DOWN = 1000
PROMISED_UP = 250

TWITTER_ID = os.environ.get("USER")
TWITTER_PASS = os.environ.get("PASS")
TWITTER_URL = 'https://twitter.com/home'

SPEEDTEST_URL = 'https://www.speedtest.net/'
go_button = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]'
down_readout = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'
up_readout = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
# close_button = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a/svg/use'
close_button = '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a'

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service = svce)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        time.sleep(15)
        self.driver.find_element(By.XPATH,go_button).click()
        time.sleep(30)
        alert_obj = self.driver.switch_to.alert
        alert_obj.dismiss()
        # self.driver.find_element(By.XPATH,close_button).click()
        self.down = self.driver.find_element(By.XPATH,down_readout).text
        self.up = self.driver.find_element(By.XPATH,up_readout).text
        print(f"Download: {self.down}\nUpload: {self.up}")

    def tweet_at_provider(self):
        pass

    def test(self):
        return 'bot is working'

bot = InternetSpeedTwitterBot()

bot.test()
bot.get_internet_speed()
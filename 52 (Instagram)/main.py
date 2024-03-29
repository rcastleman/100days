import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

INSTA = 'https://www.instagram.com/accounts/login/'
TARGET = 'paulsoninstitute/'

svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")

USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASS')

"""tried all these different elements before learning that the TIMING was important"""

# FOLLOWERS_BUTTON = '//*[@id="mount_0_0_WH"]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/div/span'
FOLLOWERS_BUTTON = "//a[contains(@href, 'followers')]"
# FOLLOWERS_BUTTON = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
# FOLLOWERS_BUTTON = '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'
# FOLLOWERS_BUTTON = '//*[@id="mount_0_0_WH"]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a'
# FOLLOWERS_BUTTON = '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a'

FOLLOWERS_WINDOW = '//*[@id="mount_0_0_Xh"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]'

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(service = svce)

    def get_follower_count(self):
        self.driver.get(INSTA)
    
    def login(self):
        self.driver.get(INSTA)
        time.sleep(5)

        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET}")

        time.sleep(6)
        self.driver.find_element(By.XPATH,FOLLOWERS_BUTTON).click()

        time.sleep(6)
        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        # modal = self.driver.find_element(By.XPATH,FOLLOWERS_WINDOW)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by(By.CSS_SELECTOR,"li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()


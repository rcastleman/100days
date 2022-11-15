import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

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

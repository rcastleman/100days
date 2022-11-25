import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

load_dotenv()

LIST_ID = "search-page-list-container"

svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")

USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASS')

FORM = 'https://forms.gle/WZPiFN9neKV8Gegh8'

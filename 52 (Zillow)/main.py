#--------- DEPENDENCIES ---------------- #
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

import sys
import numpy as np
import pandas as pd
# import regex as re
import lxml
from lxml.html.soupparser import fromstring
# import prettify
import numbers
# import htmltext

load_dotenv()

#--------- SCRAPE ALL LISTINGS ----------- #
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


# URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
# URL = 'https://www.zillow.com/charlottesville-va/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A38.190698439301926%2C%22east%22%3A-78.3177529375%2C%22south%22%3A37.863464504970835%2C%22west%22%3A-78.7572060625%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22min%22%3A2500%2C%22max%22%3A3750%7D%2C%22price%22%3A%7B%22min%22%3A505454%2C%22max%22%3A758181%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A30840%2C%22regionType%22%3A6%7D%5D%7D'

URL ='https://streeteasy.com/1-bedroom-apartments-for-rent/upper-west-side/status:listed%7Cprice:-4000%7Csqft%3E=600%7Cbaths%3E=1%7Camenities:elevator,doorman,laundry'


# response = requests.get(URL,headers=req_headers)
# site_data = response.text
# soup = BeautifulSoup(site_data,"html.parser")

# LISTINGS_XPATH = '//*[@id="grid-search-results"]/ul'
# LISTINGS_SELECTOR = '#grid-search-results > ul'
# LISTINGS_SELECTOR = '#grid-search-results > div.search-page-list-header > h1'
# FIRST_LISTING = '#grid-search-results > ul > li:nth-child(1)'
STREET_LISTINGS = '#result-details > div > ul'

#------- new approach ---------- #
# from https://www.geeksforgeeks.org/beautifulsoup-find-all-li-in-ul/

html = requests.get(URL).content




# all_link_elements = soup.select(".list-card-top a")
# all_link_elements = soup.findAll(STREET_LISTINGS)
all_link_elements = soup.find(class_="SearchResultPage")
print(f'all_link_elements = {all_link_elements}')

# all_links = []
# for link in all_link_elements:
#     href = link["href"]
#     print(href)
#     if "http" not in href:
#         all_links.append(f"https://www.zillow.com{href}")
#     else:
#         all_links.append(href)

# print(soup.prettify())

LIST_ID = "search-page-list-container"

svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")

USERNAME = os.environ.get('USER')
PASSWORD = os.environ.get('PASS')

FORM = 'https://forms.gle/WZPiFN9neKV8Gegh8'

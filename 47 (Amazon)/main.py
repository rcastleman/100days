import requests
from bs4 import BeautifulSoup
import lxml


URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"

User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

Accept_Language = "en-US,en;q=0.9,fr;q=0.8"

HEADERS = {
    User_Agent,
    Accept_Language}

response = requests.get(URL,headers = HEADERS)
site_text = response.text

soup = BeautifulSoup(site_text,"lmxl")

print(soup)

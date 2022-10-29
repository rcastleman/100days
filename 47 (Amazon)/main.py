import site
import requests
from bs4 import BeautifulSoup
import lxml
from send_mail import send_email


#--------------- SCRAPING -------------------#

URL = "https://www.amazon.com/Instant-Pot-6Qt-Plus-WiFi/dp/B08TMTJZ8L?ref_=ast_sto_dp"

User_Agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

Accept_Language = "en-US,en;q=0.9,fr;q=0.8"

HEADERS = {
    "User-Agent":User_Agent,
    "Accept-Language": Accept_Language}

response = requests.get(URL,headers = HEADERS)
site_text = response.text

# PARSER = "html.parser"
PARSER = "lxml"

soup = BeautifulSoup(site_text,PARSER)

# title = soup.find(id="productTitle").get_text().strip()

data = soup.find(name="span", class_="a-offscreen")
price = data.text

today_price = float(price.strip('$'))

# print(today_price)
# print(type(today_price))


#--------------- CHECK CURRENT PRICE -------------------#

target_price = 200

body = f"Subject:Price alert!\n\nThe current price is {price}, which is under your target price of ${target_price}."

if today_price < target_price:
    send_email(body)

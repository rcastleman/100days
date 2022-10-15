from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/")

yc_website = response.text

soup = BeautifulSoup(yc_website,"html.parser")

article_tag = soup.find(name="a",class_="storylink")

print(article_tag)


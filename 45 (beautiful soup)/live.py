from bs4 import BeautifulSoup
import requests
import lxml

PARSER = "lxml"
# PARSER = "html.parser"

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,PARSER)
article_tag = soup.find(name="a",class_="storylink")
print(article_tag)
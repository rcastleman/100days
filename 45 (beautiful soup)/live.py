from bs4 import BeautifulSoup
import requests
import lxml

# PARSER = "lxml"
PARSER = "html.parser"

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,PARSER)
heading = soup.find(name="h1", id="name")
article_tag = soup.find(name="a")
# print(soup.prettify())
print(article_tag)
from bs4 import BeautifulSoup
import requests
import lxml

# PARSER = "lxml"
PARSER = "html.parser"

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,PARSER)
heading = soup.find(name="h1", id="name")
article_tag = soup.find(name="span",class_="titleline")
article_link = article_tag.get("href")
article_upvote = soup.find(name="span",class_="score")
# print(soup.title)
# print(soup.prettify())
print(article_tag)
print(article_link)
print(article_upvote)

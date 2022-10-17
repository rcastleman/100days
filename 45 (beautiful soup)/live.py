from bs4 import BeautifulSoup
import requests
import lxml

# PARSER = "lxml"
PARSER = "html.parser"

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,PARSER)
# heading = soup.find(name="h1", id="name")
articles = soup.find_all(name="span",class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:

    article_text = article_tag.getText()
    article_texts.append(article_text)
    
    article_link = article_tag.a.get("href")
    article_links.append(article_link)

article_upvote = soup.find_all(name="span",class_="score").getText()
# print(soup.title)
# print(soup.prettify())
# print(article_tag)
print(article_text)
print(article_link)
print(article_upvote)

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
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

# article_upvotes = soup.find_all(name="span",class_="score").getText()
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
# print(soup.title)
# print(soup.prettify())
# print(article_tag)
# print(article_texts)
# print(article_links)
# print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])

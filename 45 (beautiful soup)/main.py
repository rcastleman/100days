from bs4 import BeautifulSoup

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents,"html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

print(soup.a)
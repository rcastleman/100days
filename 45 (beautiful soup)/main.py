from bs4 import BeautifulSoup

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents)

from bs4 import BeautifulSoup
import requests

with open ("test2.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")

print(soup.ul)

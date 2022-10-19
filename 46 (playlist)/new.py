import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.find_all(name="h3", class_="a-no-trucate")

titles = [title.getText().strip() for title in all_titles]


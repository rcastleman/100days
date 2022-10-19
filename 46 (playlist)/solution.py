import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

#----- GET TITLES -------- #

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://billboard.com/charts/hot-100/{date}/")

soup = BeautifulSoup(response.text, 'html.parser')

all_titles = soup.find_all(name="h3", class_="a-no-trucate")

titles = [title.getText().strip() for title in all_titles]

#---------- SPOTIFY ------------ #

CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET = os.environ.get("SECRET")
REDIRECT = os.environ.get("REDIRECT")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=SECRET,
                                               redirect_uri=REDIRECT,
                                               scope="playlist-modify-private",
                                             ))
                                            

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# emulating this solution:
# https://gist.github.com/angelabauer/e6087a48f9d1a87d4ec15fc29830892b?permalink_comment_id=4250715#gistcomment-4250715

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
                                            

results = sp.current_user()
USER_ID = results['id']
uris = [sp.search(title)['tracks']['items'][0]['uri'] for title in titles]

#------------------CREATING PLAYLIST---------------------------#

PLAYLIST_ID = sp.user_playlist_create(user=USER_ID,public=False,name=f"{date} BillBoard-100")['id']

sp.user_playlist_add_tracks(playlist_id=PLAYLIST_ID,tracks=uris,user=USER_ID)

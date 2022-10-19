import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="CLIENT_ID",
                                               client_secret="SECRET",
                                               redirect_uri="REDIRECT",
                                               scope = "playlist-modify-private")



#------------ GET BILLBOARD LIST  ----------------- #

user_date = input("Year? (YEAR-MO-DATE): ")

URL = f"https://www.billboard.com/charts/hot-100/{user_date}"

response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")
all_songs = soup.find_all(name="h3",class_="a-no-trucate", id="title-of-a-story")

titles = [song.getText().strip("\n\t") for song in all_songs]

with open("songs.txt",mode="w") as file:
    for song in titles:
        file.write(f"{song}\n")

print(titles)
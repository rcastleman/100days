from dotenv import load_dotenv
load_dotenv()
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ.get("CLIENT_ID")
SECRET = os.environ.get("SECRET")
REDIRECT = os.environ.get("REDIRECT")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=SECRET,
                                               redirect_uri=REDIRECT,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])


# set up spotify developer credentials and establish connection

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')


sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id=client_id,
                                                 client_secret= client_secret,
                                                 redirect_uri= redirect_uri,
                                                 scope= 'user-library-read'))

results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(f"{idx + 1}: {track['artists'][0]['name']} - {track['name']}")


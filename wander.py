# Selecting random artist

import random
import string
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# retrieve sensitive information from environment variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')

# authenticate with Spotify API
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                 client_secret=client_secret,
                                                 redirect_uri=redirect_uri,
                                                 scope=['user-library-read',
                                                         'user-read-recently-played',
                                                         'user-top-read']))

characters = string.ascii_letters + string.digits
random_char = random.choice(characters)

result = sp.search(q = random_char,
                   type='artist',
                   limit = 50)
random_artist = random.choice(result['artists']['items'])
print(f"Selected Artist: {random_artist['name']}")
print(f"Genres: {random_artist['genres']}")
print(f"Spotify URL: {random_artist['external_urls']['spotify']}")
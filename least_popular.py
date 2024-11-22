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


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                 client_secret=client_secret,
                                                 redirect_uri=redirect_uri,
                                                 scope=['user-library-read',
                                                         'user-read-recently-played',
                                                         'user-top-read']))

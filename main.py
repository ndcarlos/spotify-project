# import necessary libraries
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

# retrieve the top 10 artists for the current user using the 'medium_term' time range
try:
    results = sp.current_user_top_artists(limit=3, time_range='medium_term')
except spotipy.exceptions.SpotifyException as e:
    print(f"Error retrieving top artists: {e}")
    results = {'items': []}  # Handle error by providing an empty list for items


# iterate over the list of the artists returned in the results
for idx, artist in enumerate(results['items']):
    # print the index (starting from 1) and the name of each artist
    print(f"{idx + 1}. {artist['name']}")

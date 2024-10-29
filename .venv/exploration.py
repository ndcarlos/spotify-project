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


def get_artist_id(artist_name):
    # Search for the artist by name
    search_results = sp.search(q=artist_name, type='artist', limit=1)

    # Check if any results were found
    if search_results['artists']['items']:
        artist = search_results['artists']['items'][0]
        artist_id = artist['id']
        artist_name = artist['name']
        print(f"Artist: {artist_name}, ID: {artist_id}")
        return artist_id
    else:
        print(f"No artist found with the name: {artist_name}")
        return None


saved_tracks = sp.current_user_saved_tracks()
print(saved_tracks, 10)

artist_ids = set()

for item in saved_tracks['items']:
    for artist in item['track']['artists']:
        artist_ids.add(artist['id'])

for id in artist_ids:
    print(id)

# for idx, item in enumerate(saved_tracks['items']):
#     track = item['track']
#     artists = track['artists']
#     for artist in artists:
#         print(artist['name'])

# Example usage with multiple artists
# artists = ["Dua Lipa", "Beyoncé", "Charli XCX"]
# artist_ids = {artist: get_artist_id(artist) for artist in artists}

# print(artist_ids['Dua Lipa'])





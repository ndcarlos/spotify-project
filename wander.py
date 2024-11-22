# Selecting random artist

import random
import string
import spotipy
import os
import requests
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from get_token import response

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
                                                        'user-top-read',
                                                        'playlist-modify-public']))
# retrieving random artist
characters = string.ascii_letters + string.digits
random_char = random.choice(characters)

result = sp.search(q = random_char,
                   type='artist',
                   limit = 50)
random_artist = random.choice(result['artists']['items'])
# print(f"Selected Artist: {random_artist['name']}")
# print(f"Genres: {random_artist['genres']}")
# print(f"Artist ID : {random_artist['id']}")
# print(f"Spotify URL: {random_artist['external_urls']['spotify']}")


# retrieving top songs for random_artist
def get_top_tracks(artist_id, market="US"):
    headers = {
        "Authorization": f"Bearer {response}"
    }

    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"

    top_tracks = sp.artist_top_tracks(artist_id, country='US')['tracks']
    # Extract the top 5 tracks
    top_tracks = [
        {"name": track['name'], "id": track['id'], "popularity": track['popularity']}
        for track in top_tracks[:5]
    ]
    return top_tracks

top_tracks = get_top_tracks(random_artist['id'])

def get_or_create_playlist(user_id, playlist_name):
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            print(f"Playlist {playlist_name} already exists.")
            return(playlist['id'])

    # creating new playlist if it does not exist
    print(f"Creating new playlist {playlist_name}")
    new_playlist = sp.user_playlist_create(
        user = user_id,
        name = playlist_name,
        public = True)
    return(new_playlist['id'])

def add_tracks_to_playlist(playlist_id, track_ids):
    sp.playlist_add_items(playlist_id, track_ids)
    print(f"Selected Artist: {random_artist['name']}")
    print(f"Genres: {random_artist['genres']}")
    print(f"Added {len(track_ids)} tracks by to the playlist.")


# Get the user's ID
user_id = sp.current_user()['id']

# Get top tracks
top_tracks = get_top_tracks(random_artist['id'])

# Extract track IDs
track_ids = [track['id'] for track in top_tracks]

# Specify playlist name
playlist_name = "wander👣🪩"

# Get or create the playlist
playlist_id = get_or_create_playlist(user_id, playlist_name)

# Add tracks to the playlist
add_tracks_to_playlist(playlist_id, track_ids)
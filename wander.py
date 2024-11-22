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
def get_artists_by_genre(genre_name = None):
    # Search for artists with a specific genre name
    if genre_name:
        result = sp.search(q=f'genre:{genre_name}' if genre_name else '',
                           type='artist',
                           limit=50)
    else:
        result = sp.search(q='*',
                           type = 'artist',
                           limit = 50)

    if result['artists']['items']:
        random_artist = random.choice(result['artists']['items'])
        return random_artist
    else:
        return None
# print(f"Selected Artist: {random_artist['name']}")
# print(f"Genres: {random_artist['genres']}")
# print(f"Artist ID : {random_artist['id']}")
# print(f"Spotify URL: {random_artist['external_urls']['spotify']}")


# retrieving top songs for random_artist
def get_top_tracks(artist_id, market="US"):
    top_tracks = sp.artist_top_tracks(artist_id, country='US')['tracks']
    # Extract the top 5 tracks
    top_tracks = [
        {"name": track['name'], "id": track['id'], "popularity": track['popularity']}
        for track in top_tracks[:5]
    ]
    return top_tracks

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

artist = get_artists_by_genre()
top_tracks = get_top_tracks(artist['id'])




# User inputs
genre = input("If you would like to wander within a specific genre, input it here (Or press Enter to skip)").strip()
track_count = input("Specify the number of steps you want to wander down this path (Default is 5)")
track_count = int(track_count) if track_count.isdigit() else 5


# Get the user's ID
user_id = sp.current_user()['id']

random_artist = get_artists_by_genre(genre_name= genre)
if random_artist:
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

else:
    print("No artist found for the specified genre")
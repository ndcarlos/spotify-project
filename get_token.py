# script for retrieving authorization tokens for data pulls
import os
import requests
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# retrieve client ID and secret from env variables
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')


token_url = "https://accounts.spotify.com/api/token"

# prepare request headers and body
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

# send the POST request
response = requests.post(token_url, headers = headers, data = data)

# print response
if response.status_code == 200:
    access_token = response.json().get('access_token')
    print(f"Access Token: {access_token}")
else:
    print(f"Error: {response.status_code}, {response.text}")

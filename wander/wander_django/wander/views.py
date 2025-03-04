# Create your views here.
import requests
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'wander')))
from . import wander
from django.shortcuts import render
from django.http import HttpResponse

def spotify_login(request):
    return render(request, "spotify_login.html", {
        "spotify_client_id": os.getenv("SPOTIPY_CLIENT_ID"),
        "spotify_redirect_uri": os.getenv("SPOTIPY_REDIRECT_URI"),
    })

# Landing and form processing page
def index(request):
	if request.method == "POST":
		#Extract the data from the form
		genre = request.POST.get('genre')
		track_count = request.POST.get('track_count')

		#Process data through wander.py
		result = wander.get_artists_by_genre(genre)


		return request, 'index.html', {'result:'}
	
	return render(request, 'wander/index.html')



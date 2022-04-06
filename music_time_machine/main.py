import requests
from bs4 import BeautifulSoup
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

billboard_url = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    cache_path=".cache"
    )
)

user_id = sp.current_user()["id"]

date = input("What year would you like to travel to? The date format should be YYYY-MM-DD: ")

if bool(re.match(r"[1-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", f"{date}")):
    pass
else:
    while bool(re.match(r"[1-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", f"{date}")) is False:
        date = input("Please type the date in the format YYYY-MM-DD: ")

billboard = requests.get(billboard_url)
billboard_soup = BeautifulSoup(billboard.content, "html.parser")
song_titles_data = billboard_soup.select(".o-chart-results-list__item h3")
song_titles = [song.text.strip() for song in song_titles_data]

year = date[:4]
song_ids = []

for song in song_titles:
    result = sp.search(f"track: {song}, year: {year}", type="track")
    try:
        song_ids.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_ids)

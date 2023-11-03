import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import pprint

# ask user what date they want to search
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

# scrape data for top 100 songs for the given date
URL = f"https://www.billboard.com/charts/hot-100/{date}"

data = requests.get(URL).text

soup = BeautifulSoup(data, "html.parser")

top_song = [soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText().strip()]


data_song_titles = soup.findAll(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")

song_titles = top_song + [title.getText().strip() for title in data_song_titles]
# print(song_titles)

# Create a private playlist on specified user
scope = "playlist-modify-private"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ["SPOTIPY_CLIENT_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], scope=scope))

# spotify.user_playlist_create("1292421614", "Billboard to Spotify", public=False, description="Takes top 100 music from date in past to create a Spotify playlist.")

# Search spotify for top 100 songs

song_uris = []

for title in song_titles:
    data = spotify.search(q=f"track:{title} year:{year}", type=["track"], market="US", limit=1)
    try:
        song_uris.append(data["tracks"]["items"][0]["uri"])
    except IndexError:
        pass

# song_uris = [spotify.search(q=f"track:{title} year:{year}", type=["track"], market="US", limit=1)["tracks"]["items"][0]["uri"] for title in song_titles]
print(song_uris)
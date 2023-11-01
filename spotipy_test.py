import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os

scope = "playlist-modify-private"
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["SPOTIPY_CLIENT_ID"], client_secret=os.environ["SPOTIPY_CLIENT_SECRET"], redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"], scope=scope))

spotify.user_playlist_create("1292421614", "Billboard to Spotify", public=False, description="Takes top 100 music from date in past to create a Spotify playlist.")

# create_playlist_url = "https://api.spotify.com/v1/users/1292421614/playlists"
# params = {
#     "name": "Billboard to Spotify",
#     "description": "Takes top 100 music from date in past to create a Spotify playlist.",
#     "public": False
# }

# status = requests.post(url=create_playlist_url, params=params)

# print(status)

# results = spotify.artist_albums(jk_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])
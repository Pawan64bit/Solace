import spotipy
import pytube
from spotipy.oauth2 import SpotifyClientCredentials
CLIENT_ID='a12d89d9ac7d4b478ba5a97ee02e1d03'
SECRET_KEY='a7e4b0cfc9bf4fa39fc0c4b94f7d86be'


# Authenticate using Client Credentials Flow
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=SECRET_KEY)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Example: search for a track
track_results = sp.search(q='track:Shape of You artist:Ed Sheeran', type='track')
for track in track_results['tracks']['items']:
    print(track['name'], track['artists'][0]['name'])

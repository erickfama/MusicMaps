import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotify_api_creds import CLIENT_ID, CLIENT_SECRET

# Set up Spotify API credentials
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# List of Mexican states
mexican_states = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas",
    "Chihuahua", "Coahuila", "Colima", "Durango", "Guanajuato", "Guerrero", "Hidalgo",
    "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca",
    "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora",
    "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"
]

def get_top_artist_by_state(state):
    # Search for playlists related to the state
    results = sp.search(q=f'playlist {state} mexico', type='playlist', limit=1)
    
    if not results['playlists']['items']:
        return None
    
    playlist_id = results['playlists']['items'][0]['id']
    
    # Get tracks from the playlist
    tracks = sp.playlist_tracks(playlist_id, limit=50)
    
    # Count artist occurrences
    artist_count = {}
    for item in tracks['items']:
        if item['track'] and item['track']['artists']:
            artist_name = item['track']['artists'][0]['name']
            artist_count[artist_name] = artist_count.get(artist_name, 0) + 1
    
    # Find the most common artist
    if artist_count:
        top_artist = max(artist_count, key=artist_count.get)
        return top_artist
    else:
        return None

# Get top artist for each state
top_artists_by_state = {}
for state in mexican_states:
    top_artist = get_top_artist_by_state(state)
    if top_artist:
        top_artists_by_state[state] = top_artist

# Save the dictionary to a file
output_path = os.path.join('data', 'top_artists.py')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("top_artists_by_state = ")
    json.dump(top_artists_by_state, f, ensure_ascii=False, indent=4)
    f.write("\n")

print(f"Top artists by state have been saved to {output_path}")
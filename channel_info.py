import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUR_API_KEY = os.getenv('GOOGLE_API_KEY')
CHANNEL_HANDLE = 'MrBeast'

url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={YOUR_API_KEY}'

def get_playlist_id(url: str) -> str:
    response = requests.get(url=url)
    data = response.json()
    playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"]['uploads']

    return playlist_id

if __name__ == '__main__':
  print(get_playlist_id(url))
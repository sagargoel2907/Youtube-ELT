import requests
import os
from dotenv import load_dotenv

load_dotenv()

YOUR_API_KEY = os.getenv('GOOGLE_API_KEY')
CHANNEL_HANDLE = 'MrBeast'


def get_playlist_id() -> str:
    base_url = f'https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={YOUR_API_KEY}'
    response = requests.get(url=base_url)
    data = response.json()
    playlist_id = data["items"][0]["contentDetails"]["relatedPlaylists"]['uploads']

    return playlist_id

def get_video_ids(playlist_id: str) -> list[str]:
    base_url = f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&playlistId={playlist_id}&key={YOUR_API_KEY}'

    next_page_token: str | None = None
    videos_ids: list[str] = []

    while(True):
        if next_page_token:
            base_url += f'&nextPageToken={next_page_token}'
        response = requests.get(base_url)
        data = response.json()
        for item in data['items']:
            video_id = item['contentDetails']['videoId']
            videos_ids.append(video_id)
        next_page_token = data['nextPageToken']
        if not next_page_token or len(videos_ids)>100:
            break
    
    return videos_ids



if __name__ == '__main__':
  print(get_video_ids(playlist_id=get_playlist_id()))
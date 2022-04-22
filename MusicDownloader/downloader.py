from youtubesearchpython import VideosSearch
from pytube import YouTube
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
AUDIO_DOWNLOAD_PATH = Path(SCRIPT_DIR, '../converted_to_mp3/').resolve()
VIDEO_DOWNLOAD_PATH = Path(SCRIPT_DIR, '../downloaded_mp4/').resolve()

def search_video(query):
    return VideosSearch(query, limit = 1).result()['result'][0]['link']

def download_video_from_link(link, path=VIDEO_DOWNLOAD_PATH, filename=None):
    if not filename is None:
        filename += '.mp4'
    yt = YouTube(link).streams.filter(mime_type='video/mp4').filter(res='480p').first().download(output_path=path, filename=filename)

def download_audio_from_link(link, path=AUDIO_DOWNLOAD_PATH, filename=None):
    if not filename is None:
        filename += '.mp3'
    YouTube(link).streams.filter(mime_type='audio/mp4').order_by('abr').desc().first().download(output_path=path, filename=filename)
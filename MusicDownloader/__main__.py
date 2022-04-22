import os
import sys
from pathlib import Path

from reader import *
from downloader import *

SCRIPT_DIR = Path(__file__).parent.resolve()

def main():
    query = 'Architects - Doomsday'
    link = search_video(query)
    try:
        download_audio_from_link(link=link, filename=query)
        print('downloaded audio ' + query)
    except Exception:
        download_video_from_link(link=link, filename=query)
        print(' <!> downloaded video ' + query)

if __name__ == '__main__':
    main()
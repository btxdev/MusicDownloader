import os
import sys
from pathlib import Path

from reader import *
from downloader import *

SCRIPT_DIR = Path(__file__).parent.resolve()

def main():
    query = 'Architects - Doomsday'
    search_video(query)

if __name__ == '__main__':
    main()
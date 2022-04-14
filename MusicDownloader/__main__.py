import os
import sys
from pathlib import Path

from reader import *

SCRIPT_DIR = Path(__file__).parent.resolve()

def main():
    path = Path('C:/Users/sadom/Desktop/spotify_playlists').resolve()
    path2 = Path('C:/Users/sadom/Desktop/spotify_playlists', 'thall.csv').resolve()
    names = read_csv_files_in_directory(path)
    #names = read_csv_file(path2)
    
    for name in names:
        print(name)

if __name__ == '__main__':
    main()
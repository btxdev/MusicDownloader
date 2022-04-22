import os
import sys
from pathlib import Path

from reader import *
from downloader import *

SCRIPT_DIR = Path(__file__).parent.resolve()

def track_exists(playlist, track):
    path = Path(SCRIPT_DIR, '../converted_to_mp3/', playlist, track + '.mp3')
    return path.is_file()

def create_directories(name):
    dirs = (
        Path(SCRIPT_DIR, '../converted_to_mp3/'),
        Path(SCRIPT_DIR, '../downloaded_mp4/')
    )
    for path in dirs:
        path = Path(path, name)
        try:
            Path.mkdir(path)
        except FileExistsError:
            pass

def main():

    errors = []

    # read the names of playlists
    csv_files_parent_dir = Path('C:/Users/sadom/Desktop/spotify_playlists_to_download').resolve()
    csv_files = searching_all_files(csv_files_parent_dir)

    for csv_file in csv_files:
        playlist_name = csv_file.stem
        create_directories(playlist_name)
        
        print('')
        print('Downloading playlist "{}"...'.format(playlist_name))

        # get the names of songs from csv file
        tracks = read_csv_file(csv_file)
        tracks_count = len(tracks)
        tracks_downloaded = 0

        # download
        for query in tracks:

            # skip existing tracks
            if track_exists(playlist_name, query):
                tracks_downloaded += 1
                print(' [skipped] ({}/{}) {}'.format(tracks_downloaded, tracks_count, query))
                continue

            # find links for track and download
            link = search_video(query)
            audio_download_path = Path(SCRIPT_DIR, '../converted_to_mp3/', playlist_name)
            video_download_path = Path(SCRIPT_DIR, '../downloaded_mp4/', playlist_name)
            tracks_downloaded += 1
            try:
                download_audio_from_link(link=link, path=audio_download_path, filename=query)
                print('({}/{}) {}'.format(tracks_downloaded, tracks_count, query))
            except Exception as exc1:
                try:
                    download_video_from_link(link=link, path=video_download_path, filename=query)
                    print(' [video] ({}/{}) {}'.format(tracks_downloaded, tracks_count, query))
                except Exception as exc2:
                    print(' [error] Cannot download this track "{}"'.format(query))
                    print(exc2)
                    errors.append(query)

    # print list of failed songs
    if len(errors) > 0:
        print()
        print('These songs have not been downloaded:')
        i = 1
        for track in errors:
            print(' {}. {}'.format(i, track))
            i += 1

if __name__ == '__main__':
    main()
import os
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.append(Path(SCRIPT_DIR, '../MusicDownloader/').resolve())

from downloader import *

class TestDownloaderMethods(unittest.TestCase):
    
    def search_video_test(self):
        name = 'Gojira - Stranded'
        result = type(search_video(name)) is str
        self.assertTrue(result)
            
    def download_video_from_link_test(self):
        location = Path(SCRIPT_DIR, '../downloaded_mp4/').resolve()
        name = 'test'
        filename = name + '.mp4'
        link = 'https://www.youtube.com/watch?v=FNdC_3LR2AI'

        if Path(location, filename).is_file():
            os.remove(Path(location, filename).resolve())

        download_video_from_link(link=link, path=location, filename=name)
        result = Path(location, filename).is_file()
        os.remove(Path(location, filename).resolve())
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
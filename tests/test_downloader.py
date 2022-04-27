import os
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.append(str(Path(SCRIPT_DIR, '../MusicDownloader/').resolve()))

from downloader import *

class TestDownloaderMethods(unittest.TestCase):
    
    def test_search_video(self):
        name = 'Gojira - Stranded'
        result = type(search_video(name)) is str
        self.assertTrue(result)
            
    def test_download_video_from_link(self):
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
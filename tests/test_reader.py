import os
import sys
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
sys.path.append(str(Path(SCRIPT_DIR, '../MusicDownloader/').resolve()))

from reader import *

class TestReaderMethods(unittest.TestCase):
    
    def test_read_txt_file(self):
        path = Path(SCRIPT_DIR, 'files/tracks.txt').resolve()
        names = read_txt_file(path)
        check = [
            'Gojira - Stranded',
            'Metallica - Enter Sandman'
            ]
        self.assertEqual(names, check)

    def test_read_txt_files_in_directory(self):
        path = Path(SCRIPT_DIR, 'files/txt_tracklists/').resolve()
        names = read_txt_files_in_directory(path)
        check = [
            'Gojira - Stranded',
            'Metallica - Enter Sandman',
            'Meshuggah - Bleed',
            'Architects - Hereafter',
            'Lost Society - Deliever Me'
            ]
        self.assertEqual(names, check)

if __name__ == '__main__':
    unittest.main()
import unittest
from src.song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("My Way", "Frank Sinatra")

    def test_song_has_title(self):
        self.assertEqual("My Way", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Frank Sinatra", self.song.artist)

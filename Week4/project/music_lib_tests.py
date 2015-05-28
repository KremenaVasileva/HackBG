from music_library import Song
import unittest


class TestMusicLibrary(unittest.TestCase):
    def setUp(self, **kwargs):
        self.song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.title = "Odin"
        self.artist = "Manowar"
        self.album = "The Sons of Odin"
        self.length = "3:44"

    def test_init(self):
        self.assertEqual(self.song.title, "Odin")
        self.assertEqual(self.song.artist, "Manowar")
        self.assertEqual(self.song.album, "The Sons of Odin")
        self.assertEqual(self.song.length, "3:44")
        self.assertTrue(isinstance(self.song, Song))

    def test_str(self):
        needed_result = "Manowar - Odin from The Sons of Odin - 3:44"
        self.assertEqual(str(self.song), needed_result)

    def test_eq(self):
        eq_song = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertTrue(self.song == eq_song)


if __name__ == '__main__':
    unittest.main()

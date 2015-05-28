class Song:
    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.artist = kwargs['artist']
        self.album = kwargs['album']
        self.length = kwargs['length']

    def __str__(self):
        return "{} - {} from {} - {}".format(
            self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        eq_title = self.title == other.title
        eq_artist = self.artist == other.artist
        eq_album = self.album == other.album
        eq_length = self.length == other.length
        return all([eq_title, eq_artist, eq_album, eq_length])

    def __hash__(self):
        return hash(self.title)

    def get_length(self):
        return self.length

    def length_in_seconds(self, seconds=True):
        seconds = 0
        length_list = self.length.split(":")
        length_list = length_list[::-1]

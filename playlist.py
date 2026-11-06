class Playlist:
    def __init__(self, pl):
        self.pl = pl
        self.song_counter = 0
        self.playlist = []

    def add_song(self, title):
        if self.song_counter < 3:
            self.song_counter += 1
            self.playlist.append(title)
        else:
            raise ValueError()

    def count(self):
        return len(self.playlist )

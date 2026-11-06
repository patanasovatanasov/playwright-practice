class Playlist:
    limit = 3
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title):
        if len(self.songs) < Playlist.limit:
            self.songs.append(title)
        else:
            raise ValueError()

    def count(self):
        return len(self.songs)

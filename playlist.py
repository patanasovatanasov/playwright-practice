class Playlist:
    limit = 3
    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, title):
        if len(self.playlist) < Playlist.limit:
            self.playlist.append(title)
        else:
            raise ValueError()

    def count(self):
        return len(self.playlist)

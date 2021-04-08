class Song(object):
    release = ""
    artist_name = ""
    title = ""
    year = -1

    def __init__(self, o):
        self.release = o["release"]
        self.artist_name = o["artist_name"]
        self.title = o["title"]
        self.year = o["year"]

    def print(self):
        print(self.release)
        print(self.artist_name)
        print(self.title)
        print(self.year)
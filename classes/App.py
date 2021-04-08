class App(object):
    name = ""
    version = ""
    size_bytes = 0
    genre = ""
    rating = 0.0

    def __init__(self, o):
        self.name = o["name"]
        self.version = o["version"]
        self.size_bytes = o["size_bytes"]
        self.genre = o["genre"]
        self.rating = o["rating"]

    def print(self):
        print(self.name)
        print(self.version)
        print(self.size_bytes)
        print(self.genre)
        print(self.rating)




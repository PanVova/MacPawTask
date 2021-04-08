class Book(object):
    original_title = ""
    average_rating = 0.0
    authors = ""
    language_code = ""

    def __init__(self, o):
        self.original_title = o["original_title"]
        self.average_rating = o["average_rating"]
        self.authors = o["authors"]
        self.language_code = o["language_code"]

    def print(self):
        print(self.original_title)
        print(self.average_rating)
        print(self.authors)
        print(self.language_code)



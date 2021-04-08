class Movie(object):
    is_adult = False
    original_title = ""
    release_date = ""
    original_language = ""
    budget = 0

    def __init__(self, o):
        self.is_adult = o["is_adult"]
        self.original_title = o["original_title"]
        self.release_date = o["release_date"]
        self.original_language = o["original_language"]
        self.budget = o["budget"]

    def print(self):
        print(self.is_adult)
        print(self.original_title)
        print(self.release_date)
        print(self.original_language)
        print(self.budget)




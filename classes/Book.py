from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base = declarative_base()


class Book(Base, object):
    __tablename__ = 'Book'

    id = Column(Integer, primary_key=True)
    original_title = Column(String)
    average_rating = Column(Float)
    authors = Column(String)
    language_code = Column(String)

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

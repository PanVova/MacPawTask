from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base = declarative_base()


class Movie(Base, object):
    __tablename__ = 'Movie'

    id = Column(Integer, primary_key=True)
    is_adult = Column(Boolean)
    original_title = Column(String)
    release_date = Column(String)
    original_language = Column(String)
    budget = Column(Integer)

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

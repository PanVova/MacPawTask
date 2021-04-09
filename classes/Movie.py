from sqlalchemy import Column, Integer, Boolean, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    is_adult = Column(Boolean)
    original_title = Column(VARCHAR)
    release_date = Column(VARCHAR)
    original_language = Column(VARCHAR)
    budget = Column(Integer)
    original_title_normalized = Column(VARCHAR)

    def __init__(self, o):
        self.is_adult = o["is_adult"]
        self.original_title = o["original_title"]
        self.release_date = o["release_date"]
        self.original_language = o["original_language"]
        self.budget = o["budget"]
        self.original_title_normalized = self.original_title.replace(" " ,"_").replace(":" ,"_").replace("-" ,"_").replace("___","_").replace("__","_").lower()

    def print(self):
        print(self.is_adult)
        print(self.original_title)
        print(self.release_date)
        print(self.original_language)
        print(self.budget)

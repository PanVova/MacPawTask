from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base = declarative_base()

class Song(Base, object):
    __tablename__ = 'Song'

    id = Column(Integer, primary_key=True)
    release = Column(String)
    artist_name = Column(String)
    title = Column(String)
    year = Column(Integer)

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
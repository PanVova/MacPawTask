from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float

Base = declarative_base()


class App(Base, object):
    __tablename__ = 'App'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    size_bytes = Column(Integer)
    genre = Column(String)
    rating = Column(Float)

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

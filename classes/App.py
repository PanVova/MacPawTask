from sqlalchemy import Column, Integer, Float, VARCHAR, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class App(Base):
    __tablename__ = 'apps'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    version = Column(VARCHAR)
    size_bytes = Column(Integer)
    genre = Column(VARCHAR)
    rating = Column(Float)
    is_awesome = Column(Boolean)

    def __init__(self, o):
        self.name = o["name"]
        self.version = o["version"]
        self.size_bytes = o["size_bytes"]
        self.genre = o["genre"]
        self.rating = o["rating"]
        self.is_awesome = self.rating > 4.0 and True or False

    def print(self):
        print(self.name)
        print(self.version)
        print(self.size_bytes)
        print(self.genre)
        print(self.rating)
        print(self.is_awesome)

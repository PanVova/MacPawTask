from datetime import datetime
from sqlalchemy import Column, Integer, VARCHAR, DATETIME
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True)
    release = Column(VARCHAR)
    artist_name = Column(VARCHAR)
    title = Column(VARCHAR)
    year = Column(Integer)
    ingestion_time = Column(DATETIME)

    def __init__(self, o):
        self.release = o["release"]
        self.artist_name = o["artist_name"]
        self.title = o["title"]
        self.year = o["year"]
        self.ingestion_time = datetime.now()

    def print(self):
        print(self.release)
        print(self.artist_name)
        print(self.title)
        print(self.year)
        print(self.ingestion_time)

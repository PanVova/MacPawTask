import json

import aiohttp
import asyncio
import time

from sqlalchemy.orm import sessionmaker

from classes.App import App
from classes.Book import Book
from classes.Movie import Movie
from classes.Song import Song
import requests
import sqlalchemy as sa

engine = sa.create_engine("sqlite:///DB.db")
metadata = sa.MetaData()
metadata.create_all(engine)
Session = sessionmaker(engine)
ses = Session()


def create_db():
    sa.Table("App", metadata,
             sa.Column("id", sa.Integer, primary_key=True),
             sa.Column("name", sa.String(100), nullable=False, unique=False),
             sa.Column("version", sa.String(100), nullable=False, unique=False),
             sa.Column("size_bytes", sa.Integer, nullable=False, unique=False),
             sa.Column("genre", sa.String(50), nullable=False, unique=False),
             sa.Column("rating", sa.Float, nullable=False, unique=False))

    sa.Table("Movie", metadata,
             sa.Column("id", sa.Integer, primary_key=True),
             sa.Column("is_adult", sa.Boolean, nullable=False, unique=False),
             sa.Column("original_title", sa.String(100), nullable=False, unique=False),
             sa.Column("release_date", sa.String(100), nullable=False, unique=False),
             sa.Column("original_language", sa.String(50), nullable=False, unique=False),
             sa.Column("budget", sa.Integer, nullable=False, unique=False))

    sa.Table("Song", metadata,
             sa.Column("id", sa.Integer, primary_key=True),
             sa.Column("release", sa.String(100), nullable=False, unique=False),
             sa.Column("artist_name", sa.String(100), nullable=False, unique=False),
             sa.Column("title", sa.String(100), nullable=False, unique=False),
             sa.Column("year", sa.Integer, nullable=False, unique=False)
             )

    sa.Table("Book", metadata,
             sa.Column("id", sa.Integer, primary_key=True),
             sa.Column("original_title", sa.String(100), nullable=False, unique=False),
             sa.Column("average_rating", sa.Float, nullable=False, unique=False),
             sa.Column("authors", sa.String(100), nullable=False, unique=False),
             sa.Column("language_code", sa.String(100), nullable=False, unique=False))


async def requesting(url):
    try:
        async with aiohttp.ClientSession() as session:
            result = await session.get("https://data-engineering-interns.macpaw.io/" + url, allow_redirects=True)
            text = await open('files/' + url, 'wb').write(await result.read())
            return text
    except Exception:
        return f"error! No data returned from {url}"


def read_file(file):
    with open("files/" + file) as f:
        data = json.loads(f.read())

    for i in range(0, len(data)):
        type = data[i]['type']
        if type == 'song':

            result = Song(data[i]['data'])
            ses.add(result)

        elif type == "app":

            result = App(data[i]['data'])
            ses.add(result)

        elif type == "movie":

            result = Movie(data[i]['data'])
            ses.add(result)

        elif type == "book":

            result = Book(data[i]['data'])
            ses.add(result)

        ses.commit()


def download_file(url, name):
    result = requests.get(url, allow_redirects=True)
    open('files/' + name, 'wb').write(result.content)


def read_files_list():  # add async
    with open("files/files_list.data") as file:
        return file.read().split("\n")


def main():
    print("START")
    start = time.time()
    download_file('https://data-engineering-interns.macpaw.io/files_list.data', name="files_list.data")
    url_list = read_files_list()
    coros = [requesting(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*coros))
    loop.close()
    print("DOWNLOADED ALL")
    print("CREATED DB")
    create_db()



    for i in read_files_list():
        pass
        #print(i)
        read_file(i)
    print("ENDED")
    print(f"Async result: {time.time() - start}")


if __name__ == '__main__':
    main()


# make faster loading into DB
# divide it to classes
# refactor

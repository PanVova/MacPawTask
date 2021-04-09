import asyncio
import json
import time

import aiohttp
import requests
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from classes.App import App
from classes.Movie import Movie
from classes.Song import Song

engine = sa.create_engine("sqlite:///DB.db")
metadata = sa.MetaData()

sa.Table("apps", metadata,
         sa.Column("id", sa.Integer, primary_key=True),
         sa.Column("name", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("version", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("size_bytes", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("genre", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("rating", sa.Float, nullable=False, unique=False),
         sa.Column("is_awesome",sa.Boolean,nullable=False,unique=False))

sa.Table("movies", metadata,
         sa.Column("id", sa.Integer, primary_key=True),
         sa.Column("is_adult", sa.Boolean, nullable=False, unique=False),
         sa.Column("original_title", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("release_date", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("original_language", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("budget", sa.Integer, nullable=False, unique=False),
         sa.Column("original_title_normalized", sa.VARCHAR, nullable=False, unique=False))

sa.Table("songs", metadata,
         sa.Column("id", sa.Integer, primary_key=True),
         sa.Column("release", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("artist_name", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("title", sa.VARCHAR, nullable=False, unique=False),
         sa.Column("year", sa.Integer, nullable=False, unique=False),
         sa.Column("ingestion_time", sa.DATETIME, nullable=False, unique=False))

metadata.create_all(engine)
Session = sessionmaker(engine)
ses = Session()


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

        ses.commit()


def download_file(url, name):
    result = requests.get(url, allow_redirects=True)
    open('files/' + name, 'wb').write(result.content)


def read_files_list():  # add async
    with open("files/files_list.data") as file:
        return file.read().split("\n")


def main():
    print("START")
    print("CREATED DB")
    start = time.time()
    download_file('https://data-engineering-interns.macpaw.io/files_list.data', name="files_list.data")
    url_list = read_files_list()
    coros = [requesting(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*coros))
    loop.close()
    print("DOWNLOADED ALL")

    for i in read_files_list():
        pass
        # print(i)
        read_file(i)
    print("END")
    print(f"Async result: {time.time() - start}")


if __name__ == '__main__':
    main()


# read one more time how to work with acquired data
# refactor

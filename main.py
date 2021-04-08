import json

import aiohttp
import asyncio

import time

from classes.App import App
from classes.Book import Book
from classes.Movie import Movie
from classes.Song import Song
import requests


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
            Song(data[i]['data'])
        elif type == "app":
            App(data[i]['data'])
        elif type == "movie":
            Movie(data[i]['data'])
        elif type == "book":
            Book(data[i]['data'])


def download_file(url, name):
    result = requests.get(url, allow_redirects=True)
    open('files/' + name, 'wb').write(result.content)


def read_files_list():  # add async
    with open("files/files_list.data") as file:
        return file.read().split("\n")


def main():

    start = time.time()
    download_file('https://data-engineering-interns.macpaw.io/files_list.data', name="files_list.data")
    url_list = read_files_list()
    coros = [requesting(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*coros))
    loop.close()

    for i in url_list:
        #print(i)
        read_file(i)
    print(f"Async result: {time.time() - start}")


if __name__ == '__main__':
    main()

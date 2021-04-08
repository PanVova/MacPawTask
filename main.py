import json

from classes.App import App
from classes.Book import Book
from classes.Movie import Movie
from classes.Song import Song
import requests


def read_file(file):
    with open("files/"+file) as f:
        data = json.loads(f.read())

    for i in range(0, len(data)):
        type = data[i]['type']
        if type == 'song':
            Song(data[i]['data']).print()
        elif type == "app":
            App(data[i]['data']).print()
        elif type == "movie":
            Movie(data[i]['data']).print()
        elif type == "book":
            Book(data[i]['data']).print()
            


def download_file(url, name):
    r = requests.get(url, allow_redirects=True)
    open('files/' + name, 'wb').write(r.content)


def read_files_list():  # add async
    with open("files/files_list.data") as file:
        return file.read().split("\n")


def main():
    download_file('https://data-engineering-interns.macpaw.io/files_list.data', name="files_list.data")
    for i in read_files_list():
        print(i)
        download_file("https://data-engineering-interns.macpaw.io/" + i, name=i)
        read_file(i)


if __name__ == '__main__':
    main()


    # и сделать сам прогон программы - чтение json файликов

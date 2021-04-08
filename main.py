import json

from classes.App import App
from classes.Book import Book
from classes.Movie import Movie
from classes.Song import Song

def main():
    with open("files/1.json") as f:
        data = json.loads(f.read())
        print(len(data))

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

        print(type)


if __name__ == '__main__':
    main()

    # Научиться скачивать файл в эту директорию
    # считывать все названия и по очереди их проганять через нашу программу
    # и сделать сам прогон программы - чтение json файликов

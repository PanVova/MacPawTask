import json


def main():
    with open("files/1.json") as f:
        data = json.loads(f.read())
        print(len(data))

    for i in range(0, len(data)):
        type = data[i]['type']
        if type == 'song':
            from classes.Song import Song
            Song(data[i]['data']).print()
        elif type == "app":
            print(2)
        elif type == "movie":
            print(3)
        elif type == "book":
            print(4)

        print(type)


if __name__ == '__main__':
    main()

    # Научиться скачивать файл в эту директорию
    # считывать все названия и по очереди их проганять через нашу программу
    # и сделать сам прогон программы - чтение json файликов

import json


def main():
    with open('files/1.data') as f:
        data = json.load(f)

    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    print(data)


if __name__ == '__main__':
    main()

    # Научиться скачивать файл в эту директорию
    # считывать все названия и по очереди их проганять через нашу программу
    # и сделать сам прогон программы - чтение json файликов
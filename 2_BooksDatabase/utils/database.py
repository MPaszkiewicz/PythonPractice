import json


database_file = 'database.txt'


class DataNotFoundError(Exception):
    pass


def read_database():
    books = []
    try:
        with open(database_file, 'r') as database:
            books = json.load(database)
    except FileNotFoundError:
        print("Database file does not exist, returning empty dict.")
    except json.JSONDecodeError:
        print("Database file format was incorrect, returning empty dict.")
    return books


def write_database(books):
    with open(database_file, 'w') as database:
        json.dump(books, database)


def add(name, author, read):
    books = read_database()
    books.append({'name': name, 'author': author, 'read': read})
    write_database(books)


def get(name):
    books = read_database()
    for book in books:
        if book['name'] == name:
            return book
    raise DataNotFoundError("Found not find book with name {}".format(name))


def remove(name):
    books = read_database()
    books = [book for book in books if book['name'] != name]
    write_database(books)


def get_all():
    return read_database()


def update_read(name, new_read):
    books = read_database()
    for book in books:
        if book['name'] == name:
            book['read'] = new_read
    write_database(books)

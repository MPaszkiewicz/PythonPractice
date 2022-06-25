
books = []


class DataNotFoundError(Exception):
    pass


def add(name, author, read):
    books.append({'name': name, 'author': author, 'read': read})


def get(name):
    for book in books:
        if book['name'] == name:
            return book
    raise DataNotFoundError("Found not find book with name {}".format(name))


def remove(name):
    global books
    books = [book for book in books if book['name'] != name]


def get_all():
    return books


def update_read(name, new_read):
    book = get(name)
    book['read'] = new_read

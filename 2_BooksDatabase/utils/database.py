import sqlite3
from utils.database_connection import DatabaseConnection


class DataNotFoundError(Exception):
    pass


DATABASE_FILE = 'data.db'
BOOKS_TABLE_NAME = 'books'


def create_book_table():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS {}(name text primary key, author text, read integer)'
                   .format(BOOKS_TABLE_NAME))
    connection.commit()
    connection.close()


def add(name, author):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO {} VALUES(?, ?, 0)'.format(BOOKS_TABLE_NAME), (name, author))
    connection.commit()
    connection.close()


def get(name):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM {} WHERE name=?'.format(BOOKS_TABLE_NAME), (name,))
    book = cursor.fetchone()
    connection.close()
    if book is None:
        raise DataNotFoundError("Could not find book with name {}".format(name))
    return book


def remove(name):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('DELETE FROM {} WHERE name=?'.format(BOOKS_TABLE_NAME), (name,))
    connection.commit()
    connection.close()


def get_all():
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM {}'.format(BOOKS_TABLE_NAME))
    books = [{'name': row[0], 'author': row[1], 'read': row[2]}
             for row in cursor.fetchall()]  # fetchall returns list of tuples
    connection.close()
    return books


def update_read(name, new_read):
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('UPDATE {} SET read=? WHERE name=?'.format(BOOKS_TABLE_NAME), (new_read, name))
    connection.commit()
    connection.close()

import sqlite3
from utils.database_connection import DatabaseConnection


class DataNotFoundError(Exception):
    pass


DATABASE_FILE = 'data.db'
BOOKS_TABLE_NAME = 'books'


def create_book_table():
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS {}(name text primary key, author text, read integer)'
                       .format(BOOKS_TABLE_NAME))


def add(name, author):
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO {} VALUES(?, ?, 0)'.format(BOOKS_TABLE_NAME), (name, author))


def get(name):
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM {} WHERE name=?'.format(BOOKS_TABLE_NAME), (name,))
        book = cursor.fetchone()
        if book is None:
            raise DataNotFoundError("Could not find book with name {}".format(name))
        return book


def remove(name):
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM {} WHERE name=?'.format(BOOKS_TABLE_NAME), (name,))


def get_all():
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM {}'.format(BOOKS_TABLE_NAME))
        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]  # fetchall returns list of tuples
        return books


def update_read(name, new_read):
    with DatabaseConnection(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE {} SET read=? WHERE name=?'.format(BOOKS_TABLE_NAME), (new_read, name))

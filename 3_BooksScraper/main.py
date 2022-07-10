import requests
from parsers.books_parser import BooksPage, BookParser

page_content = requests.get('https://books.toscrape.com/').content

page = BooksPage(page_content)

books = page.books[:3]



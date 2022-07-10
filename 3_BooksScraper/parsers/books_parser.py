import re
import logging
from bs4 import BeautifulSoup
from locators.books_locators import BooksLocators


logger = logging.getLogger('scraping')


class BooksPage:
    def __init__(self, page):
        logger.info('Parsing page with BeautifulSoup HTML')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BooksLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(BooksLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        ret = re.search(pattern, content)
        return ret.group(1)


class BookParser:

    RATINGS_MAP = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book, title: {self.title}, price: {self.price},' \
               f'rating: {self.rating}, availability: {self.availability}, link: {self.link}>'

    @property
    def title(self):
        return self.parent.select_one(BooksLocators.BOOK_TITLE).attrs['title']

    @property
    def link(self):
        return self.parent.select_one(BooksLocators.BOOK_LINK).attrs['href']

    @property
    def price(self):
        price = float(self.parent.select_one(BooksLocators.BOOK_PRICE).string[1:])
        return price

    @property
    def rating(self):
        rating_str = next(r for r in self.parent.select_one(BooksLocators.BOOK_RATING).attrs['class']
                          if r != 'star-rating')
        return BookParser.RATINGS_MAP[rating_str]

    @property
    def availability(self):
        return self.parent.select_one(BooksLocators.BOOK_AVAILABILITY).text.strip()

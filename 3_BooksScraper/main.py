import requests
import logging
from parsers.books_parser import BooksPage, BookParser

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger('scraping')

logging.info('Loading books from website...')

books = []

page_num = 1
#while True:
for _ in range(3):
    logging.debug('Requesting page {}.'.format(page_num))
    url = f'https://books.toscrape.com/catalogue/page-{page_num}.html'
    page_request = requests.get(url)
    if page_request.status_code != 200:
        break
    page = BooksPage(page_request.content)
    books += page.books
    logging.debug('Loaded {} books so far.'.format(len(books)))
    page_num += 1

logging.info('Loaded {} books in total.'.format(len(books)))

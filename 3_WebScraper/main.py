import requests
from pages.quotes_page import QuotesPage

page_string = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(page_string)

for quote in page.quotes:
    print(quote)

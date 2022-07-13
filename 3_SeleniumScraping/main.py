from parsers.QuoteParsers import QuotesPage, InvalidTagForAuthorError

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

try:
    author = input("Enter author: ")
    tag = input("Enter tag: ")

    service = Service("D:/chromedriver/chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)
    quotes = page.search_for_quotes(author, tag)
    print(quotes)
except InvalidTagForAuthorError as e:
    print(e)
except Exception:
    print("An unknown error occurred. Please try again.")
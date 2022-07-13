from locators.QuotesLocators import QuotesLocators

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class InvalidTagForAuthorError(ValueError):
    pass


class Quote:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Quote<{self.content}>'

    @property
    def content(self):
        quote = self.parent.find_element(
            By.CSS_SELECTOR, QuotesLocators.QUOTE_CONTENT_LOCATOR
        )
        return quote.text


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def authors_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesLocators.AUTHOR_DROPDOWN
        )
        return Select(element)

    def get_available_authors(self):
        return [option.text.strip() for option in self.authors_dropdown.options]

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tags_dropdown(self):
        element = self.browser.find_element(
            By.CSS_SELECTOR, QuotesLocators.TAG_DROPDOWN
        )
        return Select(element)

    def get_available_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_author(self, author):
        self.authors_dropdown.select_by_visible_text(author)

    def select_tag(self, tag):
        self.tags_dropdown.select_by_visible_text(tag)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotesLocators.SEARCH_BUTTON)

    @property
    def quotes(self):
        return [Quote(e) for e in self.browser.find_elements(By.CSS_SELECTOR, QuotesLocators.QUOTE)]

    def wait_for_element(self, css_locator):
        WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, css_locator)
            )
        )

    def search_for_quotes(self, author, tag):
        self.select_author(author)
        self.wait_for_element(QuotesLocators.TAG_DROPDOWN_VALUE_OPTION)
        try:
            self.select_tag(tag)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author}' does not have any quotes tagged with '{tag}'."
            )
        self.search_button.click()
        self.wait_for_element(QuotesLocators.QUOTE)

        return self.quotes

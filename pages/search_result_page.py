from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR,'div.a-section span.a-color-state')

    def verify_search_result(self ,expected_text):
        self.verify_text(expected_text,*self.SEARCH_RESULT)
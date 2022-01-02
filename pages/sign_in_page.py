from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignIn(Page):
    SIGN_IN_TEXT=(By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_sign_in(self,expected_text):
        self.verify_text(expected_text,*self.SIGN_IN_TEXT)

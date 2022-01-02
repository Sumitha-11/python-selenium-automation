from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_PAGE_RESULT = (By.CSS_SELECTOR,"div[class*='sc-your-amazon-cart-is-empty']")
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container")
    CART_COUNT = (By.ID, "nav-cart-count")

    def cart_page_text(self):
        expected_Result = self.driver.find_element(*self.CART_PAGE_RESULT).text
        actual_Result = "Your Amazon Cart is empty"
        assert actual_Result == expected_Result, f"Actual_result does not match Expected_result"


    def click_cart_icon(self):
        self.click(*self.CART_ICON)


    def verify_cart_count(self,expected_count):
        actual_count = (self.driver.find_element(*self.CART_COUNT).text)
        assert int(actual_count) == int(expected_count), f"{actual_count} does not match {expected_count}"



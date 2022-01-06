from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import Page



class ProductDetails(Page):
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".a-size-mini a span")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    PROTECTION_PLAN = (By.CSS_SELECTOR, "#attachSiNoCoverage")
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container")
    NEW_ARRIVALS = (By.CSS_SELECTOR,"a[href*='/New-Arrivals/b/']")
    DIFFERENT_CATEGORY = (By.CSS_SELECTOR,"div.mega-menu")
    WOMEN_CATEGORY = (By.CSS_SELECTOR,"a[href*='/s?i=fashion-womens&bbn']")

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_LINK)

    def add_product_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BUTTON)

    def click_no_thanks(self):
        self.click(*self.PROTECTION_PLAN)
        self.wait_for_element_appear(*self.CART_ICON)

    def hover_new_arrivals(self):
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_category(self,expected_count):
        actual_count = len(self.find_elements(*self.DIFFERENT_CATEGORY))
        assert actual_count == int(expected_count) ,f"{actual_count} does not match {expected_count}"

    def verify_women_category(self):
        self.wait_for_element_appear(*self.WOMEN_CATEGORY)








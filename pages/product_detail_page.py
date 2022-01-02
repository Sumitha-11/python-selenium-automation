from selenium.webdriver.common.by import By

from pages.base_page import Page



class ProductDetails(Page):
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".a-size-mini a span")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    PROTECTION_PLAN = (By.CSS_SELECTOR, "#attachSiNoCoverage")
    CART_ICON = (By.CSS_SELECTOR, "#nav-cart-count-container")

    def click_first_product(self):
        self.click(*self.FIRST_PRODUCT_LINK)


    def add_product_to_cart(self):
        self.wait_for_element_click(*self.ADD_TO_CART_BUTTON)


    def click_no_thanks(self):
        self.click(*self.PROTECTION_PLAN)







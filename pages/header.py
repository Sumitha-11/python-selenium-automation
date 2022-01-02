from selenium.webdriver.common.by import By

from pages.base_page import Page

class Header(Page):
    SEARCH_INPUT =(By.CSS_SELECTOR,"#twotabsearchtextbox")
    SEARCH_ICON = (By.ID,"nav-search-submit-button")
    CLICK_ORDERS_AND_RETURNS = (By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_ICON =(By.CSS_SELECTOR,"span.nav-cart-icon")

    def search_input(self,text):
        self.input_text(text,*self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_order(self):
        self.click(*self.CLICK_ORDERS_AND_RETURNS)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
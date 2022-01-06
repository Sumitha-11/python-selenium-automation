from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import Page

class Header(Page):
    SEARCH_INPUT = (By.CSS_SELECTOR,"#twotabsearchtextbox")
    SEARCH_ICON = (By.ID,"nav-search-submit-button")
    CLICK_ORDERS_AND_RETURNS = (By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']")
    CART_ICON = (By.CSS_SELECTOR,"span.nav-cart-icon")
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    SPANISH_LANGUAGE = (By.XPATH, "//a[@href='#switch-lang=es_US']//span[text()='Español']")
    DROPDOWN_MENU = (By.ID,"searchDropdownBox")

    def search_input(self,text):
        self.input_text(text,*self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_order(self):
        self.click(*self.CLICK_ORDERS_AND_RETURNS)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def hover_language(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def spanish_language_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANGUAGE)

    def select_department(self,department: str):
        dropdown =self.find_element(*self.DROPDOWN_MENU)
        select = Select(dropdown)
        select.select_by_value(f"search-alias={department}")

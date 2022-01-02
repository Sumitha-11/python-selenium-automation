from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResults
from pages.sign_in_page import SignIn
from pages.cart_page import CartPage
from pages.product_detail_page import ProductDetails

class Application:

    def __init__(self,driver):
        self.driver = driver

        self.cart_page = CartPage(self.driver)
        self.header = Header(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_result_page = SearchResults(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.product_detail_page = ProductDetails(self.driver)




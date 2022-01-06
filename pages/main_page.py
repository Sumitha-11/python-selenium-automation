from pages.base_page import Page

class MainPage(Page):

    def open_product_page(self,product_id):
        self.open_page(f'gp/product/{product_id}')
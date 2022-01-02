import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLER_PAGE = (By.CSS_SELECTOR,"a[href*='/gp/bestsellers/']")
#SEARCH_TAB = (By.CSS_SELECTOR,"#twotabsearchtextbox")
#SEARCH_ICON=(By.ID,"nav-search-submit-button")


@given('Open Amazon page')
def open_Amazon(context):
    context.app.main_page.open_page()


@when('search for {product}')
def search_Product(context,product):
    context.app.header.search_input(product)


@when('Click on search button')
def click_search_button(context):
    context.app.header.click_search()


@when('Click on Orders and Returns')
def orders_returns(context):
    context.app.header.click_order()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@then('Click on BestSellers Page')
def click_bestseller_page(context):
    context.driver.find_element(*BEST_SELLER_PAGE).click()


@then('Results for {expected_text} are shown')
def search_results(context,expected_text):
    context.app.search_result_page.verify_search_result(expected_text)





from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

BEST_SELLER_PAGE = (By.CSS_SELECTOR,"a[href*='/gp/bestsellers/']")
SEARCH_TAB = (By.CSS_SELECTOR,"#twotabsearchtextbox")
SEARCH_BUTTON=(By.ID,"nav-search-submit-button")


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.Amazon.com')


@when('Click on Orders and Returns')
def orders_returns(context):
    context.driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()


@when('Click on cart icon')
def Click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"span.nav-cart-icon").click()


@then('Click on BestSellers Page')
def Click_BestSeller_Page(context):
    context.driver.find_element(*BEST_SELLER_PAGE).click()
    context.current_window= context.driver.current_window_handle
    print(context.current_window)


@when('Search for {product}')
def search_Product(context,product):
    context.driver.find_element(*SEARCH_TAB).send_keys(product)


@when('Click on search button')
def Click_search_button(context):
    context.driver.find_element(*SEARCH_BUTTON).click()



from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.Amazon.com')

@when('Click on Orders and Returns')
def orders_returns(context):
    context.driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()

@when('Click on cart icon')
def Click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"span.nav-cart-icon").click()


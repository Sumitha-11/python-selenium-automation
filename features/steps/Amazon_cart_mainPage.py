from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon webPage')
def open_amazon(context):
    context.driver.get("https://amazon.com")

@when('Click on cart icon')
def Click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,"span.nav-cart-icon").click()


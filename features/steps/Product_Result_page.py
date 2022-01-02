from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
import time

CART_ICON = (By.CSS_SELECTOR,"#nav-cart-count-container")
CART_COUNT=(By.ID,"nav-cart-count")


@then('Click on cart icon')
def Click_Cart_Icon(context):
    context.app.cart_page.click_cart_icon()


@then('Verify Cart has {expected_count} item')
def cart_count(context,expected_count):
    context.app.cart_page.verify_cart_count(expected_count)

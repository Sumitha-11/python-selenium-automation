from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify your cart is empty')
def verify_cart_empty(context):
    context.app.cart_page.cart_page_text()

from selenium.webdriver.common.by import By
from behave import given, when, then

@then('verify your cart is empty')
def verify_cart_empty(context):
    Expected_Result = context.driver.find_element(By.CSS_SELECTOR, "div[class*='sc-your-amazon-cart-is-empty']").text
    Actual_Result = "Your Amazon Cart is empty"
    assert Actual_Result == Expected_Result,f"Actual_result does not match Expected_result"
    print("Test passed")
    context.driver.close()
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
import time

CART_ICON = (By.CSS_SELECTOR,"#nav-cart-count-container")
CART_COUNT=(By.ID,"nav-cart-count")


@then('Click on cart icon')
def Click_Cart_Icon(context):
    context.driver.wait.until(EC.presence_of_element_located(CART_ICON))
    context.driver.find_element(*CART_ICON).click()


@then('Verify Cart has {Expected} item')
def CART_Count(context,Expected):
    context.driver.wait.until(EC.presence_of_element_located(CART_COUNT))
    Actual = (context.driver.find_element(*CART_COUNT).text)
    print(Actual)
    assert int(Actual) == int(Expected) , f"{Actual} does not match {Expected}"
    print("Test Passed")


from selenium.webdriver.common.by import By
from behave import given, when, then
import time
from selenium.webdriver.support import expected_conditions as EC


FIRST_PRODUCT_LINK = (By.CSS_SELECTOR,".a-size-mini a span")
ADD_TO_CART_BUTTON = (By.ID,"add-to-cart-button")
PROTECTION_PLAN = (By.CSS_SELECTOR,"#attachSiNoCoverage")

@then('Click on First product')
def Click_First_product(context):
    context.driver.find_element(*FIRST_PRODUCT_LINK).click()

@then('Click on Add to cart Button')
def Add_Product_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()

@then('Click on No thanks Button')
def Click_NO_Thanks(context):
    context.driver.find_element(*PROTECTION_PLAN).click()

    #context.driver.wait.until(EC.element_to_be_selected(PROTECTION_PLAN))


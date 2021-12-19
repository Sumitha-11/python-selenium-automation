from selenium.webdriver.common.by import By
from behave import given, when, then
import time
from selenium.webdriver.support import expected_conditions as EC


FIRST_PRODUCT_LINK = (By.CSS_SELECTOR,".a-size-mini a span")
ADD_TO_CART_BUTTON = (By.ID,"add-to-cart-button")
PROTECTION_PLAN = (By.CSS_SELECTOR,"#attachSiNoCoverage")
COLOR_SELECTED = (By.CSS_SELECTOR,"img[class='imgSwatch']")
COLOR_NAME =(By.CSS_SELECTOR,"#variation_color_name span[class='selection']")


@then('Click on First product')
def Click_First_product(context):
    context.driver.find_element(*FIRST_PRODUCT_LINK).click()


@then('Click on Add to cart Button')
def Add_Product_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BUTTON))
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@then('Click on No thanks Button')
def Click_NO_Thanks(context):
    context.driver.wait.until(EC.element_to_be_clickable(PROTECTION_PLAN))
    context.driver.find_element(*PROTECTION_PLAN).click()


@given('Open Amazon Product {product_id} Page')
def open_Amazon_product(context,product_id):
    context.driver.get(f"https://www.amazon.com/gp/product/{product_id}")


@then('Verify user can click through {Expected_colors} of the product')
def Click_on_color(context,Expected_colors):
    Actual_color=[]
    product_color = context.driver.find_elements(*COLOR_SELECTED)
    for product in product_color[:5]:
        product.click()
        Actual_color += [context.driver.find_element(*COLOR_NAME).text]
    print(Actual_color)
    Actual_color=str(Actual_color)

    assert (Actual_color) == (Expected_colors),f"{Actual_color} does not match {Expected_colors}"
    print("Test Passed")






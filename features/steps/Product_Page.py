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
def click_first_product(context):
    context.app.product_detail_page.click_first_product()


@then('Click on Add to cart Button')
def add_product_cart(context):
    context.app.product_detail_page.add_product_to_cart()


@then('Click on No thanks Button')
def click_no_thanks(context):
    context.app.product_detail_page.click_no_thanks()


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


@given('Open Amazon Product {product_id} Page')
def open_Amazon_product(context,product_id):
    context.app.main_page.open_product_page(product_id)


@when('Hover over new arrivals')
def hover_new_arrivals(context):
    context.app.product_detail_page.hover_new_arrivals()


@then('Verify {5} category are present')
def veify_different_category(context,expected_count):
    context.app.product_detail_page.verify_category(expected_count)


@then('Verify women category is present')
def verify_women_categoty(context):
    context.app.product_detail_page.verify_women_category()






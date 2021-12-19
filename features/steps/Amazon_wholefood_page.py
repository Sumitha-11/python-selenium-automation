from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

REGULAR_WORD = (By.XPATH,"//span[@class='a-size-small a-color-tertiary wfm-sales-item-card__regular-price']")
PRODUCT_NAME= (By.XPATH,"//ul[@class='s-result-list s-col-2 wfm-desktop-list-font-unset s-height-equalized']//span[contains(@class,'wfm-sales-item-card__product-name')]")

@given('Open Amazon Wholefood page')
def Open_wholefood_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify Regular word in all product')
def Verify_Regular_word(context):
    word = context.driver.find_element(*REGULAR_WORD).text
    if "Regular" in word:
        context.product_name = context.driver.find_elements(*PRODUCT_NAME)


@then('Print the name of the product')
def print_name(context):
    for name in context.product_name:
        print (name.text)

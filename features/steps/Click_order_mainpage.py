from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@given('Open Amazon customer page')
def open_amazonpage(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when('Input cancel order into search field')
def search_cancel_orders(context):
    context.driver.find_element(By.ID, "helpsearch").send_keys("cancel order")

@then('Click Enter button')
def Click_search_icon(context):
    context.driver.find_element(By.ID,"helpsearch").send_keys(Keys.ENTER)
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open Amazon page')
def open_Amazon(context):
    context.driver.get("https://www.amazon.com")
@when('Click on Orders and Returns')
def Click_orders(context, ):
    context.driver.find_element(By.XPATH,"//a[@href='/gp/css/order-history?ref_=nav_orders_first']").click()
@then('Sign-In page should appear.')
def Sigin_page(context):
    assert "Sign-In" == context.driver.find_element(By.XPATH,"//h1[@class='a-spacing-small']").text,f"Actual result not matched with expected result"



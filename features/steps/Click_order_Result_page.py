from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

@then('Check cancel and orders is shown')
def cancel_orders_shown(context):
    Expected_result = context.driver.find_element(By.XPATH, "//h1[text()='Cancel Items or Orders']").text
    Actual_result = "Cancel Items or Orders"
    assert Actual_result == Expected_result,f"Actual result doesnt match Expected result"
    print("Test Passed.")
    context.driver.close()
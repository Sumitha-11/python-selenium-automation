from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Sign-In page should appear.')
def Sigin_Page(context):
    Expected_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text
    Actual_result = "Sign-In"
    assert Expected_result == Actual_result
    print("Test Passed")
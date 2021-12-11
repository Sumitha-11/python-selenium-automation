from selenium.webdriver.common.by import By
from behave import given, when, then

Links = (By.XPATH,"//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']//div/a")

@then('verify {expected_count} links are present')
def verify_links_present(context,expected_count):
    Actual_count = len(context.driver.find_elements(*Links))
    assert Actual_count == int(expected_count),f"{Actual_count} doesnot match with {expected_count}"


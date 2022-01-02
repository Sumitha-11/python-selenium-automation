from selenium.webdriver.common.by import By
from behave import given, when, then


@then('{expected_text} page should appear.')
def sigin_page(context,expected_text):
    context.app.sign_in_page.verify_sign_in(expected_text)
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR,"a[href='https://www.amazon.com/privacy']")
TITLE_PAGE = (By.CSS_SELECTOR,".help-content h1")


@given('Open Amazon T&C page')
def open_Amazon_TC_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when('Store original windows')
def Store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.driver.window_handles)
    print(context.original_window)


@when('Click on Amazon Privacy Notice link')
def Click_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE_LINK).click()


@when('Switch to the newly opened window')
def Switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.windows=(context.driver.window_handles)
    context.driver.switch_to.window(context.windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def Verify_Amazon_privacy_page(context):
    Expected_title = context.driver.find_element(*TITLE_PAGE).text
    print(Expected_title)
    assert "Amazon.com Privacy Notice" == Expected_title ,f"Expected title does not match the original title"


@then('User can close new window and switch back to original')
def close_window_backto_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.windows[0])

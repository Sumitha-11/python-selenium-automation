from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

LINKS = (By.XPATH,"//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']//div/a")
TITLE = (By.CSS_SELECTOR,"#zg_banner_text")

@then('verify {expected_count} links are present')
def verify_links_present(context,expected_count):
    Actual_count = len(context.driver.find_elements(*LINKS))
    assert Actual_count == int(expected_count),f"{Actual_count} doesnot match with {expected_count}"


# @then('Click on sub-links and verify newpage is opened')
# def click_sublinks(context):
#     sub_link = (context.driver.find_elements(*LINKS))
#     lists = []
#     for link in sub_link:
#         print(link.get_attribute('href'))
#         lists.append(link.get_attribute('href'))
#
#     for i in range(len(lists)):
#         Actual_text = ['Best Sellers','New Releases','Movers & Shakers','Most Wished For','Gift Ideas']
#         context.driver.get(lists[i])
#         Expected_text = context.driver.find_element(*TITLE).text
#         print(Expected_text)
#         assert Actual_text[i] in Expected_text,f"Actual doesnot match Expected"



@then('Click on sub-links')
def click_sublinks(context):
    sub_link = (context.driver.find_elements(*LINKS))
    context.lists = []
    for link in sub_link:
        print(link.get_attribute('href'))
        context.lists.append(link.get_attribute('href'))


@then('Verify newpage is opened')
def newpage_opens(context):
    for i in range(len(context.lists)):
        Actual_text = ['Best Sellers','New Releases','Movers & Shakers','Most Wished For','Gift Ideas']
        context.driver.get(context.lists[i])
        Expected_text = context.driver.find_element(*TITLE).text
        print(Expected_text)
        assert Actual_text[i] in Expected_text,f"Actual doesnot match Expected"



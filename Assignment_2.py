from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome(executable_path='C:\\Users\\USER\\Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.amazon.com/gp/help/customer/display.html")
search=driver.find_element(By.ID,"helpsearch")
search.send_keys("cancel orders")
search.send_keys(Keys.RETURN)
Expected_result = driver.find_element(By.XPATH,"//h1[text()='Cancel Items or Orders']").text
Actual_result = "Cancel Items or Orders"
assert Actual_result == Expected_result
print("Test Passed.")
driver.close()
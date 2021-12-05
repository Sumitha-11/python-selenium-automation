import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions

driver= webdriver.Chrome(executable_path='C:\\Users\\USER\\Automation\\python-selenium-automation\\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.amazon.com")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox").send_keys("ipad")
driver.find_element(By.ID,"nav-search-submit-button").click()
driver.find_element(By.CSS_SELECTOR,".a-size-mini a span").click()
driver.find_element(By.ID,"add-to-cart-button").click()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"#attachSiNoCoverage").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#nav-cart-count-container").click()
Expected = (driver.find_element(By.XPATH,"//a[contains(@href,'/gp/product/B09G9FPHY6')]/span/span").text)
Actual = '2021 Apple 10.2-inch iPad (Wi-Fi, 64GB) - Space Gray'
print(Expected)
assert Actual == Expected
print("Test Passed")
driver.close()
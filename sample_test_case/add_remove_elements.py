from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('http://the-internet.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Remove Elements').click()
time.sleep(2)

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_button.click()
time.sleep(2)

remove_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
remove_button.click()
time.sleep(2)

driver.quit()
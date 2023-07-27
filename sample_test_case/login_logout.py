# Ini merupakan test case login logout menggunakan credential yang valid (positive test)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# inisialisasi webdriver
driver = webdriver.Chrome()

# masuk ke url untuk login
driver.get('http://the-internet.herokuapp.com/login')

# mencari element untuk input username
username_input = driver.find_element(By.NAME, 'username')

# input username
username_input.send_keys('tomsmith')

# mencari element untuk input password
password_input = driver.find_element(By.NAME, 'password')

# input password
password_input.send_keys('SuperSecretPassword!')

time.sleep(2)

# mencari element untuk button login
login_button = driver.find_element(By.CLASS_NAME, "radius")
login_button.click()
time.sleep(2)

# mencari element untuk button logout
logout_button = driver.find_element(By.CLASS_NAME, "button.secondary.radius")
logout_button.click()

time.sleep(2)

driver.quit()
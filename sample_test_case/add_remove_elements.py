from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# inisialisasi webdriver, disini saya menggunakan chrome
driver = webdriver.Chrome()

# memaksimalkan ukuran layar
driver.maximize_window()

# masuk ke situs the internet herokuapp
driver.get('http://the-internet.herokuapp.com/')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Remove Elements').click()
time.sleep(2)

# mencari element button add element dan mengkliknya
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
add_button.click()
time.sleep(2)

# mencari element button delete dan mengkliknya
remove_button = driver.find_element(By.XPATH, "//button[text()='Delete']")
remove_button.click()
time.sleep(2)

driver.quit()
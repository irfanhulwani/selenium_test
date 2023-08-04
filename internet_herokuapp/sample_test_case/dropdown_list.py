from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# inisialisasi web driver, disini saya menggunakan chrome
driver = webdriver.Chrome()

# masuk ke halaman web dan langung masuk ke halaman dropdown
driver.get('http://the-internet.herokuapp.com/dropdown')

# mencari element dropdown
dropdown = Select(driver.find_element(By.ID, 'dropdown'))

# memilih menu Option 2 dengan metode select by value
dropdown.select_by_value("2")
time.sleep(3)

# memilih menu Option 1 dengan metode select by visible text
dropdown.select_by_visible_text("Option 1")
time.sleep(2)

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Tentukan jalur ke ChromeDriver
chromedriver_path = "C:/path/to/chromedriver.exe"

# Inisialisasi service Chrome
service = Service(executable_path=chromedriver_path)

# Buat opsi Chrome
options = Options()
# Tambahkan opsi tambahan jika diperlukan
options.add_argument("--start-maximized")  # Contoh: maksimalkan jendela browser saat dibuka

# Inisialisasi WebDriver Chrome dengan service dan opsi
driver = webdriver.Chrome(service=service, options=options)

# Buka halaman dengan formulir checkbox
url = "http://the-internet.herokuapp.com/checkboxes"
driver.get(url)
time.sleep(3)

# Cari elemen-elemen checkbox menggunakan XPath
checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")

# Klik checkbox pertama
checkbox1.click()
time.sleep(1)
checkbox1.click()
time.sleep(1)

# Klik checkbox kedua
checkbox2.click()
time.sleep(1)
checkbox2.click()
time.sleep(1)

# Tutup browser saat selesai
driver.quit()

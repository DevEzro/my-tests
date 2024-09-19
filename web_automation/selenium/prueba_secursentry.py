from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from colorama import init, Fore

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("http://localhost/")

web_element_email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]#pass')
web_element_email.send_keys("admin@secursentry.com")

web_element_password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]#pass')
web_element_password.send_keys("3O9j8c%#Sy4hb8&Y")

login_button = driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Sign in')]]")
login_button.click()

# region ALTERNATIVA
# login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-custom.btn-login')
# login_button.click()
# endregion

# Espera unos segundos
time.sleep(2);

# Control de cierre
input("Presiona Enter para cerrar la sesión de Selenium y cerrar el navegador...")

# Se cierra al pulsar Enter
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, random
from colorama import init, Fore

def espera():
	time.sleep(2)

driver = webdriver.Firefox()

# driver.maximize_window()

driver.get("http://localhost/")

print(f"{Fore.BLUE}[-]{Fore.RESET} Introduciendo credenciales...")
web_element_email = driver.find_element(By.CSS_SELECTOR, 'input[type="email"]#pass')
web_element_email.send_keys("admin@secursentry.com")

web_element_password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]#pass')
web_element_password.send_keys("3O9j8c%#Sy4hb8&Y")
print(f"{Fore.GREEN}[+]{Fore.RESET} Credenciales introducidas")

espera()

print(f"{Fore.BLUE}[-]{Fore.RESET} Log in...")
login_button = driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Sign in')]]")
login_button.click()
print(f"{Fore.GREEN}[+]{Fore.RESET} Log in realizado con éxito")

espera()

print(f"{Fore.BLUE}[-]{Fore.RESET} Accediendo al apartado Usuarios, equipos y roles...")
users_teams_roles = driver.find_element(By.XPATH, ".//span[contains(text(), 'Usuarios, equipos y roles')]")
users_teams_roles.click()
print(f"{Fore.GREEN}[+]{Fore.RESET} Acceso con éxito")

espera()

print(f"{Fore.BLUE}[-]{Fore.RESET} Introduciendo credenciales para nuevo usuario...")
new_user_button = driver.find_element(By.XPATH, ".//span[contains(text(), 'Nuevo Usuario')]")
new_user_button.click()

numero = random.randint(0, 1000)
input_user_name = driver.find_element(By.XPATH, ".//input[@placeholder='Nombre completo del usuario']")
input_user_name.send_keys(f"hola{numero}")
input_user_email = driver.find_element(By.XPATH, ".//input[@placeholder='Email del usuario']")
input_user_email.send_keys(f"hola{numero}@hola{numero}.com")
print(f"{Fore.GREEN}[+]{Fore.RESET} Credenciales introducidas")

espera()

print(f"{Fore.BLUE}[-]{Fore.RESET} Guardando nuevo usuario...")
create_user_button = driver.find_element(By.XPATH, ".//span[contains(text(), 'Guardar')]")
create_user_button.click()

espera()

print(f"{Fore.GREEN}[+]{Fore.RESET} Usuario creado con éxito")

input("Presiona Enter para cerrar la sesión de Selenium y cerrar el navegador...")

driver.quit()
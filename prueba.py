#############################################################################
# PRUEBA CON SELENIUM Y WEBDRIVER QUE ACCEDE A UN ENLACE DE UDEMY AL BUSCAR #
# SOBRE SELENIUM                                                            #
#############################################################################

#Importación de selenium y sus componentes y time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Para colores
from colorama import init, Fore
#-------------------------------------------------

#-------------------------------------------------
#Inicializa Chrome
driver = webdriver.Chrome()

#Abre una página web
driver.get("https://www.google.com/")

#Acepta las cookies
web_element = driver.find_element(By.ID, 'L2AGLb')
web_element.send_keys(Keys.ENTER)

#Busca Selenium WebDriver
web_element = driver.find_element(By.NAME, 'q')
web_element.send_keys("Selenium WebDriver" + Keys.ENTER)

time.sleep(2);
#-------------------------------------------------
resultados = driver.find_elements(By.CSS_SELECTOR, 'h3')
if resultados:
        # Imprime los títulos de los resultados para verificar
        for i, resultado in enumerate(resultados):
            print(f"{Fore.GREEN}[+]{Fore.RESET}Resultado {i}: {resultado.text}")

        # Selecciona el primer resultado (puedes cambiar el índice para seleccionar otro resultado)
        first_result = resultados[13] #Se indica la posicion en el array del enlace deseado
        # Haz clic en el primer resultado
        first_result.click()
else:
    print(f"{Fore.RED}[-]{Fore.RESET}No se encontraron resultados de búsqueda.")
#-------------------------------------------------
#Control de cierre
input("Presiona Enter para cerrar la sesión de Selenium y cerrar Chrome...")

#Se cierra al pulsar Enter
driver.quit()
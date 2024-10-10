from colorama import Fore
from typing import List

so:str
source:List[str]

def prueba_agente(so, source):
    if so=="windows" or so=="linux" or so=="macos":
        print(f'''
        Esto es una prueba inicial
        de agente que muestra los valores
        del sistema operativo ({Fore.CYAN}{so}{Fore.RESET}) y las fuentes ({Fore.CYAN}{source}{Fore.RESET})
        que se pasan al método
        ''')

prueba_agente("windows", ["fuente_1, fuente2"])
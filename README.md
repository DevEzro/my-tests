# TEST REPOSITORY
## RAMAS
### - GITHUB_ACTIONS
- La ruta para ejecutar los jobs del fichero yml usando GitHub Actions
> root/.github/workflows/helloworld.yml
- Contenido del archivo 'helloworld.yml'
```
on: #Especifica el evento que hará funcionar el flujo de trabajo
  push: #El flujo de trabajo se lanzará cuando se haga un push en el repo
    branches: #Define en que rama se lanzará el flujo de trabajo
      - main #Em este caso, la rama main

jobs: #Define los jobs que se ejecutarán
  print_hello: #Nombre del primer job
    runs-on: ubuntu-latest #Especifica la MV en la que se ejecutará la tarea
    steps: #Define los pasos que el job ejecutará
      - run: echo "Hello world!" #El trabajo en cuestión: muestra por pantalla "Hola Mundo!"

  #Ejemplo de otro job similar al anterior
  print_name:
    runs-on: ubuntu-latest
    steps:
      - run: echo "David"
      - run: echo "Cerrando"
```

### - PYTEST
- Una clase main.py y una clase test_main.py con operaciones
- La clase test_main.py prueba algunos enteros como parametros para la prueba, doinde uno de ellos provocará un error durante la el prueba
- Sirve como prueba para entender como funcoina pytest

### - PYTEST_API
- Archivo de Python con instrucciones para probar la API de la URL todo.pixegami.io
- Pytest integrado para ejecutar pruebas
- Explicado línea por línea

### - PYTEST_FASTAPI
- Lo mismo que en PYTEST_API pero usando FastAPI

### - PYTEST_FASTAPI_CRUD
- Lo mismo que en PYTEST_FASTAPI pero implementando operaciones CRUD para usuarios

### - SELENIUM
- Un fichero Python con un ejemplo sencillo para entender como funciona Selenium Web Driver

### - TESTCAFE
- Un fichero JS con un ejemplo sencillo para entender como funciona la automatización web con TestCafé

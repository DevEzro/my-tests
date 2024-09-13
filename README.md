# USO DE TESTCAFE
## INSTALACIÓN
- Instalar node.js
- Abrir node y comprobar versiones:
`node -v`
`npm -v`

![image](https://github.com/user-attachments/assets/7958d34f-f98e-49c5-bb59-129709889a75)

## SETUP

- Inicializar testcafe en la carpeta `npm init` -> Crea package.json
- Instalar TestCafé `npm install testcafe --save-dev` -> Crea la carpeta de modulos 'node_modules'
- Crear la ruta `tests/fichero.js` para las pruebas

![image](https://github.com/user-attachments/assets/f628d18c-2909-440e-b9b0-11f3d1fe1424)

- Ejecutar pruebas `npx testcafe edge </ruta/al/fichero.js>`

### SE PUEDE USAR CUALQUIER NAVEGADOR. USO EDGE YA QUE CON CHROME ME DA ERROR

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
- Un fichero Python con un ejemplo sencillo para entender como funciona la automatización web con Selenium Web Driver

### - TESTCAFE
- Un fichero JS con un ejemplo sencillo para entender como funciona la automatización web con TestCafé
# TEST REPOSITORY
## RAMAS
### - GITHUB_ACTIONS
- La ruta para ejecutar los jobs del fichero yml usando GitHub Actions
> root/.github/workflows/helloworld.yml
- Contenido del archivo 'helloworld.yml'
```
on: #Specifies the event that will trigger the workflow
  push: #The workflow will be triggered when a push is made to the repo
    branches: #Defines on which branches the workflow will be triggered
      - main #In this case, the main branch

jobs: #Defines the jobs that will be executed
  print_hello: #Name of the first job
    runs-on: ubuntu-latest #Specifies the VM on which the task will run
    steps: #Defines the steps the job will execute
      - run: echo "Hello world!" #The specific job: display "Hello world!" on the screen

  #Example of another job similar to the previous one
  print_name:
    runs-on: ubuntu-latest
    steps:
      - run: echo "David"
      - run: echo "Closing"
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

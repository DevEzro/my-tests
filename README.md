# REPOSITORIO DE PRUEBAS
## RAMAS
### - GITHUB_ACTIONS
- La ruta para que se realicen los jobs del yml por GitHub Actions
> raiz/.github/workflows/helloworld.yml

- Contenido del fichero 'helloworld.yml'
```yml
 on: #Especifica el evento que activará el workflow
  push: #El workflow se activará cuando se haga un push al repo
    branches: #Define en que ramas se activará el workflow
      - main #En este caso es la rama main

jobs: #Definde los trabajos que se van a realizar
  print_hello: #Nombre del primer trabajo
    runs-on: ubuntu-latest #Indica en que MV se va a ejecutar la tarea
    steps: #Define los pasos que va a realizar el trabajo
      - run: echo "Hello world!" #El trabajo en cuestión: mostrar por pantalla "Hello world!"

  #Ejemplo de otro trabajo similar al anterior
  print_nombre:
    runs-on: ubuntu-latest
    steps:
      - run: echo "David"
      - run: echo "Cierre"
```

### - PYTEST_API
- Fichero de python con instrucciones para probar la api de la URL todo.pixegami.io
- Pytest integrado para realizar pruebas
- Explicado línea por línea

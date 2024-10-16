# SET UP 
- Se accede al proyecto que queramos e inicializamos Nightwatch: `npm init nightwatch`
- Opciones a seleccionar:
  - "El directorio actual no es un nodo y ya existen ficheros" `>Yes`
  - "Selecciona el tipo de setup" `>End-to-End testing`
  - "Selecciona el lenguaje y el ejecutable de tests" `>JavaScript/default`
  - "Selecciona el navegador" `>Firefox`
  - "Introduce la carpeta de los tests (tests)" `Pulsamos Enter`
  - "Introduce la url de los proyectos (localhost)" `Pulsamos Enter`
  - "Selecciona donde quieres que se ejecuten los tests" `>On localhost`
  - "Permitir colleccionar métricas anonimas (Y/n)" `n`
  - "Setup de tests para dispositivos móviles" `>No, saltar por ahora`

# EJECUCCIÓN
`npx nightwatch <ruta/a/fichero.js>`

# RECOMENDACIÓN
> Para que la ejecucción no falle, ejecutar el comando desde fuera de la carpeta tests  

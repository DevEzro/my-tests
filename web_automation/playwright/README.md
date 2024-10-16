# SET UP
- `npx playwright install`
- En la ruta del proyecto: `npm init playwright`
- "Se necesitan instalar los siguientes paquetes (y)": `y`
- "Quieres usar TypeScript o JavaScript?" `>JavaScript` 
> Nota: libre elección de lenguaje. Esto es solo un ejemplo

- "Donde guardaras los tests end-to-end?" > `tests` por defecto
- "Añadir flujo de trabajo de GitHub Actiions (y/N)" `N`
> Nota: libre elección de lenguaje. Esto es solo un ejemplo

- "Instalar navegadores de Playwright (se pueden instalar manualmente con `npx playwright install`) (Y/n)" `n`

> En este punto estará inicializando el proyecto

> Nota: nombrar los ficheros de las pruebas como nombre.spec.js. Será util para la ejecucción individual de ficheros; sin el `spec`dará error.
```
PS C:\Users\David\Documents\Dev\Mis Pruebas\my-tests\web_automation\playwright\tests> npx playwright test login.js
Error: No tests found.
Make sure that arguments are regular expressions matching test files.
You may need to escape symbols like "$" or "*" and quote the arguments.
----------------------------------------------------------
PS C:\Users\David\Documents\Dev\Mis Pruebas\my-tests\web_automation\playwright\tests> npx playwright test .\login.spec.js

Running 1 test using 1 worker

  ok 1 login.spec.js:3:1 › Login Test (1.2s)

  1 passed (2.1s)
```

# EJECUCCIÓN
- Ejecuta todas las pruebas dentro del directorio pruebas (siempre que estemos en él): `npx playwright test`
- Ejecuta un fichero individualmente: `npx playwright test .\login.spec.js`
- Para visualizar los pasos de playwright sobre el navegador, además de añadir tiempos de espera (>ver ejemplo login.spec.js): `npx playwright test login.spec.js --headed`

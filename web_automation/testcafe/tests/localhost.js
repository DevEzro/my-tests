// Para que no saque ningún mensaje de error 
process.noDeprecation = true;

// Imports
import { Selector } from 'testcafe';

// Variables de elementos inicializadas
const emailInput = Selector('input[type="email"]#pass');
const passwordInput = Selector('input[type="password"]#pass');
const loginButton = Selector('button[type="button"]');

// Info. de la prueba (nombre y URL)
fixture `Pack de pruebas`
    .page `http://localhost/`
    .skipJsErrors();

// Tests a realizar
test('Login Test', async t => {

    // Acciones (maximiza, introduce credenciales y login)
    // await t.maximizeWindow();
    console.log("[-] Introduciendo credenciales...")
    await t.typeText(emailInput, 'admin@secursentry.com');
    await t.typeText(passwordInput, '3O9j8c%#Sy4hb8&Y');
    await t.click(loginButton);

    // Espera para cargar la página
    await t.wait(2000);
    console.log("[+] Log in realizado con éxito.")
});
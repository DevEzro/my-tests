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
    .page `http://localhost/`;

// Tests a realizar
test('Login Test', async t => {

    // Acciones (maximiza, introduce credenciales y login)
    await t
        .maximizeWindow()
        .typeText(emailInput, 'admin@secursentry.com')
        .typeText(passwordInput, '3O9j8c%#Sy4hb8&Y')
        .click(loginButton);

    // Espera para cargar la página
    await t.wait(2000);
});
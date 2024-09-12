// Define el objeto Selector para poder obtener los elementos HTML
const {Selector} = require("testcafe");

// Define un conjunto de pruebas llamada  `Login Suite` para la página saucedemo.com
fixture `Login Suite`.page("https://www.saucedemo.com/v1/");

// Define con 'test' una de las pruebas a ejecutar con el nombre `Valid Login`
// - async(t): indica que la función es asíncrona -> permite esperar a que se completen todas las tareas
// - t: objeto de prueba que proporciona las API de TestCafé para realizar las acciones del usuario (escribir, hacer clic, etc)
test('Valid Login', async (t)=>{
    // await t permite la ejecucción de las tareas de manera secuencial
    await t
    // typeText es una función que permite escribir en el elemento ID llamado '#user-name' el text 'standard_user' (igual para password)
    .typeText('#user-name', 'standard_user')
    .typeText('#password', 'secret_sauce')
    // Simula un clic en el botón de login
    .click("#login-button")
    // Selecciona el elemento con una clase '.product_label' y comprueba que el texto 'Products' coincida
    .expect(Selector(".product_label").innerText)
        .eql('Products');
})
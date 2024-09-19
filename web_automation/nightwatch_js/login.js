module.exports = {
    // Nombre del test
    'Login Test': function (browser) {
    browser
        // URL para los test
        .url('https://www.saucedemo.com/v1/')
        // Espera al cuerpo de la página
        .waitForElementVisible('body', 1000)
        // Comprueba el titulo de la página
        .assert.titleContains('Swag Labs')
        // Rellena campos de login
        .setValue('input[name="user-name"]', 'standard_user')
        .setValue('input[name="password"]', 'secret_sauce')
        .click('input[id="login-button"]')

        .waitForElementVisible('body', 1000)
        
        // Comprueba la palabra en el item indicado
        .assert.textContains('div.product_label', 'Products')
        // Termina la prueba
        .end();
    },
};
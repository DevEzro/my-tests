const { test, expect } = require('@playwright/test');

test('Login Test', async ({ page }) => {
    // Accede a la URL
    await page.goto('https://www.saucedemo.com/v1/');

    // Esperar a que el cuerpo de la página esté visible
    await page.waitForSelector('body');
    
    // Comprueba el título de la página 'Swag Labs'
    await expect(page).toHaveTitle(/Swag Labs/);

    // Tiempo de espera para poder ver los pasos en el navegador
    await page.waitForTimeout(1000)

    // Rellenar los campos de usuario y contraseña
    await page.fill('input[name="user-name"]', 'standard_user');
    await page.fill('input[name="password"]', 'secret_sauce');

    // Hace clic en el botón de inicio de sesión
    await page.click('input[id="login-button"]');

    // Tiempo de espera para poder ver los pasos en el navegador
    await page.waitForTimeout(1000)

    // Esperar a que el cuerpo de la página se cargue
    await page.waitForSelector('body');

    // Verificar que el texto "Products" está presente en la página
    await expect(page.locator('div.product_label')).toHaveText('Products');

    // Tiempo de espera para poder ver los pasos en el navegador
    await page.waitForTimeout(1000)
});
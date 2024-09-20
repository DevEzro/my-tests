const { test, expect } = require('@playwright/test');

test('Login Test', async ({ page }) => {
    // Navegar a la URL
    await page.goto('https://www.saucedemo.com/v1/');

    // Esperar a que el cuerpo de la página esté visible
    await page.waitForSelector('body');
    
    // Verificar el título de la página
    await expect(page).toHaveTitle(/Swag Labs/);

    await page.waitForTimeout(1000)

    // Rellenar los campos de usuario y contraseña
    await page.fill('input[name="user-name"]', 'standard_user');
    await page.fill('input[name="password"]', 'secret_sauce');

    // Hacer clic en el botón de inicio de sesión
    await page.click('input[id="login-button"]');

    await page.waitForTimeout(1000)

    // Esperar a que el cuerpo de la página se cargue nuevamente tras el login
    await page.waitForSelector('body');

    // Verificar que el texto "Products" está presente en la página
    await expect(page.locator('div.product_label')).toHaveText('Products');
    await page.waitForTimeout(1000)
});
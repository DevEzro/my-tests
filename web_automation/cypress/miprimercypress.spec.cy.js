// Título del test
describe('Mi primer test con Cypress', () => {
  beforeEach(() => {
      // Página a la que accederá
      cy.visit('https://saucedemo.com/v1');
  });

  // Nombre de la prueba
  it('debe tener un título correcto', () => {
      // Comprueba que la página tiene el título indicado
      cy.title().should('include', 'Swag Labs');
  });
});

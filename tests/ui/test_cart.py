from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# El flujo es: abrir un navegador nuevo con el fixture driver, iniciar sesión, 
# agregar la mochila y comprobar que el contador muestre "1". 
# La prueba inicia sesión por su cuenta para no depender de que otra prueba haya corrido antes. 
# SauceDemo usa selectores data-test para los controles de productos.
def test_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    assert inventory_page.get_cart_count() == "1"
    
    # línea de comando para ejecutar el test
    # .\.venv\Scripts\python.exe -m pytest tests\ui\test_cart.py
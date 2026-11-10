from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# El test empieza desde cero: solicita un navegador nuevo, inicia sesión, agrega la mochila, 
# abre el carrito y obtiene los nombres de los productos. La última línea comprueba que 
# "Sauce Labs Backpack" esté dentro de esa lista.
def test_backpack_is_displayed_in_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    cart_page = CartPage(driver)
    cart_page.open_cart()
    product_names = cart_page.get_product_names()

    assert "Sauce Labs Backpack" in product_names
    
    # línes de comando para ejecutar el test
    # .\.venv\Scripts\python.exe -m pytest tests\ui\test_cart_contents.py
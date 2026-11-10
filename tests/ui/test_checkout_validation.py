from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# El recorrido completo es: login → agregar mochila → abrir carrito → checkout. 
# En fill_customer_info("", "Brizuela", "1900"), el primer argumento está vacío; 
# por eso esperamos que el sitio informe que falta el nombre. La última línea verifica ese resultado.
def test_checkout_requires_first_name(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("", "Brizuela", "1900")
    checkout_page.continue_to_overview()

    error_message = checkout_page.get_error_message()
    assert "First Name is required" in error_message
    
    
    # línea de comand0o para ejecutar el test
    # .\.venv\Scripts\python.exe -m pytest tests\ui\test_checkout_validation.py
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger(__name__)

# Este caso usa cada objeto de página según avanza el flujo: login, productos, carrito, formulario, 
# resumen y confirmación. Las dos comprobaciones importantes son que la mochila figure en el resumen 
# y que, al finalizar, aparezca el mensaje de compra exitosa.
def test_complete_purchase(driver):
    logger.info("Inicio del flujo de compra")

    login_page = LoginPage(driver)
    logger.info("Abriendo la página de login")
    login_page.open()

    logger.info("Ingresando con el usuario de prueba")
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    logger.info("Agregando la mochila al carrito")
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    cart_page = CartPage(driver)
    logger.info("Abriendo el carrito")
    cart_page.open_cart()

    logger.info("Avanzando al checkout")
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    logger.info("Completando los datos del checkout")
    checkout_page.fill_customer_info("Carlos", "Brizuela", "1900")
    checkout_page.continue_to_overview()

    overview_page = CheckoutOverviewPage(driver)
    logger.info("Comprobando que la mochila aparezca en el resumen")
    assert "Sauce Labs Backpack" in overview_page.get_product_names()

    logger.info("Finalizando el pedido")
    overview_page.finish_order()

    complete_page = CheckoutCompletePage(driver)
    confirmation_message = complete_page.get_confirmation_message()
    logger.info("Mensaje de confirmación: %s", confirmation_message)

    assert confirmation_message == "Thank you for your order!"
    
    # línea de comando para ejecutar el test
    # .\.venv\Scripts\python.exe -m pytest tests\ui\test_checkout_success.py
    # Get-Content .\logs\automation.log -Encoding utf8
    
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:
    # CART_BADGE guarda el selector que permite encontrar el contador del carrito.
    CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]') 

    # __init__(self, driver) recibe el navegador y lo guarda en self.driver
    def __init__(self, driver):
        self.driver = driver

    # add_product_to_cart(product_id) busca y presiona el botón del producto indicado. 
    # Por ejemplo, al pasar "sauce-labs-backpack", la f inserta ese texto en el selector y 
    # Selenium busca [data-test="add-to-cart-sauce-labs-backpack"].
    def add_product_to_cart(self, product_id):
        button_locator = (
        By.CSS_SELECTOR,
        f'[data-test="add-to-cart-{product_id}"]'
        )

        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(button_locator)
        ).click()

    # get_cart_count() encuentra el contador y devuelve el texto que contiene, por ejemplo "1"
    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
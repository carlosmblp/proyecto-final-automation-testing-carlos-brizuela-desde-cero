from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    
    # CART_ICON, PRODUCT_NAMES y CHECKOUT_BUTTON guardan cómo encontrar esos elementos.
    CART_ICON = (By.CSS_SELECTOR, ".shopping_cart_link")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    # open_cart() hace clic en el ícono del carrito.
    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.CART_ICON)
        ).click()

        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.CHECKOUT_BUTTON)
        )

    # get_product_names() busca todos los nombres de productos (find_elements, en plural), 
    # los guarda en una lista y la devuelve. Si hay una mochila, 
    # la lista contendrá "Sauce Labs Backpack".
    def get_product_names(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        names = []

        for element in product_elements:
            names.append(element.text)

        return names

    # click_checkout() presiona el botón que inicia el checkout; lo usaremos más adelante.
    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
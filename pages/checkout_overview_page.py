# Esta clase representa la pantalla donde se revisan los productos antes de terminar la compra

from selenium.webdriver.common.by import By


class CheckoutOverviewPage:
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name") # permite ubicar los productos que aparecen en el resumen.
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    # get_product_names() arma y devuelve una lista con sus nombres. 
    # En la prueba vamos a comprobar que incluya la mochila.
    def get_product_names(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        names = []

        for element in product_elements:
            names.append(element.text)

        return names

    # finish_order() hace clic en Finish para completar la compra.
    def finish_order(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
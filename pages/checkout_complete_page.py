from selenium.webdriver.common.by import By

# Esta clase representa la pantalla que aparece al terminar la compra y lee su mensaje de confirmación:

class CheckoutCompletePage:
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):
        return self.driver.find_element(
            *self.CONFIRMATION_MESSAGE
        ).text
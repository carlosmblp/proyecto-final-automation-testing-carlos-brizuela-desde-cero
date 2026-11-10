from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Claro. CheckoutPage es la clase que representa la pantalla donde se piden los datos de la persona 
# antes de revisar el pedido. Guarda el navegador que recibe y ofrece métodos para llenar el formulario, 
# continuar y leer un error.
class CheckoutPage:
    FIRST_NAME_FIELD = (By.ID, "first-name") # le indica a Selenium: “buscá por id el elemento cuyo id es first-name”.
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    
    # ERROR_MESSAGE se localiza de otra manera: con un selector CSS que busca el 
    # elemento marcado como data-test="error"
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]') 

    def __init__(self, driver):
        self.driver = driver

    def fill_customer_info(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRST_NAME_FIELD)
        ).send_keys(first_name)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LAST_NAME_FIELD)
        ).send_keys(last_name)
        
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.POSTAL_CODE_FIELD)
        ).send_keys(postal_code)
       

    # Busca el botón Continue y hace clic para pasar a la pantalla siguiente del checkout.
    def continue_to_overview(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    # Busca el mensaje de error y devuelve su texto. Una prueba podrá comparar 
    # ese texto con el que esperaba, por ejemplo cuando se intenta continuar con un campo vacío.
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
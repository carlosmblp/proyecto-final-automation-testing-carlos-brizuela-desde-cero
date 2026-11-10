from selenium.webdriver.common.by import By


class LoginPage:
    URL = "https://www.saucedemo.com/"
    
    # By le indica a Selenium cómo localizar elementos. En este caso usamos selectores CSS.


    USERNAME_FIELD = (By.CSS_SELECTOR, '[data-test="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    # __init__ recibe el navegador que prepara el fixture y lo guarda en self.driver.
    # driver es el navegador controlado por Selenium. Con él abrimos páginas, buscamos elementos, 
    # escribimos y hacemos clic.
    # self representa el objeto actual de la clase LoginPage. Permite que sus métodos compartan 
    # información, como el navegador guardado en self.driver.
    def __init__(self, driver):
        self.driver = driver

    # open() navega a la página de SauceDemo.
    def open(self):
        # self.driver.get(...) significa: “usá el navegador que guardé en este objeto para abrir la página”.
        self.driver.get(self.URL)

    # login() escribe el usuario y la contraseña y presiona el botón.
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    # get_error_message() obtiene el mensaje que muestra la página ante un error de acceso.
    def get_error_message(self):
        # *self.USERNAME_FIELD despliega la tupla en sus dos partes: 
        # el tipo de búsqueda (By.CSS_SELECTOR) y el selector.
        return self.driver.find_element(*self.ERROR_MESSAGE).text
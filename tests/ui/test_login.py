import json
from pathlib import Path

import pytest

from pages.login_page import LoginPage

# ubicacion donde estan los datos de prueba
# ¿Cómo encuentra el archivo JSON?
# __file__ identifica el archivo actual: test_login.py.
# .resolve() obtiene su ruta completa en tu computadora.
# .parents[2] sube desde tests/ui/test_login.py hasta la carpeta principal del proyecto.
# /"data"/"ui_users.json" agrega las carpetas y el nombre del archivo de datos.
DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "ui_users.json"
)

# ¿Cómo carga los casos?
# - DATA_FILE.open(...) abre el JSON.
# - json.load(file) convierte su contenido en datos de Python.
# - ["login_cases"] toma la lista que está bajo ese nombre en el Json ui_user.json.
# - Esa lista queda guardada en LOGIN_CASES.
# Allí están los dos casos: uno válido y otro inválido.
with DATA_FILE.open(encoding="utf-8") as file:
    LOGIN_CASES = json.load(file)["login_cases"]

# ¿Por qué se repite la prueba?
# Esto le indica a pytest: ejecutá la función de prueba una vez por cada elemento de LOGIN_CASES. 
# Como hay dos casos, habrá dos ejecuciones. ids les pone los nombres inicio_sesion_valido y 
# credenciales_invalidas para reconocerlas en los resultados.
@pytest.mark.parametrize(
    "login_case",
    LOGIN_CASES,
    ids=[case["id"] for case in LOGIN_CASES],
)

# ¿Qué hace una ejecución?
# La función recibe dos cosas:
# - login_case: los datos del caso actual del JSON.
# - driver: el navegador Chrome que prepara el fixture.
# En una ejecución, por ejemplo, login_case["username"] vale standard_user. 
# En la otra, vale usuario_invalido.
def test_login(login_case, driver):
    login_page = LoginPage(driver) # crea el objeto de la página y le pasa el navegador
    login_page.open() # abre SauceDemo
    login_page.login(login_case["username"], login_case["password"]) # ingresa el usuario y la contraseña del caso actual y presiona el botón.

    # Si el JSON indica que esperamos un acceso exitoso, driver.current_url consulta la 
    # dirección actual del navegador. assert comprueba que esa dirección contenga inventory.html. 
    # Si no lo contiene, la prueba falla. inventory.html es a la página que tiene que ir
    # despues de loguearse exitosamente
    if login_case["expected_result"] == "success":
        assert "inventory.html" in driver.current_url
    else:
        error_message = login_page.get_error_message()
        assert login_case["expected_message"] in error_message
        
        
    
    # para ejecutar el test desde la consola:
    # .\.venv\Scripts\python.exe -m pytest tests\ui\test_login.py
    
    
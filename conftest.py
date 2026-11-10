from base64 import b64encode # convierte la imagen a texto codificado para que pueda incrustarse en el HTML.
from datetime import datetime
from pathlib import Path # construye y maneja rutas a carpetas y archivos
import re # ayuda a limpiar el nombre de la prueba para que sea seguro usarlo como nombre de archivo

import pytest
import pytest_html # permite adjuntar contenido al reporte HTML.
from selenium import webdriver


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
    navegador.maximize_window()

    yield navegador
    
    navegador.quit()

# Un hook es una función que pytest llama en un momento concreto. 
# pytest_runtest_makereport se llama cuando pytest prepara el resultado de una prueba.
# hookwrapper=True permite que esta función espere a que pytest termine de preparar ese resultado
# yield cede el control a pytest y, al reanudarse, get_result() permite consultar 
# el informe de la prueba: si pasó, falló y en qué etapa ocurrió.

# @pytest.hookimpl le indica a pytest: “esta función participa en uno de tus eventos internos”.

# El flujo es así:
# 1. Pytest entra en nuestra función.
# 2. Llega a yield: nuestra función se pausa y le da el turno a pytest.
# 3. Pytest termina de preparar el resultado de la prueba.
# 4. Nuestra función continúa; resultado contiene lo que pytest produjo.
# 5. resultado.get_result() nos permite consultar ese informe y saber, por ejemplo, si la prueba falló.
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    resultado = yield
    reporte = resultado.get_result()
    
    # reporte.when indica en qué etapa ocurrió el resultado:
    # - "setup": pytest prepara la prueba, por ejemplo, solicita el navegador.
    # - "call": se ejecuta el cuerpo de la función de prueba.
    # - "teardown": pytest limpia los recursos al terminar.
    if reporte.when != "call" or not reporte.failed:
        return

    # item.funcargs contiene los valores que pytest le pasó a la prueba, incluidas las fixtures 
    # solicitadas. Si la prueba recibió driver, acá recuperamos ese Chrome
    navegador = getattr(item, "funcargs", {}).get("driver")
    if navegador is None:
        return

    # Preparar la carpeta y el nombre
    # Esto arma la ruta reports/screens/ dentro del proyecto y verifica que exista. Si falta, la crea.
    carpeta_capturas = Path(__file__).resolve().parent / "reports" / "screens"
    carpeta_capturas.mkdir(parents=True, exist_ok=True)

    # fecha_hora genera un sello con año, mes, día, hora, minuto, segundo y fracción de segundo.
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S_%f") 
    # item.name contiene el nombre de la prueba, posiblemente también el identificador de su 
    # caso parametrizado.
    # re.sub(...) reemplaza caracteres que podrían complicar el nombre del archivo por _
    nombre_prueba = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.name)
    # ruta_captura combina la carpeta, la fecha y el nombre, por ejemplo: 
    # reports/screens/20261110_221530_123456_test_complete_purchase.png.
    ruta_captura = carpeta_capturas / f"{fecha_hora}_{nombre_prueba}.png"

    # Guardar y adjuntar la imagen
    extras = getattr(reporte, "extras", [])

    try:
        # get_screenshot_as_png() obtiene la imagen del navegador.
        imagen_png = navegador.get_screenshot_as_png()
        # write_bytes(...) la guarda como archivo .png en reports/screens/.
        ruta_captura.write_bytes(imagen_png)
        # b64encode(...) convierte esa misma imagen en texto para poder incrustarla en el reporte.
        imagen_base64 = b64encode(imagen_png).decode("ascii")
        # pytest_html.extras.png(...) agrega la imagen como contenido extra del reporte. 
        # Como el reporte está configurado como autocontenido, adjuntamos los datos de la imagen 
        # y no solo una ruta externa. pytest-html documenta tanto los extras de imagen como la 
        # propiedad report.extras.
        extras.append(
            pytest_html.extras.png(imagen_base64, name=ruta_captura.name)
        )
    # Si falla la captura
    except Exception as error:
        extras.append(
            pytest_html.extras.text(
                f"No se pudo guardar la captura: {error}",
                name="Error de captura",
            )
        )

    reporte.extras = extras
    
    
    
    # .\.venv\Scripts\python.exe -m pytest tests\ui
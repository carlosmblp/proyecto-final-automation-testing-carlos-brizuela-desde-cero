# Proyecto Final de Automatización QA

Proyecto de automatización de pruebas con **Python**, **pytest**, **Selenium WebDriver** y **Requests**. Incluye pruebas de interfaz web y de API, reporte HTML, registro de logs e integración continua con GitHub Actions.

Se prueban estos servicios:

- **SauceDemo**, para las pruebas de interfaz.
- **JSONPlaceholder**, para las pruebas de API.

Repositorio: [proyecto-final-automation-testing-carlos-brizuela-desde-cero](https://github.com/carlosmblp/proyecto-final-automation-testing-carlos-brizuela-desde-cero)

## Tecnologías utilizadas

- Python 3.14
- pytest
- Selenium WebDriver
- Requests
- pytest-html
- GitHub Actions

## Estructura del proyecto

```text
proyecto-final-automation-testing-carlos-brizuela/
├── .github/
│   └── workflows/
│       └── ci.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── data/
│   ├── api_payloads.json
│   └── ui_users.json
├── logs/                         # Se genera durante la ejecución
├── pages/
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/                      # Contiene los reportes generados
│   └── screens/                  # Capturas generadas ante fallos
├── tests/
│   ├── api/
│   │   └── test_posts.py
│   └── ui/
│       ├── test_cart.py
│       ├── test_cart_contents.py
│       ├── test_checkout_success.py
│       ├── test_checkout_validation.py
│       └── test_login.py
└── utils/
    └── logger.py
```

## Requisitos previos

- Python instalado.
- Google Chrome instalado para las pruebas de interfaz.
- Conexión a Internet para acceder a SauceDemo y JSONPlaceholder.
- Git, si se desea clonar el repositorio.

Selenium Manager se encarga de gestionar el controlador compatible con Chrome.

## Instalación

Desde la carpeta raíz del proyecto, creá un entorno virtual:

```powershell
python -m venv .venv
```

Instalá las dependencias:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Ejecución de las pruebas

Ejecutar todas las pruebas:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Ejecutar solamente las pruebas de interfaz:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/ui
```

Ejecutar solamente las pruebas de API:

```powershell
.\.venv\Scripts\python.exe -m pytest tests/api
```

## Pruebas implementadas

La suite ejecuta **10 casos**: 6 de interfaz y 4 de API.

### Interfaz web

Las pruebas de SauceDemo verifican:

- Inicio de sesión con credenciales válidas e inválidas.
- Agregado de una mochila al carrito.
- Visualización del producto en el carrito.
- Validación del nombre obligatorio en el checkout.
- Finalización de una compra.

Los usuarios de prueba están en `data/ui_users.json`. Las clases de páginas se encuentran en `pages/` y siguen el patrón **Page Object Model (POM)**.

### API

Las pruebas de JSONPlaceholder verifican:

- Consulta de una publicación mediante `GET`.
- Creación de una publicación mediante `POST`.
- Eliminación de una publicación mediante `DELETE`.
- Respuesta 404 para una ruta inexistente.

El contenido enviado en la prueba `POST` está en `data/api_payloads.json`.

> JSONPlaceholder es un servicio de prueba. Las operaciones de creación y eliminación simulan respuestas, pero no guardan los cambios de forma permanente.

## Reportes, capturas y logs

Al ejecutar pytest se genera el reporte HTML en:

```text
reports/reporte.html
```

Si una prueba de interfaz falla, el hook de `conftest.py` guarda una captura en:

```text
reports/screens/
```

Los mensajes de ejecución se registran en:

```text
logs/automation.log
```

### Cómo interpretar el reporte HTML

Abrí `reports/reporte.html` en un navegador. El reporte muestra un resumen y el resultado de cada prueba:

- **Passed**: la prueba terminó correctamente y sus verificaciones se cumplieron.
- **Failed**: alguna verificación falló o se produjo un error. Abrí el detalle de la prueba para revisar el mensaje y el traceback.
- **Duración**: indica cuánto tardó cada prueba.
- **Captura de pantalla**: si falló una prueba de interfaz y se pudo guardar la imagen, aparece en los detalles de esa prueba.

El reporte se vuelve a generar cada vez que ejecutás pytest. Guardá una copia si necesitás conservar el resultado de una ejecución anterior.

## Integración continua

El proyecto utiliza GitHub Actions para ejecutar automáticamente las pruebas:

- Al subir cambios a `main` o a una rama cuyo nombre empiece con `feature/`.
- Al crear o actualizar una solicitud de incorporación hacia `main`.
- También se puede iniciar manualmente desde la pestaña **Actions** de GitHub.

El flujo, definido en `.github/workflows/ci.yml`, configura Python y Chrome, instala las dependencias y ejecuta pytest. En el servidor de CI, Chrome funciona en modo headless y Selenium Manager gestiona el controlador compatible.

Los resultados de cada ejecución se pueden consultar en la pestaña **Actions** del repositorio.
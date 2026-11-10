# Proyecto Final de Automatización QA

Proyecto de automatización de pruebas desarrollado con **Python**, **pytest**, **Selenium WebDriver** y **Requests**.

Se prueban dos servicios:

- **SauceDemo**, para las pruebas de interfaz web.
- **JSONPlaceholder**, para las pruebas de API.

## Tecnologías utilizadas

- Python
- pytest
- Selenium WebDriver
- Requests
- pytest-html

## Estructura del proyecto

```text
proyecto-final-automation-testing-carlos-brizuela/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── data/
│   ├── api_payloads.json
│   └── ui_users.json
├── logs/
├── pages/
│   ├── cart_page.py
│   ├── checkout_complete_page.py
│   ├── checkout_overview_page.py
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── reports/
│   └── screens/
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

## Ejecutar todas las pruebas:
### .\.venv\Scripts\python.exe -m pytest

## Ejecutar solamente las pruebas de interfaz:
### .\.venv\Scripts\python.exe -m pytest tests/ui

## Ejecutar solamente las pruebas de API:
### .\.venv\Scripts\python.exe -m pytest tests/api


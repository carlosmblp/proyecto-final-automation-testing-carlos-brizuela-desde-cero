import json
from pathlib import Path
from utils.logger import get_logger

import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "api_payloads.json"
)

with DATA_FILE.open(encoding="utf-8") as file:
    POST_DATA = json.load(file)["new_post"]
    logger = get_logger(__name__)



# La función hace una consulta a https://jsonplaceholder.typicode.com/posts/1. 
# Esa dirección pide el post cuyo identificador es 1. 
# JSONPlaceholder documenta ese endpoint y devuelve campos como id, userId, title y body.
def test_get_post():
    logger.info("Enviando GET a /posts/1")
    # requests.get(...) envía la petición. El resultado queda guardado en response.
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=10,
    )
    
    logger.info("GET /posts/1 respondió con estado %s", response.status_code)
    
    assert response.status_code == 200

    post = response.json()

    # Las siguientes líneas revisan que el post tenga los campos esperados y que algunos valores sean 
    # del tipo correcto. Por ejemplo, isinstance(post["userId"], int) comprueba que userId sea un 
    # número entero
    assert post["id"] == 1
    assert isinstance(post["userId"], int)
    assert isinstance(post["title"], str)
    assert post["title"] != ""
    assert isinstance(post["body"], str)
    assert post["body"] != ""
 
    
def test_create_post():
    logger.info("Enviando POST a /posts")
    response = requests.post(
        f"{BASE_URL}/posts",
        json=POST_DATA,
        timeout=10,
    )
    logger.info("POST /posts respondió con estado %s", response.status_code)
    assert response.status_code == 201

    created_post = response.json()

    assert created_post["title"] == POST_DATA["title"]
    assert created_post["body"] == POST_DATA["body"]
    assert created_post["userId"] == POST_DATA["userId"]
    assert isinstance(created_post["id"], int)
    
    
    
    # línea de comando para ejecutar los dos test
    # .\.venv\Scripts\python.exe -m pytest tests\api\test_posts.py

# requests.delete(...) envía una petición DELETE para el post 1. La prueba comprueba el estado 
# HTTP 200 y que el cuerpo de la respuesta sea {}. JSONPlaceholder documenta esa respuesta y 
# aclara que la eliminación es simulada: el post no se borra de forma permanente.   
def test_delete_post():
    logger.info("Enviando DELETE a /posts/1")
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=10,
    )
    
    logger.info("DELETE /posts/1 respondió con estado %s", response.status_code)
    assert response.status_code == 200
    assert response.json() == {}
    
# GET, POST y DELETE    
# .\.venv\Scripts\python.exe -m pytest tests\api\test_posts.py


# Esta prueba consulta una ruta que no corresponde a los recursos de la API y verifica que 
# responda con el estado HTTP 404 (“no encontrado”). Así la suite de API tendrá los tres métodos 
# requeridos y también una comprobación de error.
def test_unknown_route_returns_404():
    
    logger.info("Enviando not-a-resource")
    
    response = requests.get(
        f"{BASE_URL}/not-a-resource",
        timeout=10,
    )
    
    logger.info("La ruta inexistente respondió con estado %s", response.status_code)

    assert response.status_code == 404
    
# .\.venv\Scripts\python.exe -m pytest tests\api\test_posts.py
import logging
from pathlib import Path

# LOG_FILE apunta a logs/automation.log. 
# La ruta se calcula desde el proyecto, para que no dependa de dónde se ejecute pytest.
LOG_FILE = Path(__file__).resolve().parents[1] / "logs" / "automation.log"
# mkdir(...) crea la carpeta logs si todavía no existe.
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

# get_logger(name) devuelve un logger identificado por el nombre del módulo que lo usa.
def get_logger(name):
    logger = logging.getLogger(name)
    # logging.INFO permite registrar eventos informativos, 
    # como “inicio de sesión correcto” o “petición POST enviada”.
    logger.setLevel(logging.INFO)

    # if not logger.handlers evita agregar repetidamente el mismo manejador al logger.
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        # FileHandler escribe los mensajes en el archivo.
        file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        # Formatter define el formato: fecha y hora, nivel, módulo y mensaje.
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# para ver el logguer del test
# Get-Content .\logs\automation.log -Encoding utf8
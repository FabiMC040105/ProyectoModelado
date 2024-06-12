"""
Este módulo proporciona funciones para gestionar transacciones en el centro de acopio mediante archivos JSON.

Funciones disponibles:
- obtener_transacciones_centro_acopio: Obtiene las transacciones del centro de acopio filtradas por ID y opcionalmente por rango de fechas.

Constantes utilizadas:
- JSON_TRANSACCIONES_CENTRO_DE_ACOPIO: Ruta del archivo JSON que contiene las transacciones del centro de acopio.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- datetime.datetime: Para trabajar con fechas y horas.
"""

import json
import os
from datetime import datetime
from src.code.constantes import JSON_TRANSACCIONES_CENTRO_DE_ACOPIO


def obtener_transacciones():
    """
    Obtiene la lista de centros de acopio del archivo JSON.

    :return: Lista de centros de acopio.
    :rtype: list[dict]
    """
    archivo_transacciones = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_TRANSACCIONES_CENTRO_DE_ACOPIO)
    if os.path.exists(archivo_transacciones):
        with open(archivo_transacciones, "r") as file:
            data = json.load(file)
            return data.get("Transacciones", [])
    else:
        return []


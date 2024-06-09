"""
Este módulo proporciona funciones para gestionar centros de acopio mediante archivos JSON.

Funciones disponibles:
- agregar_centro_acopio_archivo: Agrega un nuevo centro de acopio al archivo JSON.
- obtener_centros_acopio: Obtiene la lista de centros de acopio del archivo JSON.

Constantes utilizadas:
- JSON_CENTRO_DE_ACOPIO: Ruta del archivo JSON que contiene la información de los centros de acopio.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
"""

import json
import os
from src.code.constantes import JSON_CENTRO_DE_ACOPIO

def agregar_centro_acopio_archivo(centro_acopio_id, sede, telefono, ubicacion, estado):
    """
    Agrega un nuevo centro de acopio al archivo JSON.

    :param centro_acopio_id: ID del centro de acopio.
    :type centro_acopio_id: str
    :param sede: Sede del centro de acopio.
    :type sede: str
    :param telefono: Número de teléfono del centro de acopio.
    :type telefono: str
    :param ubicacion: Ubicación del centro de acopio.
    :type ubicacion: str
    :param estado: Estado del centro de acopio.
    :type estado: str
    """
    nuevo_centro_acopio = {
        "id": centro_acopio_id,
        "sede": sede,
        "telefono": telefono,
        "ubicacion": ubicacion,
        "estado": estado
    }

    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "..", "db",  JSON_CENTRO_DE_ACOPIO)
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Centro de acopio": []
        }

    data["Centro de acopio"].append(nuevo_centro_acopio)

    with open(archivo_centros_acopio, "w") as file:
        json.dump(data, file, indent=4)

def obtener_centros_acopio():
    """
    Obtiene la lista de centros de acopio del archivo JSON.

    :return: Lista de centros de acopio.
    :rtype: list[dict]
    """
    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_CENTRO_DE_ACOPIO)
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
            return data.get("Centro de acopio", [])
    else:
        return []

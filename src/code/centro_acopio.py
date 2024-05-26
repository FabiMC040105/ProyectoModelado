import json
import os

from src.code.constantes import JSON_CENTRO_DE_ACOPIO


def agregar_centro_acopio_archivo(centro_acopio_id, sede, telefono, ubicacion, estado):
    """
    Agrega un nuevo centro de acopio al archivo JSON de instrucciones.

    Parámetros:
    - centro_acopio_id (str): ID del centro de acopio.
    - sede (str): Sede del centro de acopio.
    - telefono (str): Número de teléfono del centro de acopio.
    - ubicacion (str): Ubicación del centro de acopio.
    - estado (str): Estado del centro de acopio.
    """
    nuevo_centro_acopio = {
        "id": centro_acopio_id,
        "sede": sede,
        "telefono": telefono,
        "ubicacion": ubicacion,
        "estado": estado
    }

    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", JSON_CENTRO_DE_ACOPIO)
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
    Obtiene la lista de centros de acopio del archivo JSON de instrucciones.

    Retorna:
    - list: Lista de centros de acopio.
    """
    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", JSON_CENTRO_DE_ACOPIO)
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
            return data.get("Centro de acopio", [])
    else:
        return []

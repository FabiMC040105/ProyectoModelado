import json
import os

from src.code.constantes import JSON_MATERIAL
from src.code.funciones import obtener_fecha_actual


def agregar_material_archivo(material_id, nombre, unidad, valor, descripcion):
    """
    Agrega un nuevo material al archivo JSON especificado.

    Parámetros:
    - material_id (str): ID del material.
    - nombre (str): Nombre del material.
    - unidad (str): Unidad de medida del material.
    - valor (float): Valor del material.
    - descripcion (str): Descripción del material.
    """
    nuevo_material = {
        "id": material_id,
        "nombre": nombre,
        "unidad": unidad,
        "valor": valor,
        "estado": "Activo",
        "fecha_creacion": obtener_fecha_actual(),
        "descripcion": descripcion
    }

    archivo = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_MATERIAL)

    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Materiales": [],
        }

    data["Materiales"].append(nuevo_material)

    with open(archivo, "w") as file:
        json.dump(data, file, indent=4)



def obtener_materiales():
    """
    Obtiene la lista de materiales del archivo JSON especificado.

    Retorna:
    - list: Lista de materiales.
    """
    archivo_materiales = os.path.join(os.path.dirname(__file__), "..", "..", "db",  JSON_MATERIAL)
    if os.path.exists(archivo_materiales):
        with open(archivo_materiales, "r") as file:
            data = json.load(file)
            return data.get("Materiales", [])
    else:
        return []

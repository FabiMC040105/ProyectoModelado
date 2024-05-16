import random
import string
from datetime import datetime
import os
import json

def generar_id_unico():
    """
    Genera un ID único para un material.

    Returns:
        str: El ID único generado.
    """
    return "M-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def obtener_fecha_actual():
    """
    Obtiene la fecha y hora actual en el formato "%Y-%m-%d %H:%M:%S".

    Returns:
        str: La fecha y hora actual.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def agregar_material_archivo(archivo, material_id, nombre, unidad, valor, descripcion):
    """
    Agrega un nuevo material al archivo JSON especificado.

    Args:
        archivo (str): La ruta del archivo JSON.
        material_id (str): El ID del material.
        nombre (str): El nombre del material.
        unidad (str): La unidad de medida del material.
        valor (float): El valor del material.
        descripcion (str): La descripción del material.

    Returns:
        None
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

    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Materiales": [],
            "Sedes": [],
            "Centro de acopio": []
        }

    data["Materiales"].append(nuevo_material)

    with open(archivo, "w") as file:
        json.dump(data, file, indent=4)

def obtener_materiales(archivo):
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
            return data.get("Materiales", [])
    return []
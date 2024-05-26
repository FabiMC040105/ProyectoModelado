import random
import string
import json
import os
from datetime import datetime

from src.code.constantes import JSON_SEDE, JSON_CENTRO_DE_ACOPIO, JSON_MATERIAL
def agregar_material_archivo(archivo, material_id, nombre, unidad, valor, descripcion):
    """
    Agrega un nuevo material al archivo JSON especificado.

    Parámetros:
    - archivo (str): Ruta del archivo JSON.
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

    Parámetros:
    - archivo (str): Ruta del archivo JSON.

    Retorna:
    - list: Lista de materiales.
    """
    archivo_materiales = os.path.join(os.path.dirname(__file__), "..", JSON_MATERIAL)
    if os.path.exists(archivo_materiales):
        with open(archivo_materiales, "r") as file:
            data = json.load(file)
            return data.get("Materiales", [])
    else:
        return []

    
def cargar_materiales(self):
    """
    Carga los materiales en la tabla.
    """

    materiales = obtener_materiales()
    for material in materiales:
        self.tabla.insert("", "end", values=(
        material["id"], material["nombre"], material["unidad"], material["valor"], material["estado"],
        material["fecha_creacion"], material["descripcion"]))
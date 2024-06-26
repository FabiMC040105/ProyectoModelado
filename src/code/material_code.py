"""
Este módulo proporciona funciones para la gestión de materiales y la manipulación de archivos JSON.

Funciones disponibles:
- agregar_material_archivo: Agrega un nuevo material al archivo JSON especificado.
- obtener_materiales: Obtiene la lista de materiales del archivo JSON especificado.
- obtener_nombre_materiales: Obtiene una lista de nombres de materiales.
- cargar_materiales: Carga los materiales en la tabla.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- src.code.constantes.JSON_MATERIAL: Ruta del archivo JSON que contiene la información de los materiales.
- src.code.funciones.obtener_fecha_actual: Función para obtener la fecha actual.
"""

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

    archivo = os.path.join(os.path.dirname(__file__), "..", "db", JSON_MATERIAL)

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
    archivo_materiales = os.path.join(os.path.dirname(__file__), "..", "db",  JSON_MATERIAL)
    if os.path.exists(archivo_materiales):
        with open(archivo_materiales, "r") as file:
            data = json.load(file)
            return data.get("Materiales", [])
    else:
        return []

def obtener_nombre_materiales():
    """
    Obtiene una lista de nombres de materiales.

    Retorna:
    - list: Lista de nombres de materiales.
    """
    listanombremateriales = []
    materiales = obtener_materiales()
    for material in materiales:
        listanombremateriales.append(material.get("nombre"))
    return listanombremateriales


def cargar_materiales(self):
    """
    Carga los materiales en la tabla.
    """

    materiales = obtener_materiales()
    for material in materiales:
        self.tabla.insert("", "end", values=(
        material["id"], material["nombre"], material["unidad"], material["valor"], material["estado"],
        material["fecha_creacion"], material["descripcion"]))


def limpiar_formulario(app):
    """
    Limpia los campos del formulario de la aplicación.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.nombre_var.set("")
    app.unidad_var.set("")
    app.valor_var.set("")
    app.descripcion_var.set("")

"""
Este módulo proporciona funciones para gestionar materiales, sedes y centros de acopio mediante archivos JSON.

Funciones disponibles:
- generar_id_unico(prefix="M-"): Genera un ID único para los materiales con un prefijo opcional.
- obtener_provincias(): Retorna una lista de provincias de Costa Rica.
- agregar_material_archivo(archivo, material_id, nombre, unidad, valor, descripcion): Agrega un nuevo material al archivo JSON especificado.
- obtener_materiales(archivo): Obtiene la lista de materiales del archivo JSON especificado.
- agregar_sede_archivo(sede_id, nombre, ubicacion, estado, telefono): Agrega una nueva sede al archivo JSON de instrucciones.
- obtener_sedes(): Obtiene la lista de sedes del archivo JSON de instrucciones.
- agregar_centro_acopio_archivo(centro_acopio_id, sede, telefono, ubicacion, estado): Agrega un nuevo centro de acopio al archivo JSON de instrucciones.
- obtener_centros_acopio(): Obtiene la lista de centros de acopio del archivo JSON de instrucciones.
"""

import random
import string
import json
import os

def generar_id_unico(prefix="M-"):
    """
    Genera un ID único para los materiales con un prefijo opcional.

    Parámetros:
    - prefix (str): Prefijo opcional para el ID. Por defecto es "M-".

    Retorna:
    - str: ID generado.
    """
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def obtener_provincias():
    """
    Retorna una lista de provincias de Costa Rica.

    Retorna:
    - list: Lista de provincias.
    """
    return ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]

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
            "Sedes": [],
            "Centro de acopio": []
        }

    data["Materiales"].append(nuevo_material)

    with open(archivo, "w") as file:
        json.dump(data, file, indent=4)

def obtener_materiales(archivo):
    """
    Obtiene la lista de materiales del archivo JSON especificado.

    Parámetros:
    - archivo (str): Ruta del archivo JSON.

    Retorna:
    - list: Lista de materiales.
    """
    if os.path.exists(archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
            return data.get("Materiales", [])
    else:
        return []

def agregar_sede_archivo(sede_id, nombre, ubicacion, estado, telefono):
    """
    Agrega una nueva sede al archivo JSON de instrucciones.

    Parámetros:
    - sede_id (str): ID de la sede.
    - nombre (str): Nombre de la sede.
    - ubicacion (str): Ubicación de la sede.
    - estado (str): Estado de la sede.
    - telefono (str): Número de teléfono de la sede.
    """
    nueva_sede = {
        "id": sede_id,
        "nombre": nombre,
        "ubicacion": ubicacion,
        "estado": estado,
        "telefono": telefono
    }

    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Materiales": [],
            "Sedes": [],
            "Centro de acopio": []
        }

    data["Sedes"].append(nueva_sede)

    with open(archivo_sedes, "w") as file:
        json.dump(data, file, indent=4)

def obtener_sedes():
    """
    Obtiene la lista de sedes del archivo JSON de instrucciones.

    Retorna:
    - list: Lista de sedes.
    """
    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
            return data.get("Sedes", [])
    else:
        return []

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

    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Materiales": [],
            "Sedes": [],
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
    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
            return data.get("Centro de acopio", [])
    else:
        return []


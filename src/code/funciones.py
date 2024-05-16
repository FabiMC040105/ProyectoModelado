import random
import string
import json
import os

def generar_id_unico(prefix="M-"):
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def obtener_provincias():
    # Lista de provincias de Costa Rica
    return ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]

def agregar_material_archivo(archivo, material_id, nombre, unidad, valor, descripcion):
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
    else:
        return []

def agregar_sede_archivo(sede_id, nombre, ubicacion, estado, telefono):
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
    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
            return data.get("Sedes", [])
    else:
        return []

def agregar_centro_acopio_archivo(centro_acopio_id, sede, telefono, ubicacion, estado):
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
    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
    if os.path.exists(archivo_centros_acopio):
        with open(archivo_centros_acopio, "r") as file:
            data = json.load(file)
            return data.get("Centro de acopio", [])
    else:
        return []
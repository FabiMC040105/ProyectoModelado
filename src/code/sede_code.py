
import json
import os

from src.code.constantes import JSON_SEDE
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

    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "db", JSON_SEDE)
    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
    else:
        data = {
            "Sedes": []
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
    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "db", JSON_SEDE)

    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
            return data.get("Sedes", [])
    else:
        return []


def obtener_sedes_activas():
    """
    Obtiene las sedes activas.

    Retorna:
    - list: Lista de nombres de sedes activas.
    """
    sedes_activas = []
    sedes = obtener_sedes()
    for sede in sedes:
        if sede["estado"] == "Activo":
            sedes_activas.append(sede["nombre"])
    return sedes_activas
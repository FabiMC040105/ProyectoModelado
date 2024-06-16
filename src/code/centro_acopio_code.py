"""
Este módulo proporciona funciones para gestionar centros de acopio mediante archivos JSON.

Funciones disponibles:
- agregar_centro_acopio_archivo: Agrega un nuevo centro de acopio al archivo JSON.
- obtener_centros_acopio_activos: Obtiene la lista de centros de acopio activos.
- obtener_sede_de_centros_acopio: Obtiene la sede asociada a un centro de acopio por su ID.
- obtener_transacciones_centro_acopio_con_id: Obtiene las transacciones de un centro de acopio específico.
- limpiar_formulario_centro_acopio: Limpia los campos del formulario del centro de acopio.
- validar_campos_centro_acopio: Valida los campos del formulario del centro de acopio.
- validar_nombre_centro: Valida el nombre de un centro de acopio.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- tkinter.messagebox: Para mostrar mensajes de error en la interfaz gráfica.

Constantes utilizadas:
- JSON_CENTRO_DE_ACOPIO: Ruta del archivo JSON que contiene la información de los centros de acopio.
"""

import json
import os
from tkinter import messagebox

from src.code.constantes import JSON_CENTRO_DE_ACOPIO
from src.code.storage.centro_acopio_storage import obtener_centros_acopio

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

    archivo_centros_acopio = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_CENTRO_DE_ACOPIO)

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

def obtener_centros_acopio_activos():
    """
    Obtiene los centros de acopio activos.

    :return: Lista de centros de acopio activos.
    :rtype: list[dict]
    """
    centros_acopio_activos = []
    centros_acopio = obtener_centros_acopio()
    for centro in centros_acopio:
        if centro["estado"] == "Activo":
            centros_acopio_activos.append(centro)
    return centros_acopio_activos

def obtener_sede_de_centros_acopio(codigo):
    """
    Obtiene la sede asociada a un centro de acopio por su ID.

    :param codigo: ID del centro de acopio.
    :type codigo: str
    :return: Sede del centro de acopio.
    :rtype: str
    """
    centrosdeacopio = obtener_centros_acopio()
    for centro in centrosdeacopio:
        if centro["id"] == codigo:
            return centro["sede"]

def obtener_transacciones_centro_acopio_con_id(transacciones, id_centro_acopio):
    """
    Obtiene las transacciones de un centro de acopio específico.

    :param transacciones: Lista de transacciones.
    :type transacciones: list[dict]
    :param id_centro_acopio: ID del centro de acopio.
    :type id_centro_acopio: str
    :return: Lista de transacciones del centro de acopio.
    :rtype: list[dict]
    """
    transacciones_centro_acopio = [t for t in transacciones if t["id_centro_de_acopio"] == id_centro_acopio]
    return transacciones_centro_acopio

def limpiar_formulario_centro_acopio(app):
    """
    Limpia los campos del formulario del centro de acopio.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.sede_var.set("")
    app.telefono_var.set("")
    app.ubicacion_var.set("")
    app.estado_var.set("")
    app.codigo_var.set("")

def validar_campos_centro_acopio(ubicacion, estado, telefono, codigo):
    """
    Valida los campos del formulario del centro de acopio.

    :param ubicacion: La ubicación del centro de acopio.
    :type ubicacion: str
    :param estado: El estado del centro de acopio.
    :type estado: str
    :param telefono: El número de teléfono del centro de acopio.
    :type telefono: str
    :param codigo: El código ID del centro de acopio.
    :type codigo: str
    :return: True si los campos son válidos, False en caso contrario.
    :rtype: bool
    """
    centrosdeacopio = obtener_centros_acopio()
    idvalida = True
    for centro in centrosdeacopio:
        if centro["id"] == codigo:
            idvalida = False
    if not idvalida:
        messagebox.showerror("Error", "Ya existe un Centro de acopio con ese nombre")
        return False

    # Validar que todos los campos estén completos
    if not telefono or not ubicacion or not estado or not codigo:
        messagebox.showerror("Error", "Por favor complete todos los campos.")
        return False

    # Validar el formato del número de teléfono
    if not telefono.isdigit() or len(telefono) != 8:
        messagebox.showerror("Error", "El número de teléfono debe ser un valor numérico de 8 dígitos.")
        return False
    return True

def validar_nombre_centro(id_centro):
    """
    Valida el nombre de un centro de acopio.

    :param id_centro: El ID del centro de acopio a validar.
    :type id_centro: str
    :return: True si el nombre del centro de acopio es válido, False si no lo es.
    :rtype: bool
    """
    centros = obtener_centros_acopio_activos()

    for centro in centros:
        if centro["id"] == id_centro:
            return True
    return False

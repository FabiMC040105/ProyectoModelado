"""
Este módulo proporciona funciones para la gestión de sedes y la manipulación de archivos JSON.

Funciones disponibles:
- obtener_sedes_activas: Obtiene las sedes activas.
- validar_nombre_sede: Valida el nombre de una sede.
- validar_campos_form_sede: Valida los campos del formulario de sede.
- limpiar_formulario_sede: Limpia los campos del formulario de la aplicación.

Dependencias:
- tkinter.messagebox: Para mostrar mensajes de error en la interfaz gráfica.
- src.code.storage.sede_storage.obtener_sedes: Función para obtener la lista de sedes.

"""

from tkinter import messagebox
from src.code.storage.sede_storage import obtener_sedes

def obtener_sedes_activas():
    """
    Obtiene las sedes activas.

    :return: Lista de nombres de sedes activas.
    :rtype: list
    """
    sedes_activas = []
    sedes = obtener_sedes()
    for sede in sedes:
        if sede["estado"] == "Activo":
            sedes_activas.append(sede["nombre"])
    return sedes_activas

def validar_nombre_sede(nombre_sede):
    """
    Valida el nombre de una sede.

    :param nombre_sede: El nombre de la sede a validar.
    :type nombre_sede: str
    :return: True si el nombre de la sede es válido, False si no lo es.
    :rtype: bool
    """
    sedes = obtener_sedes_activas()

    for sede in sedes:
        if sede == nombre_sede:
            return True
    messagebox.showerror("Error de sede", "Nombre de sede incorrecto")
    return False

def validar_campos_form_sede(nombre, ubicacion, estado, telefono):
    """
    Valida los campos del formulario de sede.

    :param nombre: El nombre de la sede.
    :type nombre: str
    :param ubicacion: La ubicación de la sede.
    :type ubicacion: str
    :param estado: El estado de la sede.
    :type estado: str
    :param telefono: El número de teléfono de la sede.
    :type telefono: str
    :return: True si los campos son válidos, False en caso contrario.
    :rtype: bool
    """
    sedes = obtener_sedes()
    nombrevalido = True
    for sede in sedes:
        if sede["nombre"].upper() == nombre.upper():
            nombrevalido = False
    if not nombrevalido:
        messagebox.showerror("Error", "Ya existe un sede con ese nombre")
        return False
    if not nombre or not ubicacion or not estado or not telefono:
        messagebox.showerror("Error", "Por favor complete todos los campos.")
        return False

    try:
        telefono = int(telefono)
    except ValueError:
        messagebox.showerror("Error", "El número de teléfono debe ser numérico.")
        return False

    if len(str(telefono)) != 8:
        messagebox.showerror("Error", "El número de teléfono debe tener 8 dígitos.")
        return False
    return True

def limpiar_formulario_sede(app):
    """
    Limpia los campos del formulario de la aplicación.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.nombre_var.set("")
    app.ubicacion_var.set("")
    app.estado_var.set("")
    app.telefono_var.set("")
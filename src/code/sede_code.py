"""
Este módulo proporciona funciones para la gestión de sedes y la manipulación de archivos JSON.

Funciones disponibles:
- agregar_sede_archivo: Agrega una nueva sede al archivo JSON de sedes.
- obtener_sedes: Obtiene la lista de sedes del archivo JSON de sedes.
- obtener_sedes_activas: Obtiene las sedes activas.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- src.code.constantes.JSON_SEDE: Ruta del archivo JSON que contiene la información de las sedes.
"""

from tkinter import messagebox

from src.code.storage.sede_storage import obtener_sedes


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
def validar_nombre_sede(nombre_sede):
    sedes = obtener_sedes_activas()

    for sede in sedes:
        if sede == nombre_sede:
            return True
    messagebox.showerror("Error de sede", "Nombre de sede incorrecto")
    return False

def validar_campos_form_sede( nombre, ubicacion, estado, telefono):
    """
    Valida los campos del formulario.

    Parámetros:
    - nombre: El nombre de la sede.
    - ubicacion: La ubicación de la sede.
    - estado: El estado de la sede.
    - telefono: El número de teléfono de la sede.

    Retorna:
    - bool: True si los campos son válidos, False en caso contrario.
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
    app.nombre_var.set("")
    app.ubicacion_var.set("")
    app.estado_var.set("")
    app.telefono_var.set("")

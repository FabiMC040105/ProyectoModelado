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

from tkinter import messagebox
from src.code.storage.material_storage import obtener_materiales


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


def limpiar_formulario_material(app):
    """
    Limpia los campos del formulario de la aplicación.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.nombre_var.set("")
    app.unidad_var.set("")
    app.valor_var.set("")
    app.descripcion_var.set("")



def validar_campos_material( nombre, unidad, valor, descripcion):
    """
    Valida los campos del formulario.

    Parámetros:
    - nombre: El nombre del material.
    - unidad: La unidad de medida del material.
    - valor: El valor unitario del material.
    - descripcion: La descripción del material.

    Retorna:
    - bool: True si los campos son válidos, False en caso contrario.
    """
    materiales = obtener_materiales()
    nombrevalido = True
    for material in materiales:
        if material["nombre"].upper() == nombre.upper():
            nombrevalido = False
    if not nombrevalido:
        messagebox.showerror("Error", "Ya existe un material con ese nombre")
        return False

    if not nombre or not unidad or not valor:
        messagebox.showerror("Error", "Por favor complete todos los campos.")
        return False
    try:
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Error", "El valor unitario debe ser numérico.")
        return False

    if valor < 1 or valor > 100_000:
        messagebox.showerror("Error", "El valor debe encontrarse en el rango de 1 a 100 000.")
        return False

    if len(nombre) < 5 or len(nombre) > 30:
        messagebox.showerror("Error", "El nombre del material debe tener entre 5 y 30 caracteres.")
        return False

    if len(descripcion) > 1000:
        messagebox.showerror("Error", "La descripción debe tener como máximo 1000 caracteres.")
        return False
    return True

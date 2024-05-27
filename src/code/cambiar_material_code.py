"""
Este módulo proporciona funciones para gestionar transacciones de centros de acopio mediante archivos JSON.

Funciones disponibles:
- obtener_nombre_materiales: Obtiene los nombres de los materiales disponibles.
- obtener_detalles_material: Obtiene los detalles de un material específico.
- validar_cantidad_material: Valida la cantidad ingresada para un material.
- calcular_monto: Calcula el monto total de una transacción.
- limpiar_formulario: Limpia los campos del formulario de la aplicación.
- limpiar_material_formulario: Limpia los campos relacionados con el material en el formulario.
- registrar_transaccion: Registra una nueva transacción en el archivo JSON.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- datetime: Para obtener la fecha y hora actual.
- tkinter.messagebox: Para mostrar mensajes de error en la interfaz gráfica.

Constantes utilizadas:
- JSON_TRANSACCIONES_CENTRO_DE_ACOPIO: Ruta del archivo JSON que contiene las transacciones de centros de acopio.
- PREFIJO_TRANSACCION: Prefijo para generar IDs únicos de transacciones.

Módulos relacionados:
- src.code.material_code: Contiene funciones relacionadas con la gestión de materiales.

"""

import json
import os
from datetime import datetime
from tkinter import messagebox
from src.code.constantes import JSON_TRANSACCIONES_CENTRO_DE_ACOPIO, PREFIJO_TRANSACCION
from src.code.funciones import generar_id_unico, obtener_funcionarios
from src.code.material_code import obtener_materiales

def obtener_nombre_materiales():
    """
    Obtiene los nombres de los materiales disponibles.

    :return: Lista de nombres de materiales.
    :rtype: list[str]
    """
    materiales = obtener_materiales()
    return [material['nombre'] for material in materiales]

def obtener_detalles_material(nombre):
    """
    Obtiene los detalles de un material específico.

    :param nombre: Nombre del material.
    :type nombre: str
    :return: Detalles del material.
    :rtype: dict
    """
    materiales = obtener_materiales()
    for material in materiales:
        if material['nombre'] == nombre:
            return material
    return {}

def validar_cantidad_material(cantidad, nombre_material):
    """
    Valida la cantidad ingresada para un material.

    :param cantidad: Cantidad del material.
    :type cantidad: str
    :param nombre_material: Nombre del material.
    :type nombre_material: str
    :return: True si la cantidad es válida, False si no lo es.
    :rtype: bool
    """
    material = obtener_detalles_material(nombre_material)
    unidad = material['unidad']
    try:
        if unidad == "Unidad" and not cantidad.isdigit():
            raise ValueError("La cantidad debe ser un número entero.")
        cantidad = float(cantidad)
        if unidad != "Unidad" and cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")
    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False
    return True

def calcular_monto(valor, cantidad):
    """
    Calcula el monto total de una transacción.

    :param valor: Valor unitario del material.
    :type valor: float
    :param cantidad: Cantidad del material.
    :type cantidad: float
    :return: Monto total de la transacción.
    :rtype: float
    """
    return round(float(valor) * float(cantidad), 2)

def limpiar_formulario(app):
    """
    Limpia los campos del formulario de la aplicación.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.carnet_var.set("")
    app.sede_var.set("")
    app.material_var.set("")
    app.detalle_var.set("")
    app.cantidad_var.set("")

def limpiar_material_formulario(app):
    """
    Limpia los campos relacionados con el material en el formulario.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.material_var.set("")
    app.detalle_var.set("")
    app.cantidad_var.set("")

def registrar_transaccion(carnet, id_funcionario, sede, materiales, total):
    """
    Registra una nueva transacción en el archivo JSON.

    :param carnet: Carnet del estudiante.
    :type carnet: str
    :param id_funcionario: ID del funcionario.
    :type id_funcionario: str
    :param sede: Sede del centro de acopio.
    :type sede: str
    :param materiales: Lista de materiales de la transacción.
    :type materiales: list[dict]
    :param total: Total de la transacción.
    :type total: float
    :return: True si se registra la transacción correctamente, False si ocurre un error.
    :rtype: bool
    """
    try:
        archivo_transacciones = os.path.join(os.path.dirname(__file__), "..", "db", JSON_TRANSACCIONES_CENTRO_DE_ACOPIO)
        if os.path.exists(archivo_transacciones):
            with open(archivo_transacciones, "r") as file:
                data = json.load(file)
        else:
            data = {"Transacciones": []}
        funcionario = obtener_funcionarios(id_funcionario)
        transaccion = {
            "id_transaccion": generar_id_unico(PREFIJO_TRANSACCION),
            "carnet": carnet,
            "id_funcionario": id_funcionario,
            "id_centro_de_acopio": funcionario["idcentro"],
            "sede": sede,
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "materiales": materiales,
            "total": total
        }

        data["Transacciones"].append(transaccion)

        with open(archivo_transacciones, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error registrando la transacción: {e}")
        return False

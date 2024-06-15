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


from tkinter import messagebox

from src.code.centro_acopio_code import validar_nombre_centro
from src.code.material_code import obtener_materiales
from src.code.sede_code import validar_nombre_sede
from src.code.storage.validar_credenciales import verificar_correo_estudiante


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
        if cantidad =='':
            messagebox.showerror("Error de material", "Debe ingresar una cantidad.")
            return False
        if unidad == "Unidad" and not cantidad.isdigit():
            raise ValueError("La cantidad debe ser un número entero.")
        cantidad = float(cantidad)

        if unidad != "Unidad" and cantidad <= 0:
            messagebox.showerror("Error de material", "La cantidad debe ser un número positivo.")
            return False
    except ValueError as e:
        messagebox.showerror("Error de Validación", str(e))
        return False
    return True


def validar_nombre_material(nombre_material):
    materiales = obtener_nombre_materiales()

    for material in materiales:
        if material == nombre_material:
            return True
    messagebox.showerror("Error de material", "Nombre de material incorrecto")
    return False


def validar_campos_material(nombre_material, cantidad):
    if (not validar_nombre_material(nombre_material)
            or not validar_cantidad_material(cantidad, nombre_material)):
        return False
    else:
        return True
def validar_campos_transacción(materiales, centro, carnet):
    if len(materiales) < 1:
        messagebox.showerror("Érror", "Debe agregar materiales a la transacción.")
        return False
    if not validar_nombre_centro(centro):
        messagebox.showerror("Error de sede", "Nombre de sede incorrecto")
        return False
    if not verificar_correo_estudiante(carnet):
        messagebox.showerror("Error de carnet", "Carnet incorrecto")
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

def cacular_monto_total_cambio(datos_tabla):
    total_cambio = 0
    for item in datos_tabla:
        total_cambio += float(item)
    return total_cambio

def limpiar_formulario_cambiar_material(app):
    """
    Limpia los campos relacionados con el material en el formulario.

    :param app: Objeto de la aplicación.
    :type app: tkinter.Tk
    """
    app.material_var.set("")
    app.detalle_var.set("")
    app.cantidad_var.set("")



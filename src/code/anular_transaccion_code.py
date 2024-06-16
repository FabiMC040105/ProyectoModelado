"""
Este módulo proporciona funciones para la gestión de transacciones, específicamente para la anulación de transacciones de centros de acopio.

Funciones disponibles:
- verificar_anulacion_previa: Verifica si una transacción ya ha sido anulada.
- actualizar_saldo_estudiante: Actualiza el saldo del estudiante.
- verificar_campos_anular_transaccion: Verifica los campos necesarios para anular una transacción.
- obtener_transaccion_por_id: Obtiene una transacción por su ID.
- crear_id_anulado: Crea un ID único para la transacción anulada.
- crear_transaccion_anulada: Crea una nueva transacción anulada basada en la original.

Dependencias:
- datetime: Para trabajar con fechas y horas.
- tkinter.messagebox: Para mostrar mensajes de información y error.
- src.code.constantes: Para obtener constantes utilizadas en el módulo.
- src.code.storage.ver_transacciones_storage: Para obtener las transacciones almacenadas.
"""

from datetime import datetime
from tkinter import messagebox
from src.code.constantes import PREFIJO_ANULAR
from src.code.storage.ver_transacciones_storage import obtener_transacciones

def verificar_anulacion_previa(id_transaccion):
    """
    Verifica si una transacción ya ha sido anulada.

    :param id_transaccion: ID de la transacción a verificar.
    :type id_transaccion: str
    :return: True si la transacción ya está anulada, False en caso contrario.
    :rtype: bool
    """
    transacciones = obtener_transacciones()
    for transaccion in transacciones:
        if transaccion["id_transaccion"].startswith(id_transaccion + PREFIJO_ANULAR):
            return True
    return False

def actualizar_saldo_estudiante(carnet, monto_anulado):
    """
    Actualiza el saldo del estudiante.

    :param carnet: Carnet del estudiante.
    :type carnet: str
    :param monto_anulado: Monto anulado a actualizar.
    :type monto_anulado: float
    """
    # Aquí debes implementar la lógica para actualizar el saldo del estudiante.
    # Este es solo un ejemplo ficticio.
    print(f"Actualizando saldo del estudiante {carnet} con monto anulado: {monto_anulado}")

def verificar_campos_anular_transaccion(id_transaccion):
    """
    Verifica los campos necesarios para anular una transacción.

    :param id_transaccion: ID de la transacción a anular.
    :type id_transaccion: str
    :return: True si los campos son válidos, False en caso contrario.
    :rtype: bool
    """
    if not id_transaccion:
        messagebox.showerror("Error", "Debe ingresar un ID de transacción")
        return False
    if verificar_anulacion_previa(id_transaccion):
        messagebox.showerror("Error", "Esta transacción ya ha sido anulada")
        return False
    return True

def obtener_transaccion_por_id(id_transaccion):
    """
    Obtiene una transacción por su ID.

    :param id_transaccion: ID de la transacción a obtener.
    :type id_transaccion: str
    :return: La transacción si se encuentra, None en caso contrario.
    :rtype: dict or None
    """
    transacciones = obtener_transacciones()
    for transaccion in transacciones:
        if transaccion["id_transaccion"] == id_transaccion:
            return transaccion
    messagebox.showerror("Error", "Transacción no encontrada")
    return None

def crear_id_anulado(id_transaccion, fecha_anulacion):
    """
    Crea un ID único para la transacción anulada.

    :param id_transaccion: ID de la transacción original.
    :type id_transaccion: str
    :param fecha_anulacion: Fecha y hora de la anulación.
    :type fecha_anulacion: str
    :return: ID único para la transacción anulada.
    :rtype: str
    """
    return id_transaccion + PREFIJO_ANULAR + fecha_anulacion

def crear_transaccion_anulada(transaccion_original):
    """
    Crea una nueva transacción anulada basada en la original.

    :param transaccion_original: La transacción original a anular.
    :type transaccion_original: dict
    :return: La nueva transacción anulada.
    :rtype: dict
    """
    fecha_anulacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id_anulacion = crear_id_anulado(transaccion_original["id_transaccion"], fecha_anulacion)
    monto_anulado = -transaccion_original["total"]
    transaccion_anulada = {
        "id_transaccion": id_anulacion,
        "carnet": transaccion_original["carnet"],
        "id_funcionario": transaccion_original["id_funcionario"],
        "id_centro_de_acopio": transaccion_original["id_centro_de_acopio"],
        "sede": transaccion_original["sede"],
        "fecha_hora": fecha_anulacion,
        "materiales": transaccion_original["materiales"],
        "total": monto_anulado
    }
    return transaccion_anulada

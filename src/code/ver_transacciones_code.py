"""
Este módulo contiene funciones relacionadas con la gestión de transacciones en el centro de acopio.

Funciones disponibles:
- cargar_transacciones: Carga y filtra las transacciones del centro de acopio según el ID del funcionario y
  opcionalmente por rango de fechas.

Dependencias:
- src.code.storage.funcionarios_storage.obtener_funcionarios: Función para obtener la información de un funcionario.
- src.code.storage.ver_transacciones_storage.obtener_transacciones_archivo: Función para obtener las transacciones
  del centro de acopio desde un archivo.
"""
from datetime import datetime
from tkinter import messagebox

from src.code.centro_acopio_code import obtener_transacciones_centro_acopio_con_id
from src.code.storage.ver_transacciones_storage import obtener_transacciones


def validar_formato_fecha(fecha):
    """
    Valida el formato de una fecha en formato "YYYY-MM-DD".

    Parámetros:
    - fecha (str): Fecha en formato "YYYY-MM-DD".

    Retorna:
    - bool: True si el formato es correcto, False si no lo es.
    """
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        messagebox.showerror("Fecha inválida", "Revise el formato en que escribió la fecha.")
        return False
def verificar_existencia_transacciones(transacciones):
    if not transacciones:
        messagebox.showinfo("Sin transacciones",
                            "No hay transacciones para mostrar para el centro de acopio seleccionado.")
def mostrar_transacciones_tabla(app, transacciones):
        for transaccion in transacciones:
            app.tabla.insert("", "end", values=(
                transaccion["id_transaccion"], transaccion["carnet"], transaccion["sede"], transaccion["fecha_hora"],
                ', '.join([f"{m['nombre']} ({m['cantidad']})" for m in transaccion["materiales"]]), transaccion["total"]
            ))


def validar_rango_fechas(fecha_inicio, fecha_fin):
    """
    Valida que la fecha de inicio sea menor o igual que la fecha de fin, y que ambas estén en formato correcto.

    Parámetros:
    - fecha_inicio (str): Fecha de inicio en formato "YYYY-MM-DD".
    - fecha_fin (str): Fecha de fin en formato "YYYY-MM-DD".

    Retorna:
    - bool: True si el rango de fechas es válido, False si no lo es.
    """
    if not validar_formato_fecha(fecha_inicio) or not validar_formato_fecha(fecha_fin):
        return False

    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    if not inicio <= fin:
        messagebox.showerror("Fecha inválida", "El orden de las fechas es incorrecto.")
        return False

    return True


def obtener_transacciones_centro_acopio(id_centro_acopio, fecha_inicio=None, fecha_fin=None):
    """
    Obtiene las transacciones del centro de acopio filtradas por ID y opcionalmente por rango de fechas.

    Parámetros:
    - id_centro_acopio (str): ID del centro de acopio. Si es una cadena vacía (''), se muestran todas las transacciones de todos los centros de acopio.
    - fecha_inicio (str, opcional): Fecha de inicio para el filtrado de transacciones (en formato "YYYY-MM-DD").
    - fecha_fin (str, opcional): Fecha de fin para el filtrado de transacciones (en formato "YYYY-MM-DD").

    Retorna:
    - list: Lista de transacciones filtradas y ordenadas por fecha en orden descendente.
    """

    transacciones = obtener_transacciones()
    if fecha_inicio and fecha_fin:
        if not validar_rango_fechas(fecha_inicio, fecha_fin):
            return
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        transacciones = [t for t in transacciones if
                         fecha_inicio <= datetime.strptime(t["fecha_hora"], "%Y-%m-%d %H:%M:%S") <= fecha_fin]

    if 0 < len(id_centro_acopio):
        transacciones_centro_acopio = obtener_transacciones_centro_acopio_con_id(transacciones, id_centro_acopio)
    else:
        transacciones_centro_acopio = transacciones

    return sorted(transacciones_centro_acopio,
                  key=lambda x: datetime.strptime(x["fecha_hora"], "%Y-%m-%d %H:%M:%S"), reverse=True)

"""
Este módulo contiene funciones relacionadas con la gestión de transacciones en el centro de acopio.

Funciones disponibles:
- cargar_transacciones: Carga y filtra las transacciones del centro de acopio según el ID del funcionario y opcionalmente por rango de fechas.
"""
from src.code.storage.funcionarios_storage import obtener_funcionarios
from src.code.storage.ver_transacciones_storage import obtener_transacciones_archivo


def cargar_transacciones(id_funcionario, fecha_inicio=None, fecha_fin=None):
    """
    Carga y filtra las transacciones del centro de acopio.

    Parámetros:
    - id_funcionario: ID del funcionario cuyas transacciones se desean cargar.
    - fecha_inicio: Fecha de inicio para el filtrado de transacciones (opcional).
    - fecha_fin: Fecha de fin para el filtrado de transacciones (opcional).

    Retorna:
    - Una lista de transacciones filtradas y ordenadas por fecha en orden descendente.
    """
    funcionario = obtener_funcionarios(id_funcionario)
    return obtener_transacciones_archivo(funcionario, fecha_inicio=None, fecha_fin=None)


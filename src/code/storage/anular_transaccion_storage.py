"""
Este módulo proporciona funciones para la gestión de transacciones, específicamente para la anulación de transacciones de centros de acopio.

Funciones disponibles:
- agregar_transaccion_anulada_archivo: Agrega una transacción anulada al archivo JSON.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- src.code.constantes: Para obtener constantes utilizadas en el módulo.
- src.code.storage.ver_transacciones_storage: Para obtener las transacciones almacenadas.
"""

import json
import os
from src.code.constantes import JSON_TRANSACCIONES_CENTRO_DE_ACOPIO
from src.code.storage.ver_transacciones_storage import obtener_transacciones

def agregar_transaccion_anulada_archivo(transaccion_anulada):
    """
    Agrega una transacción anulada al archivo JSON.

    :param transaccion_anulada: La transacción anulada a agregar.
    :type transaccion_anulada: dict
    """
    transacciones = obtener_transacciones()
    archivo_transacciones = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_TRANSACCIONES_CENTRO_DE_ACOPIO)
    transacciones.append(transaccion_anulada)
    with open(archivo_transacciones, 'w') as file:
        json.dump({"Transacciones": transacciones}, file, indent=4)

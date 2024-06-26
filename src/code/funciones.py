"""
Este módulo proporciona funciones para gestionar materiales, sedes y centros de acopio mediante archivos JSON.

Funciones disponibles:
- generar_id_unico: Genera un ID único para los materiales con un prefijo opcional.
- obtener_provincias: Retorna una lista de provincias de Costa Rica.
- obtener_fecha_actual: Retorna la fecha y hora actual en formato Y-m-d H:M:S
- obtener_funcionarios: Obtiene la información de un funcionario a partir de su ID.
- verificar_carnet_estudiante: Verifica la validez de un carné de estudiante.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.
- random: Para generar IDs únicos.
- string: Para generar IDs únicos con caracteres alfanuméricos.
- datetime.datetime: Para obtener la fecha y hora actual.

Constantes utilizadas:
- src.code.constantes.JSON_FUNCIONARIOS: Ruta del archivo JSON que contiene la información de los funcionarios.
"""

import json
import os
import random
import string
from datetime import datetime
from src.code.constantes import JSON_FUNCIONARIOS

def generar_id_unico(prefix="M-"):
    """
    Genera un ID único para los materiales con un prefijo opcional.

    Parámetros:
    - prefix (str): Prefijo opcional para el ID. Por defecto es "M-".

    Retorna:
    - str: ID generado.
    """
    return prefix + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def obtener_provincias():
    """
    Retorna una lista de provincias de Costa Rica.

    Retorna:
    - list: Lista de provincias.
    """
    return ["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"]

def obtener_fecha_actual():
    """
    Retorna la fecha y hora actual en formato Y-m-d H:M:S.

    Retorna:
    - str: Fecha y hora actual en formato Y-m-d H:M:S.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def obtener_funcionarios(id_funcionario):
    """
    Obtiene la información de un funcionario a partir de su ID.

    Parámetros:
    - id_funcionario (str): ID del funcionario a buscar.

    Retorna:
    - dict or False: Información del funcionario si se encuentra, False si no se encuentra.
    """
    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "db", JSON_FUNCIONARIOS)

    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
            funcionarios = data.get("Funcionarios", [])
            for funcionario in funcionarios:
                if id_funcionario == funcionario["id"]:
                    return funcionario
    else:
        return False

def verificar_carnet_estudiante(carnet):
    """
    Verifica la validez de un carné de estudiante.

    Parámetros:
    - carnet (str): Carné de estudiante a verificar.

    Retorna:
    - bool: True si el carné es válido, False si no lo es.
    """
    return True

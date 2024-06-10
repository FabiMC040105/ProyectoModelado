import json
import os

from src.code.constantes import JSON_FUNCIONARIOS


def obtener_funcionarios(id_funcionario):
    """
    Obtiene la información de un funcionario a partir de su ID.

    Parámetros:
    - id_funcionario (str): ID del funcionario a buscar.

    Retorna:
    - dict or False: Información del funcionario si se encuentra, False si no se encuentra.
    """
    archivo_sedes = os.path.join(os.path.dirname(__file__), "..", "..", "db", JSON_FUNCIONARIOS)

    if os.path.exists(archivo_sedes):
        with open(archivo_sedes, "r") as file:
            data = json.load(file)
            funcionarios = data.get("Funcionarios", [])
            for funcionario in funcionarios:
                if id_funcionario == funcionario["id"]:
                    return funcionario
    else:
        return False
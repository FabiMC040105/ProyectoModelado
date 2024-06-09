import json
import os
from datetime import datetime

from src.code.constantes import PREFIJO_TRANSACCION, JSON_TRANSACCIONES_CENTRO_DE_ACOPIO
from src.code.funciones import generar_id_unico
from src.code.storage.funcionarios_storage import obtener_funcionarios


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
        archivo_transacciones = os.path.join(os.path.dirname(__file__), "..","..", "db", JSON_TRANSACCIONES_CENTRO_DE_ACOPIO)
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

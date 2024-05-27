import json
import os
from datetime import datetime

from src.code.constantes import JSON_TRANSACCIONES_CENTRO_DE_ACOPIO


def cargar_transacciones(id_funcionario, fecha_inicio=None, fecha_fin=None):
    archivo_transacciones = os.path.join(os.path.dirname(__file__), "..", "db", JSON_TRANSACCIONES_CENTRO_DE_ACOPIO)
    if os.path.exists(archivo_transacciones):
        with open(archivo_transacciones, "r") as file:
            data = json.load(file)
            transacciones = data.get("Transacciones", [])

            if fecha_inicio and fecha_fin:
                fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
                transacciones = [t for t in transacciones if fecha_inicio <= datetime.strptime(t["fecha_hora"], "%Y-%m-%d %H:%M:%S") <= fecha_fin]

            transacciones_funcionario = [t for t in transacciones if t["id_funcionario"] == id_funcionario]
            return sorted(transacciones_funcionario, key=lambda x: datetime.strptime(x["fecha_hora"], "%Y-%m-%d %H:%M:%S"), reverse=True)
    else:
        return []
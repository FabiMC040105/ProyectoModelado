import json
import os
from datetime import datetime
from tkinter import messagebox

from src.code.constantes import JSON_TRANSACCIONES_CENTRO_DE_ACOPIO, PREFIJO_TRANSACCION
from src.code.funciones import generar_id_unico, obtener_funcionarios
from src.code.material_code import obtener_materiales


def obtener_nombre_materiales():
    materiales = obtener_materiales()
    return [material['nombre'] for material in materiales]

def obtener_detalles_material(nombre):
    materiales = obtener_materiales()
    for material in materiales:
        if material['nombre'] == nombre:
            return material
    return {}

def validar_cantidad_material(cantidad, nombre_material):
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
    return round(float(valor) * float(cantidad), 2)

def limpiar_formulario(app):
    app.carnet_var.set("")
    app.sede_var.set("")
    app.material_var.set("")
    app.detalle_var.set("")
    app.cantidad_var.set("")

def limpiar_material_formulario(app):
    app.material_var.set("")
    app.detalle_var.set("")
    app.cantidad_var.set("")
def registrar_transaccion(carnet, id_funcionario, sede, materiales, total):
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

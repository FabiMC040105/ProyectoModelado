from tkinter import messagebox

from src.code.storage.centro_acopio_storage import obtener_centros_acopio


def limpiar_formulario_centro_acopio(app):
    app.sede_var.set("")
    app.telefono_var.set("")
    app.ubicacion_var.set("")
    app.estado_var.set("")
    app.codigo_var.set("")


def validar_campos_centro_acopio(ubicacion, estado, telefono, codigo):
    """
    Valida los campos del formulario.

    Parámetros:
    - ubicacion: La ubicación del centro de acopio.
    - estado: El estado del centro de acopio.
    - telefono: El número de teléfono del centro de acopio.
    - codigo: El código ID del centro de acopio.

    Retorna:
    - bool: True si los campos son válidos, False en caso contrario.
    """
    centrosdeacopio = obtener_centros_acopio()
    idvalida = True
    for centro in centrosdeacopio:
        if centro["id"] == codigo:
            idvalida = False
    if not idvalida:
        messagebox.showerror("Error", "Ya existe un Centro de acopio con ese nombre")
        return False

    # Validar que todos los campos estén completos
    if not telefono or not ubicacion or not estado or not codigo:
        messagebox.showerror("Error", "Por favor complete todos los campos.")
        return False

    # Validar el formato del número de teléfono
    if not telefono.isdigit() or len(telefono) != 8:
        messagebox.showerror("Error", "El número de teléfono debe ser un valor numérico de 8 dígitos.")
        return False
    return True

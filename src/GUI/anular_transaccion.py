"""
Este módulo proporciona la interfaz gráfica para anular transacciones de centros de acopio.

Funciones disponibles:
- actualizar_tabla: Actualiza la tabla de transacciones.
- anular_transaccion: Anula una transacción específica.

Dependencias:
- tkinter: Para crear la interfaz gráfica.
- tkinter.messagebox: Para mostrar mensajes de información y error.
- src.code.constantes: Para obtener las columnas de la tabla de transacciones de centros de acopio.
- src.code.anular_transaccion_code: Para verificar los campos, obtener transacciones y actualizar el saldo.
- src.code.storage.anular_transaccion_storage: Para agregar una transacción anulada al archivo.
- src.code.storage.ver_transacciones_storage: Para obtener las transacciones.
- src.code.ver_transacciones_code: Para mostrar las transacciones en la tabla y verificar la existencia de transacciones.

Clases:
- AnularTransaccionesCentroAcopio: Clase para la ventana de anulación de transacciones.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from src.code.constantes import COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO
from src.code.anular_transaccion_code import (
    verificar_campos_anular_transaccion,
    obtener_transaccion_por_id,
    actualizar_saldo_estudiante,
    crear_transaccion_anulada,
)
from src.code.storage.anular_transaccion_storage import agregar_transaccion_anulada_archivo
from src.code.storage.ver_transacciones_storage import obtener_transacciones
from src.code.ver_transacciones_code import mostrar_transacciones_tabla, verificar_existencia_transacciones


class AnularTransaccionesCentroAcopio:
    """
    Clase para la ventana de anulación de transacciones de centros de acopio.

    Métodos:
    - __init__: Inicializa la ventana de anulación de transacciones.
    - actualizar_tabla: Actualiza la tabla de transacciones.
    - anular_transaccion: Anula una transacción específica.
    """

    def __init__(self, parent, id_funcionario):
        """
        Inicializa la ventana de anulación de transacciones.

        :param parent: Ventana padre.
        :type parent: tk.Tk
        :param id_funcionario: ID del funcionario.
        :type id_funcionario: str
        """
        self.parent = parent
        self.id_funcionario = id_funcionario
        self.json_file = obtener_transacciones()

        # Crear el contenedor para la tabla de transacciones
        self.tabla_frame = ttk.Frame(self.parent)
        self.tabla_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear y configurar la tabla de transacciones
        self.tabla = ttk.Treeview(self.tabla_frame, columns=COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO, show="headings")
        for col in COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO:
            self.tabla.heading(col, text=col.replace("_", " ").title())
        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Crear la barra de entrada para el ID de transacción
        self.entry_id_transaccion = ttk.Entry(self.parent)
        self.entry_id_transaccion.pack(pady=5)

        # Crear el botón de anular
        self.boton_anular = ttk.Button(self.parent, text="Anular", command=self.anular_transaccion)
        self.boton_anular.pack(pady=5)

        # Crear el botón de actualizar
        self.boton_actualizar = ttk.Button(self.parent, text="Actualizar", command=self.actualizar_tabla)
        self.boton_actualizar.pack(pady=5)

        # Cargar todas las transacciones al inicio
        self.actualizar_tabla()

    def actualizar_tabla(self):
        """
        Actualiza la tabla de transacciones.
        """

        # Limpiar la tabla antes de actualizar
        self.tabla.delete(*self.tabla.get_children())
        # Cargar las transacciones y actualizar la tabla
        transacciones = obtener_transacciones()
        verificar_existencia_transacciones(transacciones)
        mostrar_transacciones_tabla(self, transacciones)

    def anular_transaccion(self):
        """
        Anula una transacción específica.
        """
        id_transaccion = self.entry_id_transaccion.get()
        if not verificar_campos_anular_transaccion(id_transaccion):
            return
        transaccion_original = obtener_transaccion_por_id(id_transaccion)
        if not transaccion_original:
            return
        transaccion_anulada = crear_transaccion_anulada(transaccion_original)
        # Añadir la transacción anulada al archivo JSON
        agregar_transaccion_anulada_archivo(transaccion_anulada)
        actualizar_saldo_estudiante(transaccion_original["carnet"], transaccion_anulada["total"])
        self.actualizar_tabla()
        self.entry_id_transaccion.delete(0, tk.END)
        messagebox.showinfo("Éxito", "La transacción ha sido anulada correctamente")



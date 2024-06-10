"""
Este módulo contiene la clase VerTransaccionesCentroAcopio, que representa la interfaz para visualizar las transacciones en un centro de acopio.

Clases disponibles:
- VerTransaccionesCentroAcopio: Clase que representa la interfaz para visualizar las transacciones de un centro de acopio.
"""

import tkinter as tk
from tkinter import ttk
from src.code.constantes import COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO
from src.code.ver_transacciones_code import cargar_transacciones

class VerTransaccionesCentroAcopio:
    """
    Clase para la interfaz de visualización de transacciones en un centro de acopio.
    """

    def __init__(self, parent, id_funcionario):
        """
        Inicializa la interfaz de visualización de transacciones.

        Parámetros:
        - parent: El widget padre que contiene esta interfaz.
        - id_funcionario: El identificador del funcionario que maneja el centro de acopio.
        """
        self.parent = parent
        self.id_funcionario = id_funcionario

        # Crear el contenedor para la tabla de transacciones
        self.tabla_frame = ttk.Frame(self.parent)
        self.tabla_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear y configurar la tabla de transacciones
        self.tabla = ttk.Treeview(self.tabla_frame, columns=COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO, show="headings")
        self.tabla.heading("id_transaccion", text="ID")
        self.tabla.heading("carnet", text="Carnet")
        self.tabla.heading("sede", text="Sede")
        self.tabla.heading("fecha_hora", text="Fecha y Hora")
        self.tabla.heading("materiales", text="Materiales")
        self.tabla.heading("total", text="Total")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Crear el contenedor para los filtros
        self.filtrar_frame = ttk.Frame(self.parent)
        self.filtrar_frame.pack(padx=10, pady=10)

        # Añadir el campo de fecha de inicio
        ttk.Label(self.filtrar_frame, text="Fecha Inicio:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_inicio_var = tk.StringVar()
        self.fecha_inicio_entry = ttk.Entry(self.filtrar_frame, textvariable=self.fecha_inicio_var)
        self.fecha_inicio_entry.grid(row=0, column=1, padx=5, pady=5)

        # Añadir el campo de fecha de fin
        ttk.Label(self.filtrar_frame, text="Fecha Fin:").grid(row=0, column=2, padx=5, pady=5)
        self.fecha_fin_var = tk.StringVar()
        self.fecha_fin_entry = ttk.Entry(self.filtrar_frame, textvariable=self.fecha_fin_var)
        self.fecha_fin_entry.grid(row=0, column=3, padx=5, pady=5)

        # Añadir el botón de filtrar
        self.boton_filtrar = ttk.Button(self.filtrar_frame, text="Filtrar", command=self.filtrar_transacciones)
        self.boton_filtrar.grid(row=0, column=4, padx=5, pady=5)

        # Cargar todas las transacciones al inicio
        self.cargar_transacciones()

    def cargar_transacciones(self):
        """
        Carga todas las transacciones del centro de acopio en la tabla.
        """
        transacciones = cargar_transacciones(self.id_funcionario)
        print(transacciones)
        for transaccion in transacciones:
            self.tabla.insert("", "end", values=(
                transaccion["id_transaccion"], transaccion["carnet"], transaccion["sede"], transaccion["fecha_hora"],
                ', '.join([f"{m['nombre']} ({m['cantidad']})" for m in transaccion["materiales"]]), transaccion["total"]
            ))

    def filtrar_transacciones(self):
        """
        Filtra las transacciones según las fechas de inicio y fin proporcionadas por el usuario.
        """
        fecha_inicio = self.fecha_inicio_var.get()
        fecha_fin = self.fecha_fin_var.get()
        self.tabla.delete(*self.tabla.get_children())
        transacciones = cargar_transacciones(self.id_funcionario, fecha_inicio, fecha_fin)
        for transaccion in transacciones:
            self.tabla.insert("", "end", values=(
                transaccion["id_transaccion"], transaccion["carnet"], transaccion["sede"], transaccion["fecha_hora"],
                ', '.join([f"{m['nombre']} ({m['cantidad']})" for m in transaccion["materiales"]]), transaccion["total"]
            ))

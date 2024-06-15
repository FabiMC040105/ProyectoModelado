"""
Este módulo contiene la clase VerTransaccionesCentroAcopio, que representa la interfaz para visualizar las transacciones en un centro de acopio.

Clases disponibles:
- VerTransaccionesCentroAcopio: Clase que representa la interfaz para visualizar las transacciones de un centro de acopio.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from src.code.centro_acopio_code import obtener_centros_acopio_activos
from src.code.constantes import COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO
from src.code.ver_transacciones_code import obtener_transacciones_centro_acopio, verificar_existencia_transacciones, \
    mostrar_transacciones_tabla


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


        # Añadir la lista desplegable para seleccionar el centro de acopio
        ttk.Label(self.tabla_frame, text="Centro de Acopio:").grid(row=0, column=0, padx=5, pady=5)
        self.centro_acopio_var = tk.StringVar()
        self.centro_acopio_combobox = ttk.Combobox(self.tabla_frame, textvariable=self.centro_acopio_var)
        self.centro_acopio_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Obtener y cargar los centros de acopio activos en el combobox
        self.centros_acopio_activos = obtener_centros_acopio_activos()
        self.centro_acopio_combobox['values'] = [centro['id'] for centro in self.centros_acopio_activos]

        # Configurar el evento para actualizar transacciones cuando se selecciona un nuevo centro de acopio
        self.centro_acopio_combobox.bind("<<ComboboxSelected>>", self.cargar_transacciones)

        # Crear y configurar la tabla de transacciones
        self.tabla = ttk.Treeview(self.tabla_frame, columns=COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO, show="headings")
        self.tabla.heading("id_transaccion", text="ID")
        self.tabla.heading("carnet", text="Carnet")
        self.tabla.heading("sede", text="Sede")
        self.tabla.heading("fecha_hora", text="Fecha y Hora")
        self.tabla.heading("materiales", text="Materiales")
        self.tabla.heading("total", text="Total")
        self.tabla.grid(row=1, column=0, columnspan=2, sticky='nsew')

        # Configurar la tabla para expandirse con el contenedor
        self.tabla_frame.grid_rowconfigure(1, weight=1)
        self.tabla_frame.grid_columnconfigure(0, weight=1)

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

    def cargar_transacciones(self, event=None):
        """
        Carga todas las transacciones del centro de acopio en la tabla.
        """
        #self.centro_acopio_var.set("CCA106")
        centro_acopio_id = self.centro_acopio_var.get()
        self.centro_acopio_var.set("CCA106")
        transacciones = obtener_transacciones_centro_acopio(centro_acopio_id)

        self.tabla.delete(*self.tabla.get_children())
        verificar_existencia_transacciones(transacciones)

        mostrar_transacciones_tabla(self, transacciones)

    def filtrar_transacciones(self):
        """
        Filtra las transacciones según las fechas de inicio y fin proporcionadas por el usuario.
        """
        self.fecha_inicio_var.set("2025-05-27")
        self.fecha_fin_var.set("2025-05-27")
        fecha_inicio = self.fecha_inicio_var.get()
        fecha_fin = self.fecha_fin_var.get()
        centro_acopio_id = self.centro_acopio_var.get()
        self.centro_acopio_var.set("CCA106")
        self.tabla.delete(*self.tabla.get_children())
        transacciones = obtener_transacciones_centro_acopio(centro_acopio_id, fecha_inicio, fecha_fin)
        verificar_existencia_transacciones(transacciones)
        mostrar_transacciones_tabla(self, transacciones)


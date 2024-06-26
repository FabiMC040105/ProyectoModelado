"""
Este módulo contiene la clase CentroAcopioApp, que gestiona la interfaz gráfica y las operaciones de creación de centros de acopio.

Clase disponible:
- CentroAcopioApp: Clase que gestiona la interfaz gráfica y las operaciones de creación de centros de acopio.
"""

import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

from src.code.centro_acopio_code import obtener_centros_acopio, agregar_centro_acopio_archivo
from src.code.sede_code import obtener_sedes_activas


class CentroAcopioApp:
    """
    Clase para la aplicación de gestión de centros de acopio.
    """

    def __init__(self, root):
        """
        Inicializa la aplicación.

        Parámetros:
        - root: El objeto raíz de la interfaz gráfica.
        """
        self.root = root

        # Variables para almacenar los datos del centro de acopio
        self.sede_var = tk.StringVar()
        self.telefono_var = tk.StringVar()
        self.ubicacion_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.codigo_var = tk.StringVar()

        # Crear frame para formulario de creación de centro de acopio
        form_frame = ttk.Frame(self.root)
        form_frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(form_frame, text="Sede:").grid(row=0, column=0, sticky="w")
        sedes = obtener_sedes_activas()  # Obtener lista de sedes activas desde la función obtener_sedes_activas
        self.sede_combobox = ttk.Combobox(form_frame, textvariable=self.sede_var, values=sedes)
        self.sede_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Número Telefónico:").grid(row=1, column=0, sticky="w")
        self.telefono_entry = ttk.Entry(form_frame, textvariable=self.telefono_var)
        self.telefono_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Ubicación:").grid(row=2, column=0, sticky="w")
        self.ubicacion_entry = ttk.Entry(form_frame, textvariable=self.ubicacion_var)
        self.ubicacion_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Estado:").grid(row=3, column=0, sticky="w")
        self.estado_combobox = ttk.Combobox(form_frame, textvariable=self.estado_var, values=["Activo", "Inactivo"])
        self.estado_combobox.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Código ID:").grid(row=4, column=0, sticky="w")
        self.codigo_entry = ttk.Entry(form_frame, textvariable=self.codigo_var)
        self.codigo_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón para crear el nuevo centro de acopio
        ttk.Button(form_frame, text="Crear Centro de Acopio", command=self.crear_centro_acopio).grid(row=5, columnspan=2, padx=5, pady=10)

        # Crear frame para la tabla de centros de acopio
        self.tabla_frame = ttk.Frame(self.root)
        self.tabla_frame.grid(row=1, column=0, padx=10, pady=10)

        self.crear_tabla()

    def crear_tabla(self):
        """
        Crea la tabla de centros de acopio.
        """
        # Crear tabla
        columnas = ("Sede", "Número Telefónico", "Ubicación", "Estado")
        self.tabla = ttk.Treeview(self.tabla_frame, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, minwidth=0, width=100)

        self.tabla.pack(fill=tk.BOTH, expand=True)

        self.cargar_centros_acopio()

    def cargar_centros_acopio(self):
        """
        Carga los centros de acopio en la tabla.
        """
        centros_acopio = obtener_centros_acopio()  # Obtener lista de centros de acopio desde la función obtener_centros_acopio

        for centro_acopio in centros_acopio:
            self.tabla.insert("", "end", values=(centro_acopio["sede"], centro_acopio["telefono"], centro_acopio["ubicacion"], centro_acopio["estado"]))

    def crear_centro_acopio(self):
        """
        Crea un nuevo centro de acopio.
        """
        sede = self.sede_var.get()
        telefono = self.telefono_var.get()
        ubicacion = self.ubicacion_var.get()
        estado = self.estado_var.get()
        codigo = self.codigo_var.get()

        if not self.validarcampos(ubicacion, estado, telefono, codigo):
            return

        # Generar ID único para el centro de acopio
        centro_acopio_id = codigo

        # Agregar nuevo centro de acopio al archivo JSON
        agregar_centro_acopio_archivo(centro_acopio_id, sede, telefono, ubicacion, estado)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Centro de acopio creado exitosamente.")

        # Limpiar los campos de entrada
        self.sede_var.set("")
        self.telefono_var.set("")
        self.ubicacion_var.set("")
        self.estado_var.set("")
        self.codigo_var.set("")

        # Recargar la tabla de centros de acopio
        self.tabla.delete(*self.tabla.get_children())
        self.cargar_centros_acopio()

    def validarcampos(self, ubicacion, estado, telefono, codigo):
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

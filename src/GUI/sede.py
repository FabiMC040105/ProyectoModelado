"""
Este módulo contiene la clase SedeApp, que gestiona la interfaz gráfica y las operaciones de creación de sedes.

Clase disponible:
- SedeApp: Clase que gestiona la interfaz gráfica y las operaciones de creación de sedes.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from src.code.constantes import JSON_SEDE, COLUMNAS_TABLA_SEDE, PREFIJO_SEDE
from src.code.funciones import generar_id_unico
from src.code.sede_code import obtener_sedes, agregar_sede_archivo


class SedeApp:
    """
    Clase para la aplicación de gestión de sedes.
    """

    def __init__(self, root):
        """
        Inicializa la aplicación.

        Parámetros:
        - root: El objeto raíz de la interfaz gráfica.
        """
        self.root = root
        self.prefijo = "S-"
        # Variables para almacenar los datos de la nueva sede
        self.nombre_var = tk.StringVar()
        self.ubicacion_var = tk.StringVar()
        self.estado_var = tk.StringVar()
        self.telefono_var = tk.StringVar()

        # Crear frame para formulario de creación de sede
        form_frame = ttk.Frame(self.root)
        form_frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(form_frame, text="Nombre de la Sede:").grid(row=0, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(form_frame, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Ubicación:").grid(row=1, column=0, sticky="w")
        self.ubicacion_combobox = ttk.Combobox(form_frame, textvariable=self.ubicacion_var, values=["San José", "Alajuela", "Cartago", "Heredia", "Guanacaste", "Puntarenas", "Limón"])
        self.ubicacion_combobox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Estado:").grid(row=2, column=0, sticky="w")
        self.estado_combobox = ttk.Combobox(form_frame, textvariable=self.estado_var, values=["Activo", "Inactivo"])
        self.estado_combobox.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Número de Teléfono:").grid(row=3, column=0, sticky="w")
        self.telefono_entry = ttk.Entry(form_frame, textvariable=self.telefono_var)
        self.telefono_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botón para crear la nueva sede
        ttk.Button(form_frame, text="Crear Sede", command=self.crear_sede).grid(row=4, columnspan=2, padx=5, pady=10)

        # Crear frame para la tabla de sedes
        self.tabla_frame = ttk.Frame(self.root)
        self.tabla_frame.grid(row=1, column=0, padx=10, pady=10)

        self.crear_tabla()

    def crear_tabla(self):
        """
        Crea la tabla de sedes.
        """
        # Crear tabla
        self.tabla = ttk.Treeview(self.tabla_frame, columns=COLUMNAS_TABLA_SEDE, show="headings")

        for col in COLUMNAS_TABLA_SEDE:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, minwidth=0, width=100)

        self.tabla.pack(fill=tk.BOTH, expand=True)

        self.cargar_sedes()

    def cargar_sedes(self):
        """
        Carga las sedes en la tabla.
        """

        sedes = obtener_sedes()

        for sede in sedes:
            self.tabla.insert("", "end", values=(sede["nombre"], sede["ubicacion"], sede["estado"], sede["telefono"]))

    def crear_sede(self):
        """
        Crea una nueva sede.
        """
        nombre = self.nombre_var.get()
        ubicacion = self.ubicacion_var.get()
        estado = self.estado_var.get()
        telefono = self.telefono_var.get()
        if not self.validarcampos( nombre, ubicacion, estado, telefono):
            return
        # Generar ID único para la sede
        sede_id = generar_id_unico(PREFIJO_SEDE)

        # Agregar nueva sede al archivo JSON
        agregar_sede_archivo(sede_id, nombre, ubicacion, estado, telefono)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Sede creada exitosamente.")

        # Limpiar los campos de entrada
        self.nombre_var.set("")
        self.ubicacion_var.set("")
        self.estado_var.set("")
        self.telefono_var.set("")

        # Recargar la tabla de sedes
        self.tabla.delete(*self.tabla.get_children())
        self.cargar_sedes()

    def validarcampos(self, nombre, ubicacion, estado, telefono):
        sedes = obtener_sedes()
        nombrevalido = True
        for sede in sedes:
            if sede["nombre"].upper() == nombre.upper():
                nombrevalido = False
        if not nombrevalido:
            messagebox.showerror("Error", "Ya existe un sede con ese nombre")
            return False
        if not nombre or not ubicacion or not estado or not telefono:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return False

        try:
            telefono = int(telefono)
        except ValueError:
            messagebox.showerror("Error", "El número de teléfono debe ser numérico.")
            return False

        if len(str(telefono)) != 8:
            messagebox.showerror("Error", "El número de teléfono debe tener 8 dígitos.")
            return False

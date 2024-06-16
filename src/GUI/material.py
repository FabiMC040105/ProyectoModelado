"""
Este módulo contiene la clase MaterialReciclajeApp, que gestiona la interfaz gráfica y las operaciones de creación de materiales de reciclaje.

Clase disponible:
- MaterialReciclajeApp: Clase que gestiona la interfaz gráfica y las operaciones de creación de materiales de reciclaje.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from src.code.constantes import PREFIJO_MATERIAL, COLUMNAS_TABLA_MATERIAL

from src.code.funciones import generar_id_unico
from src.code.material_code import cargar_materiales, limpiar_formulario_material, validar_campos_material
from src.code.storage.material_storage import agregar_material_archivo


class MaterialReciclajeApp:
    """
    Clase para la aplicación de gestión de materiales de reciclaje.
    """

    def __init__(self, root):
        """
        Inicializa la aplicación.

        Parámetros:
        - root: El objeto raíz de la interfaz gráfica.
        """
        self.root = root
        self.prefijo = PREFIJO_MATERIAL
        # Variables para almacenar los datos del nuevo material
        self.nombre_var = tk.StringVar()
        self.unidad_var = tk.StringVar()
        self.valor_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()

        # Crear frame para formulario de creación de materiales
        form_frame = ttk.Frame(self.root)
        form_frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(form_frame, text="Nombre del Material:").grid(row=0, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(form_frame, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Unidad:").grid(row=1, column=0, sticky="w")
        self.unidad_combobox = ttk.Combobox(form_frame, textvariable=self.unidad_var, values=["Kilogramo", "Litro", "Unidad"])
        self.unidad_combobox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Valor Unitario (Tec-Colones):").grid(row=2, column=0, sticky="w")
        self.valor_entry = ttk.Entry(form_frame, textvariable=self.valor_var)
        self.valor_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Descripción:").grid(row=3, column=0, sticky="w")
        self.descripcion_entry = ttk.Entry(form_frame, textvariable=self.descripcion_var)
        self.descripcion_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botón para crear el nuevo material
        ttk.Button(form_frame, text="Crear Material", command=self.crear_material).grid(row=4, columnspan=2, padx=5, pady=10)

        # Crear frame para la tabla de materiales
        self.tabla_frame = ttk.Frame(self.root)
        self.tabla_frame.grid(row=1, column=0, padx=10, pady=10)

        self.crear_tabla()

    def crear_tabla(self):
        """
        Crea la tabla de materiales.
        """
        # Crear tabla
        columnas = COLUMNAS_TABLA_MATERIAL
        self.tabla = ttk.Treeview(self.tabla_frame, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, minwidth=0, width=100)

        self.tabla.pack(fill=tk.BOTH, expand=True)

        cargar_materiales(self)

    def crear_material(self):
        """
        Crea un nuevo material.
        """

        nombre = self.nombre_var.get()
        unidad = self.unidad_var.get()
        valor = self.valor_var.get()
        descripcion = self.descripcion_var.get()
        """
        print("Nombre: "+nombre)
        print("Unidad: " + unidad)
        print("Valor: " + valor)
        """
        if not validar_campos_material(nombre, unidad, valor, descripcion):
            return

        # Generar ID único para el material
        material_id = generar_id_unico(self.prefijo)

        # Agregar nuevo material al archivo JSON
        agregar_material_archivo(material_id, nombre, unidad, valor, descripcion)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Material creado exitosamente.")

        # Limpiar los campos de entrada
        limpiar_formulario_material(self)

        # Recargar la tabla de materiales
        self.tabla.delete(*self.tabla.get_children())
        cargar_materiales(self)



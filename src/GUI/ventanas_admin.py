"""
Este módulo contiene la clase AppPrincipalAdmin, que representa la interfaz principal de la aplicación de gestión de reciclaje.

Clase disponible:
- AppPrincipalAdmin: Clase que representa la interfaz principal de la aplicación de gestión de reciclaje.
"""

import tkinter as tk
from tkinter import ttk
from src.GUI.material import MaterialReciclajeApp
from src.GUI.sede import SedeApp
from src.GUI.centro_acopio import CentroAcopioApp

class AppPrincipalAdmin:
    """
    Clase para la interfaz principal de la aplicación de gestión de reciclaje.
    """

    def __init__(self, root):
        """
        Inicializa la aplicación principal.

        Parámetros:
        - root: El objeto raíz de la interfaz gráfica.
        """
        self.root = root
        self.root.title("Gestión de Reciclaje")

        # Crear el contenedor principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el panel lateral con los botones
        self.panel_lateral = ttk.Frame(main_frame)
        self.panel_lateral.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.boton_material = ttk.Button(self.panel_lateral, text="Crear Material", command=self.cargar_material)
        self.boton_material.pack(pady=5)

        self.boton_sede = ttk.Button(self.panel_lateral, text="Crear Sede", command=self.cargar_sede)
        self.boton_sede.pack(pady=5)

        self.boton_centro_acopio = ttk.Button(self.panel_lateral, text="Crear Centro de Acopio", command=self.cargar_centro_acopio)
        self.boton_centro_acopio.pack(pady=5)

        # Crear el área principal donde se cargarán los widgets
        self.area_principal = ttk.Frame(main_frame)
        self.area_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cargar_material(self):
        """
        Carga la interfaz para la creación de materiales.
        """
        self.limpiar_area_principal()
        MaterialReciclajeApp(self.area_principal)

    def cargar_sede(self):
        """
        Carga la interfaz para la creación de sedes.
        """
        self.limpiar_area_principal()
        SedeApp(self.area_principal)

    def cargar_centro_acopio(self):
        """
        Carga la interfaz para la creación de centros de acopio.
        """
        self.limpiar_area_principal()
        CentroAcopioApp(self.area_principal)

    def limpiar_area_principal(self):
        """
        Limpia el área principal eliminando todos los widgets.
        """
        for widget in self.area_principal.winfo_children():
            widget.destroy()

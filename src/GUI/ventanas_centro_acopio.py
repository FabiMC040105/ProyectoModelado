"""
Este módulo contiene la clase AppPrincipalCentroAcopio, que representa la interfaz principal para la gestión de un centro de acopio en la aplicación de reciclaje.

Clases disponibles:
- AppPrincipalCentroAcopio: Clase que representa la interfaz principal para la gestión de un centro de acopio.
"""

import tkinter as tk
from tkinter import ttk
from src.GUI.cambiar_material import CambiarMaterialApp
from src.GUI.ver_transacciones import VerTransaccionesCentroAcopio

class AppPrincipalCentroAcopio:
    """
    Clase para la interfaz principal de la gestión de un centro de acopio en la aplicación de reciclaje.
    """

    def __init__(self, root, id_funcionario):
        """
        Inicializa la aplicación principal del centro de acopio.

        Parámetros:
        - root: El objeto raíz de la interfaz gráfica.
        - id_funcionario: El identificador del funcionario que maneja el centro de acopio.
        """
        self.root = root
        self.id_funcionario = id_funcionario
        self.root.title("Centro de Acopio - Gestión de Reciclaje")

        # Crear el contenedor principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el panel lateral con los botones
        self.panel_lateral = ttk.Frame(main_frame)
        self.panel_lateral.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.boton_cambiar_material = ttk.Button(self.panel_lateral, text="Cambiar Material", command=self.cargar_cambiar_material)
        self.boton_cambiar_material.pack(pady=5)

        self.boton_ver_transacciones = ttk.Button(self.panel_lateral, text="Ver Transacciones", command=self.cargar_ver_transacciones)
        self.boton_ver_transacciones.pack(pady=5)

        # Crear el área principal donde se cargarán los widgets
        self.area_principal = ttk.Frame(main_frame)
        self.area_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cargar_cambiar_material(self):
        """
        Carga la interfaz para cambiar materiales en el centro de acopio.
        """
        self.limpiar_area_principal()
        CambiarMaterialApp(self.area_principal, self.id_funcionario)

    def cargar_ver_transacciones(self):
        """
        Carga la interfaz para ver las transacciones realizadas en el centro de acopio.
        """
        self.limpiar_area_principal()
        VerTransaccionesCentroAcopio(self.area_principal, self.id_funcionario)

    def limpiar_area_principal(self):
        """
        Limpia el área principal eliminando todos los widgets.
        """
        for widget in self.area_principal.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppPrincipalCentroAcopio(root, "CCA106")
    root.mainloop()


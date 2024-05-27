import tkinter as tk
from tkinter import ttk
from src.GUI.cambiar_material import CambiarMaterialApp
from src.GUI.ver_transacciones import VerTransaccionesCentroAcopio

class AppPrincipalCentroAcopio:
    def __init__(self, root, id_funcionario):
        self.root = root
        self.id_funcionario = id_funcionario
        self.root.title("Centro de Acopio - Gestión de Reciclaje")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.panel_lateral = ttk.Frame(main_frame)
        self.panel_lateral.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.boton_cambiar_material = ttk.Button(self.panel_lateral, text="Cambiar Material", command=self.cargar_cambiar_material)
        self.boton_cambiar_material.pack(pady=5)

        self.boton_ver_transacciones = ttk.Button(self.panel_lateral, text="Ver Transacciones", command=self.cargar_ver_transacciones)
        self.boton_ver_transacciones.pack(pady=5)

        self.area_principal = ttk.Frame(main_frame)
        self.area_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cargar_cambiar_material(self):
        self.limpiar_area_principal()
        CambiarMaterialApp(self.area_principal, self.id_funcionario)

    def cargar_ver_transacciones(self):
        self.limpiar_area_principal()
        VerTransaccionesCentroAcopio(self.area_principal, self.id_funcionario)

    def limpiar_area_principal(self):
        for widget in self.area_principal.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AppPrincipalCentroAcopio(root, "CCA106")
    root.mainloop()

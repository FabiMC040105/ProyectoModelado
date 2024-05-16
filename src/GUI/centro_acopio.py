import tkinter as tk
from tkinter import ttk

class CentroAcopioApp:
    def __init__(self, root):
        self.root = root

        # Crear frame
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiqueta con el nombre "Crear Centro de Acopio"
        ttk.Label(frame, text="Crear Centro de Acopio").grid(row=0, column=0, sticky="w")

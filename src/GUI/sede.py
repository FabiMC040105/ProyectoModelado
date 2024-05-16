import tkinter as tk
from tkinter import ttk

class SedeApp:
    def __init__(self, root):
        self.root = root

        # Crear frame
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiqueta con el nombre "Crear Sede"
        ttk.Label(frame, text="Crear Sede").grid(row=0, column=0, sticky="w")

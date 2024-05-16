import tkinter as tk
from tkinter import ttk, messagebox
from src.code.funciones import generar_id_unico, agregar_material_archivo
import os

class MaterialReciclajeApp:
    def __init__(self, root):
        self.root = root

        # Variables para almacenar los datos del nuevo material
        self.nombre_var = tk.StringVar()
        self.unidad_var = tk.StringVar()
        self.valor_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()

        # Crear frame
        frame = ttk.Frame(self.root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Etiquetas y campos de entrada
        ttk.Label(frame, text="Nombre del Material:").grid(row=0, column=0, sticky="w")
        self.nombre_entry = ttk.Entry(frame, textvariable=self.nombre_var)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Unidad:").grid(row=1, column=0, sticky="w")
        self.unidad_combobox = ttk.Combobox(frame, textvariable=self.unidad_var, values=["Kilogramo", "Litro", "Unidad"])
        self.unidad_combobox.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Valor Unitario (Tec-Colones):").grid(row=2, column=0, sticky="w")
        self.valor_entry = ttk.Entry(frame, textvariable=self.valor_var)
        self.valor_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Descripción:").grid(row=3, column=0, sticky="w")
        self.descripcion_entry = ttk.Entry(frame, textvariable=self.descripcion_var)
        self.descripcion_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botón para crear el nuevo material
        ttk.Button(frame, text="Crear Material", command=self.crear_material).grid(row=4, columnspan=2, padx=5, pady=10)

    def crear_material(self):
        nombre = self.nombre_var.get()
        unidad = self.unidad_var.get()
        valor = self.valor_var.get()
        descripcion = self.descripcion_var.get()

        if not nombre or not unidad or not valor:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        try:
            valor = float(valor)

        except ValueError:
            messagebox.showerror("Error", "El valor unitario debe ser numérico.")
            return

        if valor < 1 or valor > 1000:
            messagebox.showerror("Error", "El valor unitario debe ser mayor a 0 y menor a 1000.")
            return

        if len(nombre) < 5 or len(nombre) > 30:
            messagebox.showerror("Error", "El nombre del material debe tener entre 5 y 30 caracteres.")
            return

        if len(descripcion) > 1000:
            messagebox.showerror("Error", "La descripción debe tener como máximo 1000 caracteres.")
            return

        # Generar ID único para el material
        material_id = generar_id_unico()

        # Agregar nuevo material al archivo JSON
        archivo_materiales = os.path.join(os.path.dirname(__file__), "..", "instrucciones.json")
        agregar_material_archivo(archivo_materiales, material_id, nombre, unidad, valor, descripcion)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Material creado exitosamente.")

        # Limpiar los campos de entrada
        self.nombre_var.set("")
        self.unidad_var.set("")
        self.valor_var.set("")
        self.descripcion_var.set("")
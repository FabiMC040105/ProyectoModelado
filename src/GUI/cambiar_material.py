import tkinter as tk
from tkinter import ttk, messagebox
from src.code.cambiar_material_code import *

from src.code.cambiar_material_code import validar_cantidad_material, obtener_detalles_material, calcular_monto, \
    limpiar_formulario, registrar_transaccion
from src.code.sede_code import obtener_sedes_activas


class CambiarMaterialApp:
    def __init__(self, parent, id_funcionario):
        self.parent = parent
        self.id_funcionario = id_funcionario

        form_frame = ttk.Frame(self.parent)
        form_frame.pack(padx=10, pady=10)

        self.carnet_var = tk.StringVar()
        ttk.Label(form_frame, text="Carnet del Estudiante:").grid(row=0, column=0, sticky="w")
        self.carnet_entry = ttk.Entry(form_frame, textvariable=self.carnet_var)
        self.carnet_entry.grid(row=0, column=1, padx=5, pady=5)

        self.sede_var = tk.StringVar()
        ttk.Label(form_frame, text="Sede:").grid(row=1, column=0, sticky="w")
        sedes = obtener_sedes_activas()
        self.sede_combobox = ttk.Combobox(form_frame, textvariable=self.sede_var, values=sedes)
        self.sede_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.material_var = tk.StringVar()
        ttk.Label(form_frame, text="Material:").grid(row=2, column=0, sticky="w")
        materiales = obtener_nombre_materiales()
        self.material_combobox = ttk.Combobox(form_frame, textvariable=self.material_var, values=materiales)
        self.material_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.material_combobox.bind("<<ComboboxSelected>>", self.mostrar_detalles_material)

        self.detalle_var = tk.StringVar()
        ttk.Label(form_frame, text="Detalles:").grid(row=3, column=0, sticky="w")
        self.detalle_label = ttk.Label(form_frame, textvariable=self.detalle_var)
        self.detalle_label.grid(row=3, column=1, padx=5, pady=5)

        self.cantidad_var = tk.StringVar()
        ttk.Label(form_frame, text="Cantidad:").grid(row=4, column=0, sticky="w")
        self.cantidad_entry = ttk.Entry(form_frame, textvariable=self.cantidad_var)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        self.boton_agregar = ttk.Button(form_frame, text="Agregar Material", command=self.agregar_material)
        self.boton_agregar.grid(row=5, columnspan=2, pady=5)

        self.tabla_frame = ttk.Frame(self.parent)
        self.tabla_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tabla = ttk.Treeview(self.tabla_frame, columns=("nombre", "valor", "unidad", "cantidad", "monto"), show="headings")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("valor", text="Valor")
        self.tabla.heading("unidad", text="Unidad")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.heading("monto", text="Monto")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        self.boton_realizar_cambio = ttk.Button(self.parent, text="Realizar Cambio", command=self.realizar_cambio)
        self.boton_realizar_cambio.pack(pady=10)

    def mostrar_detalles_material(self, event):
        nombre_material = self.material_var.get()
        detalles = obtener_detalles_material(nombre_material)
        self.detalle_var.set(f"Unidad: {detalles['unidad']}, Valor: {detalles['valor']}, Descripción: {detalles['descripcion']}")

    def agregar_material(self):
        nombre = self.material_var.get()
        cantidad = self.cantidad_var.get()
        if not validar_cantidad_material(cantidad, nombre):
            return
        material_info = obtener_detalles_material(nombre)
        monto = calcular_monto(material_info['valor'], cantidad)
        self.tabla.insert("", "end", values=(nombre, material_info['valor'], material_info['unidad'], cantidad, monto))
        limpiar_material_formulario(self)

    def realizar_cambio(self):
        carnet = self.carnet_var.get()
        sede = self.sede_var.get()
        materiales = []
        total = 0
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            materiales.append({
                "nombre": values[0],
                "cantidad": values[3],
                "valor": values[1]
            })
            total += float(values[4])

        if registrar_transaccion(carnet, self.id_funcionario, sede, materiales, total):
            messagebox.showinfo("Éxito", "Transacción realizada exitosamente.")
            self.tabla.delete(*self.tabla.get_children())
        else:
            messagebox.showerror("Error", "Hubo un problema al registrar la transacción.")
        limpiar_formulario(self)
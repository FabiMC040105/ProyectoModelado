import tkinter as tk
from tkinter import ttk

from src.code.constantes import COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO
from src.code.ver_transacciones_code import cargar_transacciones

class VerTransaccionesCentroAcopio:
    def __init__(self, parent, id_funcionario):
        self.parent = parent
        self.id_funcionario = id_funcionario

        self.tabla_frame = ttk.Frame(self.parent)
        self.tabla_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tabla = ttk.Treeview(self.tabla_frame, columns=COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO, show="headings")
        self.tabla.heading("id_transaccion", text="ID")
        self.tabla.heading("carnet", text="Carnet")
        self.tabla.heading("sede", text="Sede")
        self.tabla.heading("fecha_hora", text="Fecha y Hora")
        self.tabla.heading("materiales", text="Materiales")
        self.tabla.heading("total", text="Total")
        self.tabla.pack(fill=tk.BOTH, expand=True)

        self.filtrar_frame = ttk.Frame(self.parent)
        self.filtrar_frame.pack(padx=10, pady=10)

        ttk.Label(self.filtrar_frame, text="Fecha Inicio:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_inicio_var = tk.StringVar()
        self.fecha_inicio_entry = ttk.Entry(self.filtrar_frame, textvariable=self.fecha_inicio_var)
        self.fecha_inicio_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.filtrar_frame, text="Fecha Fin:").grid(row=0, column=2, padx=5, pady=5)
        self.fecha_fin_var = tk.StringVar()
        self.fecha_fin_entry = ttk.Entry(self.filtrar_frame, textvariable=self.fecha_fin_var)
        self.fecha_fin_entry.grid(row=0, column=3, padx=5, pady=5)

        self.boton_filtrar = ttk.Button(self.filtrar_frame, text="Filtrar", command=self.filtrar_transacciones)
        self.boton_filtrar.grid(row=0, column=4, padx=5, pady=5)

        self.cargar_transacciones()

    def cargar_transacciones(self):
        transacciones = cargar_transacciones(self.id_funcionario)
        for transaccion in transacciones:
            self.tabla.insert("", "end", values=(
                transaccion["id_transaccion"], transaccion["carnet"], transaccion["sede"], transaccion["fecha_hora"],
                ', '.join([f"{m['nombre']} ({m['cantidad']})" for m in transaccion["materiales"]]), transaccion["total"]
            ))

    def filtrar_transacciones(self):
        fecha_inicio = self.fecha_inicio_var.get()
        fecha_fin = self.fecha_fin_var.get()
        self.tabla.delete(*self.tabla.get_children())
        transacciones = cargar_transacciones(self.id_funcionario, fecha_inicio, fecha_fin)
        for transaccion in transacciones:
            self.tabla.insert("", "end", values=(
                transaccion["id_transaccion"], transaccion["carnet"], transaccion["sede"], transaccion["fecha_hora"],
                ', '.join([f"{m['nombre']} ({m['cantidad']})" for m in transaccion["materiales"]]), transaccion["total"]
            ))

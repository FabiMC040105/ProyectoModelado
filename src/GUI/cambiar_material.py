"""
Este módulo contiene la clase CambiarMaterialApp, que gestiona la interfaz gráfica y las operaciones de cambio de material.

Clase disponible:
- CambiarMaterialApp: Clase que gestiona la interfaz gráfica y las operaciones de cambio de material.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from src.code.cambiar_material_code import obtener_detalles_material, calcular_monto, obtener_nombre_materiales, \
    validar_campos_material, limpiar_formulario_cambiar_material, cacular_monto_total_cambio, validar_campos_transacción
from src.code.centro_acopio_code import obtener_centros_acopio_activos
from src.code.storage.cambiar_material_storage import registrar_transaccion


class CambiarMaterialApp:
    """
    Clase para la aplicación de cambio de material.
    """

    def __init__(self, parent, id_funcionario):
        """
        Inicializa la aplicación.

        Parámetros:
        - parent: El objeto raíz de la interfaz gráfica.
        - id_funcionario: El ID del funcionario que realiza el cambio de material.
        """
        self.parent = parent
        self.id_funcionario = id_funcionario

        # Crear frame para el formulario
        form_frame = ttk.Frame(self.parent)
        form_frame.pack(padx=10, pady=10)

        # Variables de control para los campos de entrada
        self.carnet_var = tk.StringVar()
        self.sede_var = tk.StringVar()
        self.material_var = tk.StringVar()
        self.detalle_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()

        # Campo de entrada para el carnet del estudiante
        ttk.Label(form_frame, text="Carnet del Estudiante:").grid(row=0, column=0, sticky="w")
        self.carnet_entry = ttk.Entry(form_frame, textvariable=self.carnet_var)
        self.carnet_entry.grid(row=0, column=1, padx=5, pady=5)



        # Añadir la lista desplegable para seleccionar el centro de acopio
        ttk.Label(form_frame, text="Centro de Acopio:").grid(row=1, column=0, padx=5, pady=5)
        self.centro_acopio_var = tk.StringVar()
        self.centro_acopio_combobox = ttk.Combobox(form_frame, textvariable=self.centro_acopio_var)
        self.centro_acopio_combobox.grid(row=1, column=1, padx=5, pady=5)

        # Obtener y cargar los centros de acopio activos en el combobox
        self.centros_acopio_activos = obtener_centros_acopio_activos()
        self.centro_acopio_combobox['values'] = [centro['id'] for centro in self.centros_acopio_activos]

        # ComboBox para seleccionar el material
        ttk.Label(form_frame, text="Material:").grid(row=2, column=0, sticky="w")
        materiales = obtener_nombre_materiales()
        self.material_combobox = ttk.Combobox(form_frame, textvariable=self.material_var, values=materiales)
        self.material_combobox.grid(row=2, column=1, padx=5, pady=5)
        self.material_combobox.bind("<<ComboboxSelected>>", self.mostrar_detalles_material)

        # Label para mostrar los detalles del material seleccionado
        ttk.Label(form_frame, text="Detalles:").grid(row=3, column=0, sticky="w")
        self.detalle_label = ttk.Label(form_frame, textvariable=self.detalle_var)
        self.detalle_label.grid(row=3, column=1, padx=5, pady=5)

        # Campo de entrada para la cantidad del material
        ttk.Label(form_frame, text="Cantidad:").grid(row=4, column=0, sticky="w")
        self.cantidad_entry = ttk.Entry(form_frame, textvariable=self.cantidad_var)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón para agregar el material a la lista de transacción
        self.boton_agregar = ttk.Button(form_frame, text="Agregar Material", command=self.agregar_material)
        self.boton_agregar.grid(row=5, columnspan=2, pady=5)

        # Frame para la tabla que muestra los materiales agregados
        self.tabla_frame = ttk.Frame(self.parent)
        self.tabla_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Configurar la tabla para mostrar los materiales
        self.tabla = ttk.Treeview(self.tabla_frame, columns=("nombre", "valor", "unidad", "cantidad", "monto"), show="headings")
        for col in ("nombre", "valor", "unidad", "cantidad", "monto"):
            self.tabla.heading(col, text=col.capitalize())
        self.tabla.pack(fill=tk.BOTH, expand=True)

        # Botón para realizar el cambio de material
        self.boton_realizar_cambio = ttk.Button(self.parent, text="Realizar Cambio", command=self.realizar_cambio)
        self.boton_realizar_cambio.pack(pady=10)

    def mostrar_detalles_material(self, event):
        """
        Muestra los detalles del material seleccionado en el ComboBox.
        """
        nombre_material = self.material_var.get()
        print("nombre material: "+ nombre_material)
        detalles = obtener_detalles_material(nombre_material)
        print("detalles: ")
        print(detalles)
        self.detalle_var.set(f"Unidad: {detalles['unidad']}, Valor: {detalles['valor']}, Descripción: {detalles['descripcion']}")

    def agregar_material(self):
        """
        Agrega el material seleccionado y su cantidad a la tabla de materiales.
        """
        nombre = self.material_var.get()
        cantidad = self.cantidad_var.get()
        nombre = "carton"
        cantidad = 15
        if not validar_campos_material(nombre, cantidad):
            return
        material_info = obtener_detalles_material(nombre)
        monto = calcular_monto(material_info['valor'], cantidad)
        self.tabla.insert("", "end", values=(nombre, material_info['valor'], material_info['unidad'], cantidad, monto))
        limpiar_formulario_cambiar_material(self)

    def realizar_cambio(self):
        """
        Realiza la transacción de cambio de material.
        """
        carnet = self.carnet_var.get()
        carnet = "estudiante@tec.ac.cr"
        centro = self.centro_acopio_var.get()
        centro = "CCA106"
        materiales = []
        lista_de_totales = []
        for item in self.tabla.get_children():
            values = self.tabla.item(item, "values")
            materiales.append({
                "nombre": values[0],
                "cantidad": values[3],
                "valor": values[1]
            })
            lista_de_totales.append(values[4])
        total = cacular_monto_total_cambio(lista_de_totales)
        if not validar_campos_transacción(materiales, centro, carnet):
            return
        if registrar_transaccion(carnet, self.id_funcionario, centro, materiales, total):
            messagebox.showinfo("Éxito", "Transacción realizada exitosamente.")
            self.tabla.delete(*self.tabla.get_children())
        else:
            messagebox.showerror("Error", "Hubo un problema al registrar la transacción.")
        limpiar_formulario_cambiar_material(self)

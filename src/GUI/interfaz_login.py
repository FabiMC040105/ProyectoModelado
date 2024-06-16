"""
Este módulo proporciona la interfaz gráfica para el inicio de sesión.

Funciones disponibles:
- iniciar_sesion: Verifica las credenciales del usuario y abre la ventana correspondiente según el rol del usuario.

Dependencias:
- tkinter: Para crear la interfaz gráfica.
- tkinter.messagebox: Para mostrar mensajes de información y error.
- src.code.storage.validar_credenciales: Para validar las credenciales del usuario.
- src.GUI.ventanas_admin: Para abrir la ventana principal del administrador.
- src.GUI.ventanas_centro_acopio: Para abrir la ventana principal del centro de acopio.

Clases:
- InterfazLogin: Clase para la ventana de inicio de sesión.
"""


import tkinter as tk
from tkinter import messagebox
from src.code.storage.validar_credenciales import validar_credenciales
from src.GUI.ventanas_admin import AppPrincipalAdmin
from src.GUI.ventanas_centro_acopio import AppPrincipalCentroAcopio
class InterfazLogin(tk.Toplevel):
    """
    Clase para la ventana de inicio de sesión.

    Métodos:
    - __init__: Inicializa la ventana de inicio de sesión.
    - iniciar_sesion: Verifica las credenciales del usuario y abre la ventana correspondiente según el rol del usuario.
    """

    def __init__(self, parent):
        """
        Inicializa la ventana de inicio de sesión.

        :param parent: Ventana padre.
        :type parent: tk.Tk
        """

        super().__init__(parent)
        self.title("Inicio de Sesión")
        self.geometry("300x150")

        self.label_carnet = tk.Label(self, text="Carnet:")
        self.label_carnet.pack()
        self.entry_carnet = tk.Entry(self)
        self.entry_carnet.pack()

        self.label_contrasena = tk.Label(self, text="Contraseña:")
        self.label_contrasena.pack()
        self.entry_contrasena = tk.Entry(self, show="*")
        self.entry_contrasena.pack()

        self.btn_login = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.btn_login.pack()

        self.parent = parent

    def iniciar_sesion(self):
        """
        Verifica las credenciales del usuario y abre la ventana correspondiente según el rol del usuario.
        """

        carnet = self.entry_carnet.get()
        contrasena = self.entry_contrasena.get()
        """
        carnet = "centro@tec.ac.cr"
        contrasena = "9900abcd"
        """
        rol = validar_credenciales(carnet, contrasena)
        if rol == "administrador":
            messagebox.showinfo("Inicio de Sesión", "Bienvenido, administrador!")
            self.destroy()  # Cierra la ventana de login
            root_admin = tk.Tk()  # Nueva ventana principal para administrador
            app = AppPrincipalAdmin(root_admin)
            app.pack(expand=True, fill='both')
            root_admin.mainloop()

        elif rol == "centro_acopio":
            messagebox.showinfo("Inicio de Sesión", "Bienvenido al centro de acopio!")
            self.destroy()  # Cierra la ventana de login
            root_centro = tk.Tk()  # Nueva ventana principal para centro de acopio
            app = AppPrincipalCentroAcopio(master=root_centro, id_funcionario=carnet)
            app.pack(expand=True, fill='both')
            root_centro.mainloop()

        elif rol == "estudiante":
            messagebox.showinfo("Credenciales correctas", "No hay vista a cargar para estudiantes")

        else:
            messagebox.showerror("Error", "No tiene acceso a la plataforma o credenciales incorrectas")



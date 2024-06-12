import tkinter as tk
from tkinter import messagebox
from src.code.storage.validar_credenciales import validar_credenciales

class InterfazLogin(tk.Toplevel):
    def __init__(self, parent):
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
        carnet = self.entry_carnet.get()
        contrasena = self.entry_contrasena.get()

        rol = validar_credenciales(carnet, contrasena)
        if rol == "administrador":
            messagebox.showinfo("Inicio de Sesión", "Bienvenido, administrador!")
            self.destroy()  # Cierra la ventana de login
            from src.GUI.ventanas_admin import AppPrincipalAdmin
            root_admin = tk.Tk()  # Nueva ventana principal para administrador
            app = AppPrincipalAdmin(root_admin)
            app.pack(expand=True, fill='both')
            root_admin.mainloop()
        elif rol == "centro_acopio":
            messagebox.showinfo("Inicio de Sesión", "Bienvenido al centro de acopio!")
            self.destroy()  # Cierra la ventana de login
            from src.GUI.ventanas_centro_acopio import AppPrincipalCentroAcopio
            root_centro = tk.Tk()  # Nueva ventana principal para centro de acopio
            app = AppPrincipalCentroAcopio(master=root_centro, id_funcionario=carnet)
            app.pack(expand=True, fill='both')
            root_centro.mainloop()
        else:
            messagebox.showerror("Error", "No tiene acceso a la plataforma o credenciales incorrectas")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazLogin(root)
    app.mainloop()

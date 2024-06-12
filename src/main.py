import sys
import os
import tkinter as tk

# Agregar src al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.GUI.interfaz_login import InterfazLogin

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal hasta que se inicie sesión

    login = InterfazLogin(root)
    login.protocol("WM_DELETE_WINDOW", root.destroy)  # Cierra toda la app si se cierra la ventana de login

    root.mainloop()

if __name__ == "__main__":
    main()

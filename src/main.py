import tkinter as tk

from src.GUI.ventanas_admin import AppPrincipalAdmin
from src.GUI.ventanas_centro_acopio import AppPrincipalCentroAcopio


def main():
    root = tk.Tk()
    #app = AppPrincipalCentroAcopio(root, "F-4444")
    app = AppPrincipalAdmin(root)
    root.mainloop()


if __name__ == "__main__":
    main()

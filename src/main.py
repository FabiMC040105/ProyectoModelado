import tkinter as tk
from src.GUI.ventanas_admin import AppPrincipalAdmin


def main():
    root = tk.Tk()
    app = AppPrincipalAdmin(root)
    root.mainloop()


if __name__ == "__main__":
    main()

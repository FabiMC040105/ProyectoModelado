import tkinter as tk
from src.GUI.ventanas import AppPrincipal

def main():
    root = tk.Tk()
    app = AppPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()

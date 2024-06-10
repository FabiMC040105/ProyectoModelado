import json
import os

# Obtener la ruta del archivo usuarios.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USUARIOS_FILE = os.path.join(BASE_DIR, 'db', 'usuarios.json')

def cargar_usuarios():
    with open(USUARIOS_FILE, 'r') as file:
        return json.load(file)

def validar_credenciales(carnet, contrasena):
    usuarios = cargar_usuarios()
    usuario = usuarios.get(carnet)
    if usuario and usuario["contrasena"] == contrasena:
        return usuario["rol"]
    return None

"""
Este módulo proporciona funciones para gestionar la autenticación de usuarios mediante un archivo JSON.

Funciones disponibles:
- cargar_usuarios: Carga la lista de usuarios desde un archivo JSON.
- validar_credenciales: Valida las credenciales de un usuario.
- verificar_correo_estudiante: Verifica si un correo corresponde a un estudiante.

Dependencias:
- json: Para cargar y escribir datos en archivos JSON.
- os: Para manipular rutas de archivos y verificar la existencia de archivos.

Constantes utilizadas:
- USUARIOS_FILE: Ruta del archivo JSON que contiene la información de los usuarios.
"""

import json
import os

# Obtener la ruta del archivo usuarios.json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
USUARIOS_FILE = os.path.join(BASE_DIR, 'db', 'usuarios.json')

def cargar_usuarios():
    """
    Carga la lista de usuarios desde un archivo JSON.

    :return: Diccionario de usuarios.
    :rtype: dict
    """
    with open(USUARIOS_FILE, 'r') as file:
        return json.load(file)

def validar_credenciales(carnet, contrasena):
    """
    Valida las credenciales de un usuario.

    :param carnet: Carnet del usuario.
    :type carnet: str
    :param contrasena: Contraseña del usuario.
    :type contrasena: str
    :return: El rol del usuario si las credenciales son válidas, None en caso contrario.
    :rtype: str or None
    """
    usuarios = cargar_usuarios()
    usuario = usuarios.get(carnet)
    if usuario and usuario["contrasena"] == contrasena:
        return usuario["rol"]
    return None

def verificar_correo_estudiante(correo):
    """
    Verifica si un correo corresponde a un estudiante.

    :param correo: Correo del usuario.
    :type correo: str
    :return: True si el correo corresponde a un estudiante, False en caso contrario.
    :rtype: bool
    """
    usuarios = cargar_usuarios()
    usuario = usuarios.get(correo)
    if usuario and usuario["rol"] == "estudiante":
        return True
    return False

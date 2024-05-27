
# Archivos JSON
JSON_MATERIAL = "materiales.json"
JSON_SEDE = "sedes.json"
JSON_CENTRO_DE_ACOPIO = "centros_de_acopio.json"
JSON_TRANSACCIONES_CENTRO_DE_ACOPIO ="transacciones_centros_de_acopio.json"
JSON_FUNCIONARIOS = "funcionarios.json"

# Columnas de tablas
COLUMNAS_TABLA_MATERIAL = ("ID", "Nombre", "Unidad", "Valor", "Estado", "Fecha de Creación", "Descripción")
COLUMNAS_TABLA_SEDE = ("Nombre", "Ubicación", "Estado", "Teléfono")
COLUMNAS_TABLA_CENTRO_ACOPIO = ("Sede", "Número Telefónico", "Ubicación", "Estado")
COLUMNAS_TABLA_TRANSACCIONES_CENTRO_ACOPIO = ("id_transaccion", "carnet", "sede", "fecha_hora", "materiales", "total")

# Prefijos
PREFIJO_MATERIAL = "M-"
PREFIJO_SEDE = "S-"
PREFIJO_ESTUDIANTE = "E-"
PREFIJO_TRANSACCION = "T-"

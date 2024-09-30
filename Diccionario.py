informacion_personal = {
    "nombre": "Ana Pérez",
    "edad": 29,
    "ciudad": "Quito",
    "profesion": "Ingeniera Civil"
}

# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# Agregar o modificar la clave "profesion"
informacion_personal["profesion"] = "Arquitecta"


# Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"


# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]


print(informacion_personal)

{
    "nombre": "Ana Pérez",
    "ciudad": "Guayaquil",
    "profesion": "Arquitecta",
    "telefono": "0987654321"
}

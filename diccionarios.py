# Creación del diccionario con la información personal ficticia
informacion_personal = {
    "nombre": "Jonathan Felix",
    "edad": 33,
    "ciudad": "Quito",
    "profesion": "Chofer y Guardaespaldas"
}

# Imprimimos el diccionario inicial para verificar su creación
print("Diccionario inicial:", informacion_personal)
# Acceder al valor de la clave 'ciudad' y modificarlo
informacion_personal["ciudad"] = "Guayaquil"  # Cambiamos 'Quito' por 'Guayaquil'
print("Después de modificar la ciudad:", informacion_personal)

# Agregar una nueva clave 'profesion' con un nuevo valor
informacion_personal["nueva_profesion"] = "Instructor de manejo"  # Nueva clave-valor
print("Después de agregar nueva profesión:", informacion_personal)

# Verificar si existe la clave 'telefono'. Si no existe, la añadimos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0997011051"  # Número ficticio
    print("Clave 'telefono' agregada:", informacion_personal)
else:
    print("La clave 'telefono' ya existe.")

# Eliminar la clave 'edad'
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave
    print("Clave 'edad' eliminada:", informacion_personal)
else:
    print("La clave 'edad' no existe.")

# Imprimir el diccionario final después de realizar todas las operaciones
print("Diccionario final:", informacion_personal)

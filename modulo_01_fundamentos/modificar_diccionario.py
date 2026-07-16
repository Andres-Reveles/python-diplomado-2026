print("--- Modificar Diccionario ---")

alumno = {
    "nombre": "Andres",
    "edad": 23,
    "carrera": "ISC",
    "promedio": 9.5
}

print("Antes de modificar:")
print(alumno)

alumno["edad"] = 24
alumno["promedio"] = 9.8

print("Después de modificar:")
print(alumno)
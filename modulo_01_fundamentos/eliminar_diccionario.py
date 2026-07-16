print("--- Eliminar Diccionario ---")

alumno = {
    "nombre": "Andres",
    "edad": 23,
    "carrera": "ISC",
    "promedio": 9.5
}

print("Diccionario original")
print(alumno)

del alumno["promedio"]
print("Diccionario modificado")
print(alumno)
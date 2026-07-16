print("--- Validar Clave en Diccionario ---")

alumno = {
    "nombre": "Andres",
    "edad": 23,
    "carrera": "ISC",
    "promedio": 9.5
}

clave = input("Ingrese la clave a validar: ").strip()

if clave in alumno:
    print(f"La clave '{clave}' existe en el diccionario")
    print(f"Valor asociado a la clave '{clave}': {alumno[clave]}")
else:
    print(f"La clave '{clave}' no existe en el diccionario")
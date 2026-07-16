print("--- Recorrer Diccionario ---")

alumno = {
    "nombre": "Andres",
    "edad": 23,
    "carrera": "ISC",
    "promedio": 9.5
}

print("Claves del diccionario:")
for clave in alumno.keys():
    print(clave)

print()
print("Valores del diccionario:")
for valor in alumno.values():
    print(valor)

print()
print("Claves y valores del diccionario:")
for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

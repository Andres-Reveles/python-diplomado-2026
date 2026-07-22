print("-- Scope básico ---")

nombre_global = "Andres"

def saludar():
    nombre_local = "Angel"
    print(f"Nombre global: {nombre_global}")
    print(f"Nombre local: {nombre_local}")

saludar()

print(f"Nombre global: {nombre_global}")

# Esta línea daría error porque nombre_local solo existe dentro de la función
# print(nombre_local)


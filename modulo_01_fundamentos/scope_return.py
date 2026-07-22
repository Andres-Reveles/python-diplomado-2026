print("=== Modificar valores usando return ===")

nombre = "Angel"


def cambiar_nombre(nombre_actual):
    nuevo_nombre = nombre_actual + " Andres"
    return nuevo_nombre


print(f"Nombre antes de llamar la función: {nombre}")

nombre = cambiar_nombre(nombre)

print(f"Nombre después de llamar la función: {nombre}")
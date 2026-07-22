print("=== Scope con el mismo nombre ===")

nombre = "Angel"


def cambiar_nombre():
    nombre = "Andres"
    print(f"Nombre dentro de la función: {nombre}")


print(f"Nombre antes de llamar la función: {nombre}")

cambiar_nombre()

print(f"Nombre después de llamar la función: {nombre}")
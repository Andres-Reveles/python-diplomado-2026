print("--- Sets Eliminar ---")

nombres = {"Andres", "Juan", "Pedro", "Maria"}
print(f"Set original: {nombres}")

nombre = input("Ingrese un nombre a eliminar: ")
if nombre in nombres:
    nombres.remove(nombre)
    print(f"Set actualizado: {nombres}")
else:
    print(f"El nombre '{nombre}' no se encuentra en el set.")

print(f"Set final: {nombres}")
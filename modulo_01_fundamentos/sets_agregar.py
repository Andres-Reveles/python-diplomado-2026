print("--- Sets Agregar ---")

nombres = {"Andres", "Juan", "Pedro"}
print(f"Set original: {nombres}")

nombres.add("Maria")
print(f"Set después de agregar un elemento: {nombres}")
nombres.add("Juan")  # Intentando agregar un elemento duplicado
print(f"Set después de intentar agregar un elemento duplicado: {nombres}")

print(f"Cantidad de elementos en el set: {len(nombres)}")
print(f"Set actual: {nombres}")
print(f"Set ordenado: {sorted(nombres)}")  # Ordenando el set para mostrarlo
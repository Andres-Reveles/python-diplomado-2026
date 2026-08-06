import json

print(" --- Cargar productos desde un archivo JSON ---")

with open('productos.json', 'r') as archivo_json:
    productos = json.load(archivo_json)

print("Productos cargados desde el archivo JSON:")
print(productos)


print()
print("--- Productos cargados ---")
for producto in productos:
    print(f"Codigo: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Stock: {producto['stock']}")
    print("-----------------------------")
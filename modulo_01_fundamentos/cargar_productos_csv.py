import csv

print("--- Cargar productos desde un archivo CSV ---")

productos = []

with open('productos.csv', 'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)

    for fila in lector:
        producto = {
            'codigo': fila['codigo'],
            'nombre': fila['nombre'],
            'precio': float(fila['precio']),
            'stock': int(fila['stock'])
        }
        productos.append(producto)

print("Productos cargados desde el archivo CSV:")
print(productos)

print()
print("--- Productos registrados ---")

for producto in productos:
    print(f"Codigo: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: {producto['precio']}")
    print(f"Stock: {producto['stock']}")
    print("-----------------------------")
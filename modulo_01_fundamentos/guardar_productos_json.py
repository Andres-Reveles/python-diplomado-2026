import json

print(" --- Guardar productos en un archivo JSON ---")

productos = [
    {
        'codigo': 'P001',
        'nombre': 'Producto 1',
        'precio': 100.0,
        'stock': 50
    },
    {
        'codigo': 'P002',
        'nombre': 'Producto 2',
        'precio': 200.0,
        'stock': 30
    },
    {
        'codigo': 'P003',
        'nombre': 'Producto 3',
        'precio': 150.0,
        'stock': 20
    }

]

with open('productos.json', 'w') as archivo_json:
    json.dump(productos, archivo_json, ensure_ascii=False, indent=4)

print("Productos guardados en el archivo JSON.")
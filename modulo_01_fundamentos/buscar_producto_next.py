print("--- Buscar Producto Next ---")

productos = [
    {"codigo": "P001", "nombre": "Laptop", "precio": 1200, "stock": 10},
    {"codigo": "P002", "nombre": "Smartphone", "precio": 800, "stock": 20},
    {"codigo": "P003", "nombre": "Tablet", "precio": 500, "stock": 15},
    {"codigo": "P004", "nombre": "Monitor", "precio": 300, "stock": 5},
    {"codigo": "P005", "nombre": "Teclado", "precio": 50, "stock": 30}
]

codigo_buscado = input("Ingrese el código del producto a buscar: ")

producto_encontrado = next(
    (producto for producto in productos if producto["codigo"] == codigo_buscado), None)

if producto_encontrado:
    print("Producto encontrado:")
    print(producto_encontrado)
else:
    print("Producto no encontrado.")
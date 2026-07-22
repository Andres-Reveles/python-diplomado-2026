print("--- Validar Producto Any ---")

productos = [
    {"codigo": "P001", "nombre": "Laptop", "precio": 1200, "stock": 10},
    {"codigo": "P002", "nombre": "Smartphone", "precio": 800, "stock": 20},
    {"codigo": "P003", "nombre": "Tablet", "precio": 500, "stock": 15},
    {"codigo": "P004", "nombre": "Monitor", "precio": 300, "stock": 5},
    {"codigo": "P005", "nombre": "Teclado", "precio": 50, "stock": 30}
]

codigo = input("Ingrese el código del producto a validar: ")

existe = any(producto["codigo"] == codigo for producto in productos)

if existe:
    print("El producto existe.")
else:
    print("El producto no existe.")
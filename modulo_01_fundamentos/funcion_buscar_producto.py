print("--- Función buscar producto ---")

productos = [
    {"Codigo": "P001", "nombre": "Laptop", "precio": 12000, "stock": 10},
    {"Codigo": "P002", "nombre": "Mouse", "precio": 500, "stock": 50},
    {"Codigo": "P003", "nombre": "Teclado", "precio": 800, "stock": 30},
    {"Codigo": "P004", "nombre": "Monitor", "precio": 3000, "stock": 20}
]

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["Codigo"] == codigo:
            return producto
    return None


codigo_buscar = input("Ingrese el código del producto a buscar: ")

producto_encontrado = buscar_producto(productos, codigo_buscar)

if producto_encontrado is not None:
    print("Producto encontrado:")
    print(f"Código: {producto_encontrado['Codigo']}")
    print(f"Nombre: {producto_encontrado['nombre']}")
    print(f"Precio: {producto_encontrado['precio']}")
    print(f"Stock: {producto_encontrado['stock']}")
else:
    print("Producto no encontrado.")
print("--- Función mostrar productos ---")


productos = [
    {"Codigo": "P001", "nombre": "Laptop", "precio": 12000, "stock": 10},
    {"Codigo": "P002", "nombre": "Mouse", "precio": 500, "stock": 50},
    {"Codigo": "P003", "nombre": "Teclado", "precio": 800, "stock": 30},
    {"Codigo": "P004", "nombre": "Monitor", "precio": 3000, "stock": 20}
]

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos disponibles.")
        return
    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. Código: {producto['Codigo']}")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: {producto['precio']}")
        print(f"   Stock: {producto['stock']}")
        print("--------------------")

mostrar_productos(productos)
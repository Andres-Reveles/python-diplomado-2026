print("=== Función para filtrar productos ===")

productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250.0, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500.0, "stock": 5},
    {"codigo": "P003", "nombre": "Monitor", "precio": 3200.0, "stock": 2},
    {"codigo": "P004", "nombre": "Webcam", "precio": 850.0, "stock": 0},
    {"codigo": "P005", "nombre": "USB", "precio": 120.0, "stock": 20}
]


def mostrar_productos_simple(productos):
    if len(productos) == 0:
        print("No hay productos para mostrar")
        return

    for producto in productos:
        print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def filtrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Filtros ===")
    print("1. Productos disponibles")
    print("2. Productos sin stock")
    print("3. Productos caros")
    print("4. Productos baratos")

    opcion = input("Elige una opción de filtro: ").strip()

    if opcion == "1":
        productos_filtrados = [
            producto for producto in productos
            if producto["stock"] > 0
        ]
        print("=== Productos disponibles ===")

    elif opcion == "2":
        productos_filtrados = [
            producto for producto in productos
            if producto["stock"] == 0
        ]
        print("=== Productos sin stock ===")

    elif opcion == "3":
        productos_filtrados = [
            producto for producto in productos
            if producto["precio"] > 500
        ]
        print("=== Productos caros ===")

    elif opcion == "4":
        productos_filtrados = [
            producto for producto in productos
            if producto["precio"] <= 500
        ]
        print("=== Productos baratos ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_simple(productos_filtrados)


filtrar_productos(productos)
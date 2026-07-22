print("=== Función para ordenar productos ===")

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


def ordenar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Ordenar productos ===")
    print("1. Precio menor a mayor")
    print("2. Precio mayor a menor")
    print("3. Stock menor a mayor")
    print("4. Stock mayor a menor")
    print("5. Nombre A-Z")

    opcion = input("Elige una opción de ordenamiento: ").strip()

    if opcion == "1":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["precio"]
        )
        print("=== Productos por precio menor a mayor ===")

    elif opcion == "2":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["precio"],
            reverse=True
        )
        print("=== Productos por precio mayor a menor ===")

    elif opcion == "3":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["stock"]
        )
        print("=== Productos por stock menor a mayor ===")

    elif opcion == "4":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["stock"],
            reverse=True
        )
        print("=== Productos por stock mayor a menor ===")

    elif opcion == "5":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["nombre"].lower()
        )
        print("=== Productos por nombre A-Z ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_simple(productos_ordenados)


ordenar_productos(productos)
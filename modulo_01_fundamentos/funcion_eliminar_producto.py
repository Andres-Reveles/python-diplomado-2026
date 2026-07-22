print("=== Función para eliminar producto ===")

productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250.0, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500.0, "stock": 5},
    {"codigo": "P003", "nombre": "Monitor", "precio": 3200.0, "stock": 2}
]


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
    else:
        print("=== Productos registrados ===")

        for indice, producto in enumerate(productos, start=1):
            print(f"{indice}. Código: {producto['codigo']}")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Precio: ${producto['precio']}")
            print(f"   Stock: {producto['stock']}")
            print("--------------------")


def eliminar_producto(productos):
    codigo = input("Ingresa el código del producto a eliminar: ").strip().upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")

    confirmacion = input("¿Seguro que deseas eliminarlo? Escribe si o no: ").strip().lower()

    if confirmacion == "si" or confirmacion == "sí":
        productos.remove(producto)
        print("Producto eliminado correctamente")
    else:
        print("Eliminación cancelada")


eliminar_producto(productos)

print()
mostrar_productos(productos)
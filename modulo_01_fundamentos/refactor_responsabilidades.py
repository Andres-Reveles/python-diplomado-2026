print("=== Refactor: separar responsabilidades ===")


def crear_producto(codigo, nombre, precio, stock):
    """
    Crea un diccionario que representa un producto.
    """
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    return producto


def mostrar_producto(producto):
    """
    Muestra la información de un solo producto.
    """
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


def mostrar_productos(productos):
    """
    Muestra una lista de productos.
    """
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"Producto {indice}")
        mostrar_producto(producto)
        print("--------------------")


producto_1 = crear_producto("P001", "Mouse", 250.0, 10)
producto_2 = crear_producto("P002", "Teclado", 500.0, 5)
producto_3 = crear_producto("P003", "Monitor", 3200.0, 2)

productos = [producto_1, producto_2, producto_3]

mostrar_productos(productos)

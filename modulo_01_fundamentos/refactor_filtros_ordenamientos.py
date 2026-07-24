print("=== Refactor: filtros y ordenamientos ===")


def crear_producto(codigo, nombre, precio, stock):
    """
    Crea y retorna un diccionario con los datos de un producto.
    """
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }


def mostrar_producto_resumen(producto):
    """
    Muestra un producto en formato resumido.
    """
    print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def mostrar_productos_resumen(productos):
    """
    Muestra una lista de productos en formato resumido.
    """
    if len(productos) == 0:
        print("No hay productos para mostrar")
        return

    for producto in productos:
        mostrar_producto_resumen(producto)


def obtener_productos_disponibles(productos):
    """
    Retorna productos con stock mayor a cero.
    """
    return [
        producto for producto in productos
        if producto["stock"] > 0
    ]


def obtener_productos_sin_stock(productos):
    """
    Retorna productos con stock igual a cero.
    """
    return [
        producto for producto in productos
        if producto["stock"] == 0
    ]


def obtener_productos_caros(productos, precio_minimo=500):
    """
    Retorna productos con precio mayor al precio mínimo.
    """
    return [
        producto for producto in productos
        if producto["precio"] > precio_minimo
    ]


def obtener_productos_baratos(productos, precio_maximo=500):
    """
    Retorna productos con precio menor o igual al precio máximo.
    """
    return [
        producto for producto in productos
        if producto["precio"] <= precio_maximo
    ]


def ordenar_por_precio(productos, descendente=False):
    """
    Retorna productos ordenados por precio.
    """
    return sorted(
        productos,
        key=lambda producto: producto["precio"],
        reverse=descendente
    )


def ordenar_por_stock(productos, descendente=False):
    """
    Retorna productos ordenados por stock.
    """
    return sorted(
        productos,
        key=lambda producto: producto["stock"],
        reverse=descendente
    )


def ordenar_por_nombre(productos):
    """
    Retorna productos ordenados por nombre A-Z.
    """
    return sorted(
        productos,
        key=lambda producto: producto["nombre"].lower()
    )


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2),
    crear_producto("P004", "Webcam", 850.0, 0),
    crear_producto("P005", "USB", 120.0, 20)
]

print("=== Productos disponibles ===")
productos_disponibles = obtener_productos_disponibles(productos)
mostrar_productos_resumen(productos_disponibles)

print()
print("=== Productos sin stock ===")
productos_sin_stock = obtener_productos_sin_stock(productos)
mostrar_productos_resumen(productos_sin_stock)

print()
print("=== Productos caros ===")
productos_caros = obtener_productos_caros(productos)
mostrar_productos_resumen(productos_caros)

print()
print("=== Productos baratos ===")
productos_baratos = obtener_productos_baratos(productos)
mostrar_productos_resumen(productos_baratos)

print()
print("=== Precio menor a mayor ===")
productos_por_precio = ordenar_por_precio(productos)
mostrar_productos_resumen(productos_por_precio)

print()
print("=== Precio mayor a menor ===")
productos_por_precio_desc = ordenar_por_precio(productos, descendente=True)
mostrar_productos_resumen(productos_por_precio_desc)

print()
print("=== Stock mayor a menor ===")
productos_por_stock_desc = ordenar_por_stock(productos, descendente=True)
mostrar_productos_resumen(productos_por_stock_desc)

print()
print("=== Nombre A-Z ===")
productos_por_nombre = ordenar_por_nombre(productos)
mostrar_productos_resumen(productos_por_nombre)
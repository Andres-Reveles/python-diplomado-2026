print("=== Refactor: reporte general ===")


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


def calcular_stock_total(productos):
    """
    Calcula el stock total del inventario.
    """
    return sum(producto["stock"] for producto in productos)


def calcular_valor_total(productos):
    """
    Calcula el valor total del inventario.
    """
    return sum(producto["precio"] * producto["stock"] for producto in productos)


def obtener_producto_mas_caro(productos):
    """
    Retorna el producto con mayor precio.
    """
    return max(productos, key=lambda producto: producto["precio"])


def obtener_producto_mas_barato(productos):
    """
    Retorna el producto con menor precio.
    """
    return min(productos, key=lambda producto: producto["precio"])


def hay_productos_sin_stock(productos):
    """
    Valida si existe al menos un producto sin stock.
    """
    return any(producto["stock"] == 0 for producto in productos)


def todos_tienen_precio_valido(productos):
    """
    Valida si todos los productos tienen precio mayor a cero.
    """
    return all(producto["precio"] > 0 for producto in productos)


def mostrar_producto_resumen(producto):
    """
    Muestra un producto en formato resumido.
    """
    print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def mostrar_reporte_general(productos):
    """
    Muestra un reporte general del inventario.
    """
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    cantidad_productos = len(productos)
    stock_total = calcular_stock_total(productos)
    valor_total = calcular_valor_total(productos)

    producto_mas_caro = obtener_producto_mas_caro(productos)
    producto_mas_barato = obtener_producto_mas_barato(productos)

    existe_producto_sin_stock = hay_productos_sin_stock(productos)
    precios_validos = todos_tienen_precio_valido(productos)

    print("=== Reporte general ===")
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total del inventario: ${valor_total}")

    print()
    print("Producto más caro:")
    mostrar_producto_resumen(producto_mas_caro)

    print()
    print("Producto más barato:")
    mostrar_producto_resumen(producto_mas_barato)

    print()
    print(f"¿Hay productos sin stock?: {existe_producto_sin_stock}")
    print(f"¿Todos tienen precio válido?: {precios_validos}")


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2),
    crear_producto("P004", "Webcam", 850.0, 0),
    crear_producto("P005", "USB", 120.0, 20)
]

mostrar_reporte_general(productos)
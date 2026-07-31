from producto import mostrar_producto_resumen


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

    print("=== Reporte general del inventario ===")
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
    print(f"¿Hay productos sin stock?: {hay_productos_sin_stock(productos)}")


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


def mostrar_productos_resumen(productos):
    """
    Muestra una lista de productos en formato resumido.
    """
    if len(productos) == 0:
        print("No hay productos para mostrar")
        return

    for producto in productos:
        mostrar_producto_resumen(producto)
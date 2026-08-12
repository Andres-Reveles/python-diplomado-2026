from venta import mostrar_venta_resumen


def calcular_total_ventas(ventas):
    """
    Calcula el total vendido en dinero.
    """
    return sum(venta["total"] for venta in ventas)


def calcular_total_productos_vendidos(ventas):
    """
    Calcula cuántas piezas se vendieron en total.
    """
    return sum(venta["cantidad"] for venta in ventas)


def obtener_venta_mayor(ventas):
    """
    Retorna la venta con mayor total.
    """
    if len(ventas) == 0:
        return None

    return max(ventas, key=lambda venta: venta["total"])


def mostrar_reporte_ventas(ventas):
    """
    Muestra un reporte general de ventas.
    """
    if len(ventas) == 0:
        print("No hay ventas registradas")
        return

    total_ventas = calcular_total_ventas(ventas)
    total_productos_vendidos = calcular_total_productos_vendidos(ventas)
    venta_mayor = obtener_venta_mayor(ventas)

    print("=== Reporte general de ventas ===")
    print(f"Cantidad de ventas registradas: {len(ventas)}")
    print(f"Total de productos vendidos: {total_productos_vendidos}")
    print(f"Total vendido: ${total_ventas}")

    print()
    print("Venta de mayor monto:")
    mostrar_venta_resumen(venta_mayor)


def mostrar_ventas_resumen(ventas):
    """
    Muestra todas las ventas en formato resumido.
    """
    if len(ventas) == 0:
        print("No hay ventas registradas")
        return

    print("=== Ventas registradas ===")

    for venta in ventas:
        mostrar_venta_resumen(venta)
def crear_venta(folio, codigo_producto, nombre_producto, precio_unitario, cantidad):
    """
    Crea y retorna un diccionario que representa una venta.
    """
    total = precio_unitario * cantidad

    return {
        "folio": folio,
        "codigo_producto": codigo_producto,
        "nombre_producto": nombre_producto,
        "precio_unitario": precio_unitario,
        "cantidad": cantidad,
        "total": total
    }


def mostrar_venta(venta):
    """
    Muestra la información completa de una venta.
    """
    print(f"Folio: {venta['folio']}")
    print(f"Código producto: {venta['codigo_producto']}")
    print(f"Producto: {venta['nombre_producto']}")
    print(f"Precio unitario: ${venta['precio_unitario']}")
    print(f"Cantidad: {venta['cantidad']}")
    print(f"Total: ${venta['total']}")


def mostrar_venta_resumen(venta):
    """
    Muestra la venta en formato resumido.
    """
    print(
        f"{venta['folio']} - {venta['nombre_producto']} - "
        f"Cantidad: {venta['cantidad']} - Total: ${venta['total']}"
    )
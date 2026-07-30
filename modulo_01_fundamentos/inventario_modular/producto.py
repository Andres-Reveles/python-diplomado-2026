def crear_producto(codigo, nombre, precio, stock):
    """
    Crea y retorna un diccionario que representa un producto.
    """
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }


def mostrar_producto(producto):
    """
    Muestra la información de un producto.
    """
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")
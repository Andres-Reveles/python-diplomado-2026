print("=== Docstrings básicos ===")


def calcular_total(precio, cantidad):
    """
    Calcula el total de una compra.

    Parámetros:
    precio: precio unitario del producto.
    cantidad: cantidad de productos comprados.

    Retorna:
    El total de la compra.
    """
    return precio * cantidad


def precio_valido(precio):
    """
    Valida si un precio es mayor a cero.

    Parámetros:
    precio: número a validar.

    Retorna:
    True si el precio es válido, False en caso contrario.
    """
    return precio > 0


total = calcular_total(250, 3)

print(f"Total de la compra: ${total}")

if precio_valido(250):
    print("El precio es válido")
else:
    print("El precio es inválido")
from venta import crear_venta, mostrar_venta
from entradas import pedir_texto_no_vacio, pedir_int_positivo
from producto_servicio import buscar_producto


def generar_folio(ventas):
    """
    Genera un folio automático para la venta.
    """
    numero = len(ventas) + 1
    return f"V{numero:03d}"


def stock_suficiente(producto, cantidad):
    """
    Valida si el producto tiene stock suficiente.
    """
    return producto["stock"] >= cantidad


def registrar_venta(productos, ventas):
    """
    Registra una venta y descuenta stock del producto.
    """
    codigo = pedir_texto_no_vacio("Ingresa el código del producto a vender: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado:")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock disponible: {producto['stock']}")

    cantidad = pedir_int_positivo("Ingresa la cantidad a vender: ")

    if not stock_suficiente(producto, cantidad):
        print("Error: no hay stock suficiente")
        return

    folio = generar_folio(ventas)

    venta = crear_venta(
        folio,
        producto["codigo"],
        producto["nombre"],
        producto["precio"],
        cantidad
    )

    ventas.append(venta)

    producto["stock"] -= cantidad

    print("Venta registrada correctamente")
    print("Detalle de venta:")
    mostrar_venta(venta)


def mostrar_ventas(ventas):
    """
    Muestra todas las ventas registradas.
    """
    if len(ventas) == 0:
        print("No hay ventas registradas")
        return

    print("=== Ventas registradas ===")

    for indice, venta in enumerate(ventas, start=1):
        print(f"Venta {indice}")
        mostrar_venta(venta)
        print("--------------------")
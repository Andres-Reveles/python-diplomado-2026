from producto import crear_producto, mostrar_producto
from entradas import pedir_texto_no_vacio, pedir_float_positivo, pedir_int_no_negativo


def buscar_producto(productos, codigo):
    """
    Busca un producto por código.
    Retorna el producto si existe o None si no existe.
    """
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def codigo_disponible(productos, codigo):
    """
    Valida si un código de producto está disponible.
    """
    producto = buscar_producto(productos, codigo)

    return producto is None


def mostrar_productos(productos):
    """
    Muestra todos los productos registrados.
    """
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"Producto {indice}")
        mostrar_producto(producto)
        print("--------------------")


def registrar_producto(productos):
    """
    Registra un producto nuevo.
    """
    codigo = pedir_texto_no_vacio("Ingresa el código del producto: ").upper()

    if not codigo_disponible(productos, codigo):
        print("Error: ya existe un producto con ese código")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre del producto: ")
    precio = pedir_float_positivo("Ingresa el precio del producto: ")
    stock = pedir_int_no_negativo("Ingresa el stock del producto: ")

    producto = crear_producto(codigo, nombre, precio, stock)

    productos.append(producto)

    print("Producto registrado correctamente")


def buscar_producto_menu(productos):
    """
    Busca un producto por código y lo muestra.
    """
    codigo = pedir_texto_no_vacio("Ingresa el código del producto a buscar: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado:")
    mostrar_producto(producto)
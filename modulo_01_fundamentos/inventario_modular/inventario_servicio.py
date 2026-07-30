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
    Valida si un código está disponible.
    """
    producto = buscar_producto(productos, codigo)

    return producto is None


def mostrar_productos(productos):
    """
    Muestra todos los productos del inventario.
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
    codigo = pedir_texto_no_vacio("Ingresa el código: ").upper()

    if not codigo_disponible(productos, codigo):
        print("Error: ya existe un producto con ese código")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
    precio = pedir_float_positivo("Ingresa el precio: ")
    stock = pedir_int_no_negativo("Ingresa el stock: ")

    producto = crear_producto(codigo, nombre, precio, stock)

    productos.append(producto)

    print("Producto registrado correctamente")

def buscar_producto_menu(productos):
    """
    Busca un producto por código y lo muestra en pantalla.
    """
    codigo = pedir_texto_no_vacio("Ingresa el código del producto a buscar: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado:")
    mostrar_producto(producto)

def pedir_producto_existente(productos):
    """
    Pide un código y retorna el producto si existe.
    Si no existe, retorna None.
    """
    codigo = pedir_texto_no_vacio("Ingresa el código del producto: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return None

    return producto


def actualizar_precio(productos):
    """
    Actualiza el precio de un producto existente.
    """
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado:")
    mostrar_producto(producto)

    nuevo_precio = pedir_float_positivo("Ingresa el nuevo precio: ")

    producto["precio"] = nuevo_precio

    print("Precio actualizado correctamente")


def actualizar_stock(productos):
    """
    Actualiza el stock de un producto existente.
    """
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado:")
    mostrar_producto(producto)

    nuevo_stock = pedir_int_no_negativo("Ingresa el nuevo stock: ")

    producto["stock"] = nuevo_stock

    print("Stock actualizado correctamente")

def confirmar_accion(mensaje):
    """
    Pide confirmación al usuario.
    Retorna True si responde si/sí.
    """
    respuesta = input(mensaje).strip().lower()

    return respuesta == "si" or respuesta == "sí"


def eliminar_producto(productos):
    """
    Elimina un producto existente del inventario.
    """
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado:")
    mostrar_producto(producto)

    confirmado = confirmar_accion("¿Seguro que deseas eliminarlo? Escribe si o no: ")

    if confirmado:
        productos.remove(producto)
        print("Producto eliminado correctamente")
    else:
        print("Eliminación cancelada")
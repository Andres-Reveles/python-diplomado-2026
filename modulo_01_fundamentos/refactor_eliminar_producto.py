print("=== Refactor: eliminar producto ===")


def pedir_texto_no_vacio(mensaje):
    """
    Pide un texto y no permite que esté vacío.
    """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


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


def buscar_producto(productos, codigo):
    """
    Busca un producto por código.
    """
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


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


def confirmar_accion(mensaje):
    """
    Pide confirmación al usuario.

    Retorna True si responde si/sí.
    Retorna False en cualquier otro caso.
    """
    respuesta = input(mensaje).strip().lower()

    return respuesta == "si" or respuesta == "sí"


def mostrar_producto(producto):
    """
    Muestra la información de un producto.
    """
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


def mostrar_productos(productos):
    """
    Muestra todos los productos.
    """
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"Producto {indice}")
        mostrar_producto(producto)
        print("--------------------")


def eliminar_producto(productos):
    """
    Elimina un producto existente de la lista.
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


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2)
]

print("Inventario inicial:")
mostrar_productos(productos)

print()
eliminar_producto(productos)

print()
print("Inventario actualizado:")
mostrar_productos(productos)
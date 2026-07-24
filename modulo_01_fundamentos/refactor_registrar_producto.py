print("=== Refactor: registrar producto completo ===")


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


def pedir_float_positivo(mensaje):
    """
    Pide un número decimal mayor a cero.
    """
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


def pedir_int_no_negativo(mensaje):
    """
    Pide un número entero mayor o igual a cero.
    """
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)

            if numero < 0:
                print("Error: el número no puede ser negativo")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


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

    Retorna el producto si existe, o None si no existe.
    """
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def codigo_disponible(productos, codigo):
    """
    Valida que no exista un producto con el mismo código.
    """
    producto = buscar_producto(productos, codigo)

    return producto is None


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


def registrar_producto(productos):
    """
    Registra un producto nuevo en la lista de productos.
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


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5)
]

registrar_producto(productos)

print()
mostrar_productos(productos)

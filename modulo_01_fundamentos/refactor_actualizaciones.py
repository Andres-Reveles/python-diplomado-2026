print("=== Refactor: actualizar precio y stock ===")


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


def actualizar_precio(productos):
    """
    Actualiza el precio de un producto existente.
    """
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio actual: ${producto['precio']}")

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

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Stock actual: {producto['stock']}")

    nuevo_stock = pedir_int_no_negativo("Ingresa el nuevo stock: ")

    producto["stock"] = nuevo_stock

    print("Stock actualizado correctamente")


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2)
]

print("Inventario inicial:")
mostrar_productos(productos)

print()
actualizar_precio(productos)

print()
actualizar_stock(productos)

print()
print("Inventario actualizado:")
mostrar_productos(productos)
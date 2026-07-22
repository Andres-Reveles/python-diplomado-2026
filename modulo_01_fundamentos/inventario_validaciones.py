print("=== Inventario con validaciones reutilizables ===")


def buscar_producto(productos, codigo):
    """
    Busca un producto por código.

    Retorna:
    El producto encontrado o None si no existe.
    """
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def texto_no_vacio(texto):
    """
    Valida que un texto no esté vacío.
    """
    return texto.strip() != ""


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


def mostrar_productos(productos):
    """
    Muestra todos los productos registrados.
    """
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. Código: {producto['codigo']}")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: ${producto['precio']}")
        print(f"   Stock: {producto['stock']}")
        print("--------------------")


def registrar_producto(productos):
    """
    Registra un producto nuevo en el inventario.
    """
    codigo = input("Ingresa el código del producto: ").strip().upper()

    if not texto_no_vacio(codigo):
        print("El código no puede estar vacío")
        return

    producto_existente = buscar_producto(productos, codigo)

    if producto_existente is not None:
        print("Error: ya existe un producto con ese código")
        return

    nombre = input("Ingresa el nombre del producto: ").strip()

    if not texto_no_vacio(nombre):
        print("El nombre no puede estar vacío")
        return

    precio = pedir_float_positivo("Ingresa el precio: ")
    stock = pedir_int_no_negativo("Ingresa el stock: ")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    print("Producto registrado correctamente")


productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250.0, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500.0, "stock": 5}
]

registrar_producto(productos)

print()
mostrar_productos(productos)
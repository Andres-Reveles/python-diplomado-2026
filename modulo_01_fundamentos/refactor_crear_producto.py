print("=== Refactor: crear producto ===")


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
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    return producto


codigo = pedir_texto_no_vacio("Ingresa el código: ").upper()
nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
precio = pedir_float_positivo("Ingresa el precio: ")
stock = pedir_int_no_negativo("Ingresa el stock: ")

producto = crear_producto(codigo, nombre, precio, stock)

print()
print("Producto creado correctamente")
print(producto)
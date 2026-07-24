print("=== Refactor: entradas de usuario ===")


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


codigo = pedir_texto_no_vacio("Ingresa el código: ").upper()
nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
precio = pedir_float_positivo("Ingresa el precio: ")
stock = pedir_int_no_negativo("Ingresa el stock: ")

producto = {
    "codigo": codigo,
    "nombre": nombre,
    "precio": precio,
    "stock": stock
}

print()
print("Producto capturado correctamente")
print(producto)
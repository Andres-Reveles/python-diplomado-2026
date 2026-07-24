print("=== Refactor: validaciones reutilizables ===")


def texto_no_vacio(texto):
    """
    Valida que un texto no esté vacío.
    """
    return texto.strip() != ""


def numero_positivo(numero):
    """
    Valida que un número sea mayor a cero.
    """
    return numero > 0


def numero_no_negativo(numero):
    """
    Valida que un número sea mayor o igual a cero.
    """
    return numero >= 0


def producto_valido(codigo, nombre, precio, stock):
    """
    Valida los datos básicos de un producto.
    """
    if not texto_no_vacio(codigo):
        print("El código no puede estar vacío")
        return False

    if not texto_no_vacio(nombre):
        print("El nombre no puede estar vacío")
        return False

    if not numero_positivo(precio):
        print("El precio debe ser mayor a cero")
        return False

    if not numero_no_negativo(stock):
        print("El stock no puede ser negativo")
        return False

    return True


codigo = input("Ingresa el código: ").strip().upper()
nombre = input("Ingresa el nombre: ").strip()
precio = float(input("Ingresa el precio: "))
stock = int(input("Ingresa el stock: "))

if producto_valido(codigo, nombre, precio, stock):
    print("Producto válido")
else:
    print("Producto inválido")
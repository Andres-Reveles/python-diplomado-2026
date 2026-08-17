print("=== Funciones seguras ===")


def convertir_a_entero(valor):
    """
    Intenta convertir un valor a entero.
    Si no puede, retorna None.
    """
    try:
        return int(valor)

    except ValueError:
        return None


def convertir_a_decimal(valor):
    """
    Intenta convertir un valor a decimal.
    Si no puede, retorna None.
    """
    try:
        return float(valor)

    except ValueError:
        return None


def dividir_seguro(a, b):
    """
    Divide dos números.
    Si el divisor es cero, retorna None.
    """
    try:
        return a / b

    except ZeroDivisionError:
        return None


edad_texto = input("Ingresa tu edad: ")
edad = convertir_a_entero(edad_texto)

if edad is None:
    print("Edad inválida")
else:
    print(f"Edad registrada: {edad}")


precio_texto = input("Ingresa un precio: ")
precio = convertir_a_decimal(precio_texto)

if precio is None:
    print("Precio inválido")
else:
    print(f"Precio registrado: ${precio}")


resultado = dividir_seguro(10, 0)

if resultado is None:
    print("No se pudo realizar la división")
else:
    print(f"Resultado: {resultado}")
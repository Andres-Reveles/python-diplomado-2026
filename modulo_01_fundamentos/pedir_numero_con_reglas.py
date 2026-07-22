print("=== Pedir números con reglas de negocio ===")


def pedir_float_positivo(mensaje):
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


precio = pedir_float_positivo("Ingresa el precio del producto: ")
stock = pedir_int_no_negativo("Ingresa el stock del producto: ")

print()
print("Datos válidos")
print(f"Precio: ${precio}")
print(f"Stock: {stock}")
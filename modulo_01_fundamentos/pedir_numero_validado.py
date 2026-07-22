print("=== Pedir número validado ===")


def pedir_float(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


def pedir_int(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


precio = pedir_float("Ingresa el precio del producto: ")
stock = pedir_int("Ingresa el stock del producto: ")

print()
print("Datos capturados correctamente")
print(f"Precio: ${precio}")
print(f"Stock: {stock}")
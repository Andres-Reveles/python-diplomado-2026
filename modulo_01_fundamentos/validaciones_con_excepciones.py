print("=== Validaciones con excepciones ===")


def pedir_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def pedir_decimal_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número decimal válido")


cantidad = pedir_entero_positivo("Ingresa la cantidad de productos: ")
precio = pedir_decimal_positivo("Ingresa el precio unitario: ")

total = cantidad * precio

print()
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio}")
print(f"Total: ${total}")
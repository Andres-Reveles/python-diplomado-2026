print("=== Pedir números seguros ===")


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def pedir_decimal(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número decimal válido")


edad = pedir_entero("Ingresa tu edad: ")
estatura = pedir_decimal("Ingresa tu estatura: ")

print()
print(f"Edad registrada: {edad}")
print(f"Estatura registrada: {estatura}")
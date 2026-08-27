def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


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
            print("Error: debes ingresar un número válido")


def confirmar_accion(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta == "s":
            return True

        if respuesta == "n":
            return False

        print("Error: responde solamente con S o N")
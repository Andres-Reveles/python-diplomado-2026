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


def pedir_entero_positivo(mensaje):
    """
    Pide un número entero mayor a cero.
    """
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


def confirmar_accion(mensaje):
    """
    Pide confirmación con S/N.
    """
    while True:
        respuesta = input(mensaje).strip().lower()

        if respuesta == "s":
            return True

        if respuesta == "n":
            return False

        print("Error: responde solamente con S o N")
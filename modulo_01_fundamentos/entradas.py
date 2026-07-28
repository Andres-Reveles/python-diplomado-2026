def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


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


def pedir_float_rango(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero < minimo or numero > maximo:
                print(f"Error: el número debe estar entre {minimo} y {maximo}")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")
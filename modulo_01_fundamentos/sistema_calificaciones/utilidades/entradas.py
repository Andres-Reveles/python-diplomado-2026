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


def pedir_float_rango(mensaje, minimo, maximo):
    """
    Pide un número decimal dentro de un rango.
    """
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
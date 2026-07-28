def texto_no_vacio(texto):
    return texto.strip() != ""


def numero_positivo(numero):
    return numero > 0


def numero_no_negativo(numero):
    return numero >= 0


def calificacion_valida(calificacion):
    return calificacion >= 0 and calificacion <= 10
import json


def guardar_datos(nombre_archivo, datos):
    """
    Guarda datos en un archivo JSON.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_datos(nombre_archivo):
    """
    Carga datos desde un archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

    except FileNotFoundError:
        print(f"No existe {nombre_archivo}. Se iniciará con lista vacía.")
        datos = []

    return datos
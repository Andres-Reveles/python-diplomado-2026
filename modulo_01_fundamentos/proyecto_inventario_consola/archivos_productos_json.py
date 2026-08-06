import json


def guardar_productos_json(productos, nombre_archivo):
    """
    Guarda una lista de productos en un archivo JSON.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


def cargar_productos_json(nombre_archivo):
    """
    Carga productos desde un archivo JSON.

    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            productos = json.load(archivo)

    except FileNotFoundError:
        print(f"No existe {nombre_archivo}. Se iniciará con inventario vacío.")
        productos = []

    return productos
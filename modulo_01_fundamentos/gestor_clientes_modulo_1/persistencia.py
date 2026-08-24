import json
import os


def guardar_datos(nombre_archivo, datos):
    """
    Guarda datos en un archivo JSON de forma segura.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"Archivo guardado en: {os.path.abspath(nombre_archivo)}")

    except OSError:
        print(f"Error: no se pudo guardar el archivo {nombre_archivo}")

    finally:
        print("Intento de guardado finalizado")


def cargar_datos(nombre_archivo):
    """
    Carga datos desde un archivo JSON de forma segura.
    Si el archivo no existe o está dañado, retorna una lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos

    except FileNotFoundError:
        print(f"No existe {nombre_archivo}. Se iniciará con lista vacía.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {nombre_archivo} no tiene formato JSON válido.")
        return []

    except OSError:
        print(f"Error: no se pudo leer el archivo {nombre_archivo}.")
        return []

    finally:
        print(f"Intento de lectura finalizado: {nombre_archivo}")
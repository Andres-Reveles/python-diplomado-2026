import json

print("=== Lectura segura de JSON ===")


def cargar_json_seguro(nombre_archivo):
    """
    Carga información desde un archivo JSON.
    Si ocurre un error, retorna una lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        return datos

    except FileNotFoundError:
        print("Error: el archivo no existe")
        return []

    except json.JSONDecodeError:
        print("Error: el archivo no tiene formato JSON válido")
        return []

    finally:
        print("Intento de lectura finalizado")


productos = cargar_json_seguro("productos_prueba_segura.json")

print()
print("Datos cargados:")
print(productos)
import json
import os
from cuenta_bancaria import CuentaBancaria


def convertir_cuentas_a_diccionarios(cuentas):
    """
    Convierte una lista de objetos CuentaBancaria
    a una lista de diccionarios.
    """
    return [cuenta.convertir_a_diccionario() for cuenta in cuentas]


def convertir_diccionarios_a_cuentas(datos):
    """
    Convierte una lista de diccionarios
    a una lista de objetos CuentaBancaria.
    """
    cuentas = []

    for dato in datos:
        cuenta = CuentaBancaria(
            dato["numero_cuenta"],
            dato["titular"],
            float(dato["saldo"])
        )

        cuenta.activa = dato.get("activa", True)

        cuentas.append(cuenta)

    return cuentas


def guardar_cuentas(nombre_archivo, cuentas):
    """
    Guarda cuentas bancarias en un archivo JSON.
    """
    try:
        datos = convertir_cuentas_a_diccionarios(cuentas)

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        print(f"Archivo guardado en: {os.path.abspath(nombre_archivo)}")

    except OSError:
        print(f"Error: no se pudo guardar el archivo {nombre_archivo}")

    finally:
        print("Intento de guardado finalizado")


def cargar_cuentas(nombre_archivo):
    """
    Carga cuentas bancarias desde un archivo JSON.
    Si el archivo no existe o está dañado, retorna lista vacía.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        cuentas = convertir_diccionarios_a_cuentas(datos)

        return cuentas

    except FileNotFoundError:
        print(f"No existe {nombre_archivo}. Se iniciará con lista vacía.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {nombre_archivo} no tiene formato JSON válido.")
        return []

    except KeyError:
        print(f"Error: {nombre_archivo} no tiene la estructura esperada.")
        return []

    except OSError:
        print(f"Error: no se pudo leer el archivo {nombre_archivo}.")
        return []

    finally:
        print(f"Intento de lectura finalizado: {nombre_archivo}")
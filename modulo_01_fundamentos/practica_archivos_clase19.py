print("=== Clase 19 - Práctica corta con archivos ===")


def crear_archivo_bitacora(nombre_archivo):
    """
    Crea una bitácora desde cero.
    Si el archivo ya existe, su contenido se reemplaza.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("=== Bitácora de práctica con archivos ===\n")


def agregar_evento(nombre_archivo, evento):
    """
    Agrega un evento al final del archivo.
    """
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(evento + "\n")


def leer_bitacora(nombre_archivo):
    """
    Lee y muestra todo el contenido de la bitácora.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

    print("=== Contenido de la bitácora ===")
    print(contenido)


def contar_eventos(nombre_archivo):
    """
    Cuenta cuántas líneas tiene el archivo.
    """
    contador = 0

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() != "":
                contador += 1

    return contador


nombre_archivo = "bitacora_clase19.txt"

crear_archivo_bitacora(nombre_archivo)

agregar_evento(nombre_archivo, "Repasé escritura de archivos TXT.")
agregar_evento(nombre_archivo, "Repasé lectura de archivos TXT.")
agregar_evento(nombre_archivo, "Practiqué funciones para manejar archivos.")
agregar_evento(nombre_archivo, "Preparé el camino para CSV y JSON.")

leer_bitacora(nombre_archivo)

total_eventos = contar_eventos(nombre_archivo)

print(f"Total de líneas registradas: {total_eventos}")
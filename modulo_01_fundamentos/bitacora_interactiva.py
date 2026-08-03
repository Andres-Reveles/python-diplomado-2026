print("=== Bitácora interactiva ===")


def agregar_evento(nombre_archivo, evento):
    """
    Agrega un evento al final del archivo.
    """
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(evento + "\n")


def leer_bitacora(nombre_archivo):
    """
    Lee y muestra el contenido de la bitácora.
    """
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        if contenido.strip() == "":
            print("La bitácora está vacía")
        else:
            print("=== Contenido de la bitácora ===")
            print(contenido)

    except FileNotFoundError:
        print("Todavía no existe la bitácora")


def contar_eventos(nombre_archivo):
    """
    Cuenta los eventos registrados en la bitácora.
    """
    contador = 0

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() != "":
                    contador += 1

    except FileNotFoundError:
        return 0

    return contador


nombre_archivo = "bitacora_interactiva.txt"

while True:
    print()
    print("1. Agregar evento")
    print("2. Ver bitácora")
    print("3. Contar eventos")
    print("4. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        evento = input("Escribe el evento: ").strip()

        if evento == "":
            print("El evento no puede estar vacío")
        else:
            agregar_evento(nombre_archivo, evento)
            print("Evento guardado correctamente")

    elif opcion == "2":
        leer_bitacora(nombre_archivo)

    elif opcion == "3":
        total = contar_eventos(nombre_archivo)
        print(f"Total de eventos registrados: {total}")

    elif opcion == "4":
        print("Saliendo de la bitácora")
        break

    else:
        print("Opción inválida")
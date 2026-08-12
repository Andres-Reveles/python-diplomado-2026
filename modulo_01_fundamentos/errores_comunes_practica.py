print("=== Práctica de errores comunes ===")


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def division_segura():
    print()
    print("=== División segura ===")

    numero_1 = pedir_entero("Ingresa el primer número: ")
    numero_2 = pedir_entero("Ingresa el segundo número: ")

    try:
        resultado = numero_1 / numero_2
        print(f"Resultado: {resultado}")

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")


def elegir_producto():
    print()
    print("=== Elegir producto ===")

    productos = ["Mouse", "Teclado", "Monitor"]

    print("Productos disponibles:")

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. {producto}")

    opcion = pedir_entero("Elige el número del producto: ")

    try:
        producto_elegido = productos[opcion - 1]
        print(f"Producto elegido: {producto_elegido}")

    except IndexError:
        print("Error: elegiste una opción que no existe")


def mostrar_dato_producto():
    print()
    print("=== Mostrar dato de producto ===")

    producto = {
        "codigo": "P001",
        "nombre": "Mouse",
        "precio": 250.0
    }

    clave = input("¿Qué dato quieres ver? codigo/nombre/precio/stock: ").strip().lower()

    try:
        print(f"{clave}: {producto[clave]}")

    except KeyError:
        print("Error: ese dato no existe en el producto")


def leer_archivo():
    print()
    print("=== Leer archivo ===")

    nombre_archivo = input("Ingresa el nombre del archivo a leer: ").strip()

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        print("Contenido del archivo:")
        print(contenido)

    except FileNotFoundError:
        print("Error: el archivo no existe")


def mostrar_menu():
    print()
    print("1. División segura")
    print("2. Elegir producto")
    print("3. Mostrar dato de producto")
    print("4. Leer archivo")
    print("5. Salir")


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        division_segura()

    elif opcion == "2":
        elegir_producto()

    elif opcion == "3":
        mostrar_dato_producto()

    elif opcion == "4":
        leer_archivo()

    elif opcion == "5":
        print("Saliendo del programa")
        break

    else:
        print("Opción inválida")
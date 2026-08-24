import json


ARCHIVO_PRODUCTOS = "productos_evaluacion.json"


def cargar_productos():
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            productos = json.load(archivo)

        return productos

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: el archivo JSON está dañado")
        return []


def guardar_productos(productos):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        json.dump(productos, archivo, indent=4, ensure_ascii=False)


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


def pedir_float_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


def pedir_int_no_negativo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)

            if numero < 0:
                print("Error: el número no puede ser negativo")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def registrar_producto(productos):
    codigo = pedir_texto_no_vacio("Código: ").upper()

    producto_existente = buscar_producto(productos, codigo)

    if producto_existente is not None:
        print("Error: ya existe un producto con ese código")
        return

    nombre = pedir_texto_no_vacio("Nombre: ")
    precio = pedir_float_positivo("Precio: ")
    stock = pedir_int_no_negativo("Stock: ")

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)

    print("Producto registrado correctamente")


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for producto in productos:
        print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def buscar_producto_menu(productos):
    codigo = pedir_texto_no_vacio("Código a buscar: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado:")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


def mostrar_reporte(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    total_productos = len(productos)
    stock_total = sum(producto["stock"] for producto in productos)
    valor_total = sum(producto["precio"] * producto["stock"] for producto in productos)

    print("=== Reporte de productos ===")
    print(f"Total de productos registrados: {total_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total del inventario: ${valor_total}")


def mostrar_menu():
    print()
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Reporte")
    print("5. Guardar")
    print("6. Salir")


productos = cargar_productos()


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_producto(productos)

    elif opcion == "2":
        mostrar_productos(productos)

    elif opcion == "3":
        buscar_producto_menu(productos)

    elif opcion == "4":
        mostrar_reporte(productos)

    elif opcion == "5":
        guardar_productos(productos)
        print("Productos guardados correctamente")

    elif opcion == "6":
        guardar_productos(productos)
        print("Productos guardados correctamente")
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
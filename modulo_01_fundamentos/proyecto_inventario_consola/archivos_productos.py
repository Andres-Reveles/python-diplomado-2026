from producto import crear_producto


def guardar_productos_txt(productos, nombre_archivo):
    """
    Guarda una lista de productos en un archivo TXT.
    """
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for producto in productos:
            linea = f"{producto['codigo']}|{producto['nombre']}|{producto['precio']}|{producto['stock']}\n"
            archivo.write(linea)


def cargar_productos_txt(nombre_archivo):
    """
    Carga productos desde un archivo TXT.

    Si el archivo no existe, retorna una lista vacía.
    """
    productos = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                if linea == "":
                    continue

                datos = linea.split("|")

                codigo = datos[0]
                nombre = datos[1]
                precio = float(datos[2])
                stock = int(datos[3])

                producto = crear_producto(codigo, nombre, precio, stock)

                productos.append(producto)

    except FileNotFoundError:
        print(f"No existe {nombre_archivo}. Se iniciará con inventario vacío.")

    return productos
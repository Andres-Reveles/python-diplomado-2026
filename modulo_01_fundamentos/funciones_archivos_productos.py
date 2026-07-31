print("=== Funciones para guardar y cargar productos ===")


def crear_producto(codigo, nombre, precio, stock):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }


def guardar_productos_txt(productos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for producto in productos:
            linea = f"{producto['codigo']}|{producto['nombre']}|{producto['precio']}|{producto['stock']}\n"
            archivo.write(linea)


def cargar_productos_txt(nombre_archivo):
    productos = []

    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            datos = linea.split("|")

            codigo = datos[0]
            nombre = datos[1]
            precio = float(datos[2])
            stock = int(datos[3])

            producto = crear_producto(codigo, nombre, precio, stock)

            productos.append(producto)

    return productos


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for producto in productos:
        print(f"Código: {producto['codigo']}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']}")
        print(f"Stock: {producto['stock']}")
        print("--------------------")


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2)
]

guardar_productos_txt(productos, "productos_funciones.txt")

print("Productos guardados correctamente")

productos_cargados = cargar_productos_txt("productos_funciones.txt")

print()
print("Productos cargados desde archivo:")
mostrar_productos(productos_cargados)
print("=== Inventario refactorizado ===")


def mostrar_menu():
    print()
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Actualizar precio")
    print("5. Actualizar stock")
    print("6. Eliminar producto")
    print("7. Reporte general")
    print("8. Filtrar productos")
    print("9. Ordenar productos")
    print("10. Salir")


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


def confirmar_accion(mensaje):
    respuesta = input(mensaje).strip().lower()
    return respuesta == "si" or respuesta == "sí"


def crear_producto(codigo, nombre, precio, stock):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def codigo_disponible(productos, codigo):
    producto = buscar_producto(productos, codigo)
    return producto is None


def pedir_producto_existente(productos):
    codigo = pedir_texto_no_vacio("Ingresa el código del producto: ").upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return None

    return producto


def mostrar_producto(producto):
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"Producto {indice}")
        mostrar_producto(producto)
        print("--------------------")


def mostrar_producto_resumen(producto):
    print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def mostrar_productos_resumen(productos):
    if len(productos) == 0:
        print("No hay productos para mostrar")
        return

    for producto in productos:
        mostrar_producto_resumen(producto)


def registrar_producto(productos):
    codigo = pedir_texto_no_vacio("Ingresa el código: ").upper()

    if not codigo_disponible(productos, codigo):
        print("Error: ya existe un producto con ese código")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
    precio = pedir_float_positivo("Ingresa el precio: ")
    stock = pedir_int_no_negativo("Ingresa el stock: ")

    producto = crear_producto(codigo, nombre, precio, stock)

    productos.append(producto)
    print("Producto registrado correctamente")


def buscar_producto_menu(productos):
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado:")
    mostrar_producto(producto)


def actualizar_precio(productos):
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio actual: ${producto['precio']}")

    nuevo_precio = pedir_float_positivo("Ingresa el nuevo precio: ")

    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente")


def actualizar_stock(productos):
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Stock actual: {producto['stock']}")

    nuevo_stock = pedir_int_no_negativo("Ingresa el nuevo stock: ")

    producto["stock"] = nuevo_stock
    print("Stock actualizado correctamente")


def eliminar_producto(productos):
    producto = pedir_producto_existente(productos)

    if producto is None:
        return

    print("Producto encontrado:")
    mostrar_producto(producto)

    confirmado = confirmar_accion("¿Seguro que deseas eliminarlo? Escribe si o no: ")

    if confirmado:
        productos.remove(producto)
        print("Producto eliminado correctamente")
    else:
        print("Eliminación cancelada")


def calcular_stock_total(productos):
    return sum(producto["stock"] for producto in productos)


def calcular_valor_total(productos):
    return sum(producto["precio"] * producto["stock"] for producto in productos)


def obtener_producto_mas_caro(productos):
    return max(productos, key=lambda producto: producto["precio"])


def obtener_producto_mas_barato(productos):
    return min(productos, key=lambda producto: producto["precio"])


def hay_productos_sin_stock(productos):
    return any(producto["stock"] == 0 for producto in productos)


def todos_tienen_precio_valido(productos):
    return all(producto["precio"] > 0 for producto in productos)


def mostrar_reporte_general(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    cantidad_productos = len(productos)
    stock_total = calcular_stock_total(productos)
    valor_total = calcular_valor_total(productos)

    producto_mas_caro = obtener_producto_mas_caro(productos)
    producto_mas_barato = obtener_producto_mas_barato(productos)

    print("=== Reporte general ===")
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total del inventario: ${valor_total}")

    print()
    print("Producto más caro:")
    mostrar_producto_resumen(producto_mas_caro)

    print()
    print("Producto más barato:")
    mostrar_producto_resumen(producto_mas_barato)

    print()
    print(f"¿Hay productos sin stock?: {hay_productos_sin_stock(productos)}")
    print(f"¿Todos tienen precio válido?: {todos_tienen_precio_valido(productos)}")


def obtener_productos_disponibles(productos):
    return [
        producto for producto in productos
        if producto["stock"] > 0
    ]


def obtener_productos_sin_stock(productos):
    return [
        producto for producto in productos
        if producto["stock"] == 0
    ]


def obtener_productos_caros(productos, precio_minimo=500):
    return [
        producto for producto in productos
        if producto["precio"] > precio_minimo
    ]


def obtener_productos_baratos(productos, precio_maximo=500):
    return [
        producto for producto in productos
        if producto["precio"] <= precio_maximo
    ]


def ordenar_por_precio(productos, descendente=False):
    return sorted(
        productos,
        key=lambda producto: producto["precio"],
        reverse=descendente
    )


def ordenar_por_stock(productos, descendente=False):
    return sorted(
        productos,
        key=lambda producto: producto["stock"],
        reverse=descendente
    )


def ordenar_por_nombre(productos):
    return sorted(
        productos,
        key=lambda producto: producto["nombre"].lower()
    )


def filtrar_productos_menu(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Filtros ===")
    print("1. Productos disponibles")
    print("2. Productos sin stock")
    print("3. Productos caros")
    print("4. Productos baratos")

    opcion = input("Elige una opción de filtro: ").strip()

    if opcion == "1":
        resultado = obtener_productos_disponibles(productos)
        print("=== Productos disponibles ===")

    elif opcion == "2":
        resultado = obtener_productos_sin_stock(productos)
        print("=== Productos sin stock ===")

    elif opcion == "3":
        resultado = obtener_productos_caros(productos)
        print("=== Productos caros ===")

    elif opcion == "4":
        resultado = obtener_productos_baratos(productos)
        print("=== Productos baratos ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_resumen(resultado)


def ordenar_productos_menu(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Ordenar productos ===")
    print("1. Precio menor a mayor")
    print("2. Precio mayor a menor")
    print("3. Stock menor a mayor")
    print("4. Stock mayor a menor")
    print("5. Nombre A-Z")

    opcion = input("Elige una opción de ordenamiento: ").strip()

    if opcion == "1":
        resultado = ordenar_por_precio(productos)
        print("=== Precio menor a mayor ===")

    elif opcion == "2":
        resultado = ordenar_por_precio(productos, descendente=True)
        print("=== Precio mayor a menor ===")

    elif opcion == "3":
        resultado = ordenar_por_stock(productos)
        print("=== Stock menor a mayor ===")

    elif opcion == "4":
        resultado = ordenar_por_stock(productos, descendente=True)
        print("=== Stock mayor a menor ===")

    elif opcion == "5":
        resultado = ordenar_por_nombre(productos)
        print("=== Nombre A-Z ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_resumen(resultado)


productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2),
    crear_producto("P004", "Webcam", 850.0, 0),
    crear_producto("P005", "USB", 120.0, 20)
]


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
        actualizar_precio(productos)

    elif opcion == "5":
        actualizar_stock(productos)

    elif opcion == "6":
        eliminar_producto(productos)

    elif opcion == "7":
        mostrar_reporte_general(productos)

    elif opcion == "8":
        filtrar_productos_menu(productos)

    elif opcion == "9":
        ordenar_productos_menu(productos)

    elif opcion == "10":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
print("=== Inventario con funciones ===")


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


def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return producto

    return None


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    print("=== Productos registrados ===")

    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. Código: {producto['codigo']}")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: ${producto['precio']}")
        print(f"   Stock: {producto['stock']}")
        print("--------------------")


def mostrar_productos_simple(productos):
    if len(productos) == 0:
        print("No hay productos para mostrar")
        return

    for producto in productos:
        print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']} - Stock: {producto['stock']}")


def registrar_producto(productos):
    codigo = input("Ingresa el código del producto: ").strip().upper()

    if codigo == "":
        print("El código no puede estar vacío")
        return

    producto_existente = buscar_producto(productos, codigo)

    if producto_existente is not None:
        print("Error: ya existe un producto con ese código")
        return

    nombre = input("Ingresa el nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío")
        return

    precio = float(input("Ingresa el precio: "))
    stock = int(input("Ingresa el stock: "))

    if precio <= 0:
        print("El precio debe ser mayor a cero")
        return

    if stock < 0:
        print("El stock no puede ser negativo")
        return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    productos.append(producto)
    print("Producto registrado correctamente")


def buscar_producto_menu(productos):
    codigo = input("Ingresa el código del producto: ").strip().upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")


def actualizar_precio(productos):
    codigo = input("Ingresa el código del producto: ").strip().upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio actual: ${producto['precio']}")

    nuevo_precio = float(input("Ingresa el nuevo precio: "))

    if nuevo_precio <= 0:
        print("El precio debe ser mayor a cero")
        return

    producto["precio"] = nuevo_precio
    print("Precio actualizado correctamente")


def actualizar_stock(productos):
    codigo = input("Ingresa el código del producto: ").strip().upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado")
    print(f"Nombre: {producto['nombre']}")
    print(f"Stock actual: {producto['stock']}")

    nuevo_stock = int(input("Ingresa el nuevo stock: "))

    if nuevo_stock < 0:
        print("El stock no puede ser negativo")
        return

    producto["stock"] = nuevo_stock
    print("Stock actualizado correctamente")


def eliminar_producto(productos):
    codigo = input("Ingresa el código del producto a eliminar: ").strip().upper()

    producto = buscar_producto(productos, codigo)

    if producto is None:
        print("Producto no encontrado")
        return

    print("Producto encontrado")
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']}")
    print(f"Stock: {producto['stock']}")

    confirmacion = input("¿Seguro que deseas eliminarlo? Escribe si o no: ").strip().lower()

    if confirmacion == "si" or confirmacion == "sí":
        productos.remove(producto)
        print("Producto eliminado correctamente")
    else:
        print("Eliminación cancelada")


def mostrar_reporte_general(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    cantidad_productos = len(productos)
    stock_total = sum(producto["stock"] for producto in productos)
    valor_total = sum(producto["precio"] * producto["stock"] for producto in productos)

    producto_mas_caro = max(productos, key=lambda producto: producto["precio"])
    producto_mas_barato = min(productos, key=lambda producto: producto["precio"])

    hay_productos_sin_stock = any(producto["stock"] == 0 for producto in productos)
    todos_tienen_precio_valido = all(producto["precio"] > 0 for producto in productos)

    print("=== Reporte general ===")
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total del inventario: ${valor_total}")

    print()
    print("Producto más caro:")
    print(f"{producto_mas_caro['codigo']} - {producto_mas_caro['nombre']} - ${producto_mas_caro['precio']}")

    print()
    print("Producto más barato:")
    print(f"{producto_mas_barato['codigo']} - {producto_mas_barato['nombre']} - ${producto_mas_barato['precio']}")

    print()
    print(f"¿Hay productos sin stock?: {hay_productos_sin_stock}")
    print(f"¿Todos tienen precio válido?: {todos_tienen_precio_valido}")


def filtrar_productos(productos):
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
        productos_filtrados = [
            producto for producto in productos
            if producto["stock"] > 0
        ]
        print("=== Productos disponibles ===")

    elif opcion == "2":
        productos_filtrados = [
            producto for producto in productos
            if producto["stock"] == 0
        ]
        print("=== Productos sin stock ===")

    elif opcion == "3":
        productos_filtrados = [
            producto for producto in productos
            if producto["precio"] > 500
        ]
        print("=== Productos caros ===")

    elif opcion == "4":
        productos_filtrados = [
            producto for producto in productos
            if producto["precio"] <= 500
        ]
        print("=== Productos baratos ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_simple(productos_filtrados)


def ordenar_productos(productos):
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
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["precio"]
        )
        print("=== Productos por precio menor a mayor ===")

    elif opcion == "2":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["precio"],
            reverse=True
        )
        print("=== Productos por precio mayor a menor ===")

    elif opcion == "3":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["stock"]
        )
        print("=== Productos por stock menor a mayor ===")

    elif opcion == "4":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["stock"],
            reverse=True
        )
        print("=== Productos por stock mayor a menor ===")

    elif opcion == "5":
        productos_ordenados = sorted(
            productos,
            key=lambda producto: producto["nombre"].lower()
        )
        print("=== Productos por nombre A-Z ===")

    else:
        print("Opción inválida")
        return

    mostrar_productos_simple(productos_ordenados)


productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250.0, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500.0, "stock": 5},
    {"codigo": "P003", "nombre": "Monitor", "precio": 3200.0, "stock": 2},
    {"codigo": "P004", "nombre": "Webcam", "precio": 850.0, "stock": 0},
    {"codigo": "P005", "nombre": "USB", "precio": 120.0, "stock": 20}
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
        filtrar_productos(productos)

    elif opcion == "9":
        ordenar_productos(productos)

    elif opcion == "10":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
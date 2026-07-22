#tendra un menu 
#1. Registrar producto
#2. Mostrar productos
#3. Buscar producto
#4. Actualizar precio
#5. Actualizar stock
#6. Eliminar producto
#7. Reporte general
#8. Filtrar productos
#9. Ordenar productos
#10. Salir

print("--- Inventario Mejorado con Reportes ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 190.0, "Stock": 100},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 350.0, "Stock": 50},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1500.0, "Stock": 30},
    {"Codigo": "P004", "Nombre": "Impresora", "Precio": 2500.0, "Stock": 20},
    {"Codigo": "P005", "Nombre": "Auriculares", "Precio": 500.0, "Stock": 80}
]

while True:
    #menu
    print("\n--- Menú ---")
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

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        codigo = input("Ingresa el código del producto: ").strip().upper()

        if codigo == "":
            print("El código no puede estar vacío")
            continue

        existe = any(producto["Codigo"] == codigo for producto in productos)

        if existe:
            print("Error: ya existe un producto con ese código")
        else:
            nombre = input("Ingresa el nombre del producto: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío")
            continue

        precio = float(input("Ingresa el precio: "))
        stock = int(input("Ingresa el stock: "))

        if precio <= 0:
            print("El precio debe ser mayor a cero")
        elif stock < 0:
            print("El stock no puede ser negativo")
        else:
            nuevo_producto = {
                "Codigo": codigo,
                "Nombre": nombre,
                "Precio": precio,
                "Stock": stock
            }

            productos.append(nuevo_producto)
            print("Producto registrado correctamente")
            
    elif opcion == "2":
        
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print()
            print("Productos registrados:")
            
            for indice, producto in enumerate(productos, start=1):
                print(f"{indice}. Código: {producto['Codigo']}, "
                      f"Nombre: {producto['Nombre']}, "
                      f"Precio: {producto['Precio']}, "
                      f"Stock: {producto['Stock']}")
                print("-" * 40)

    elif opcion == "3":
        codigo_buscar = input("Ingresa el código del producto a buscar: ").strip().upper()
        producto_encontrado = next((producto for producto in productos if producto["Codigo"] == codigo_buscar), None)

        if producto_encontrado:
            print(f"Producto encontrado: Código: {producto_encontrado['Codigo']}, "
                  f"Nombre: {producto_encontrado['Nombre']}, "
                  f"Precio: {producto_encontrado['Precio']}, "
                  f"Stock: {producto_encontrado['Stock']}")
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        codigo_actualizar = input("Ingresa el código del producto: ").strip().upper()

        producto_encontrado = next((producto for producto in productos if producto["Codigo"] == codigo_actualizar), None)

        if producto_encontrado is not None:
            print(f"Producto encontrado: Código: {producto_encontrado['Codigo']}, "
                  f"Nombre: {producto_encontrado['Nombre']}, "
                    f"Precio: {producto_encontrado['Precio']}, "
                    f"Stock: {producto_encontrado['Stock']}")
            
            nuevo_precio = float(input("Ingresa el nuevo precio: "))

            if nuevo_precio <= 0:
                print("El precio debe ser mayor a cero")
            else:
                producto_encontrado["Precio"] = nuevo_precio
                print("Precio actualizado correctamente.")
                print(f"Nuevo precio: {producto_encontrado['Precio']}")
        else:
        
            print("Producto no encontrado.")

    elif opcion == "5":

        codigo_buscar = input("Ingresa el código del producto: ").strip().upper()

        producto_encontrado = next((producto for producto in productos if producto["Codigo"] == codigo_buscar), None)

        if producto_encontrado is not None:
            print(f"Producto encontrado: Código: {producto_encontrado['Codigo']}, "
                  f"Nombre: {producto_encontrado['Nombre']}, "
                  f"Precio: {producto_encontrado['Precio']}, "
                  f"Stock: {producto_encontrado['Stock']}")

            nuevo_stock = int(input("Ingresa el nuevo stock: "))

            if nuevo_stock < 0:
                print("El stock no puede ser negativo")
            else:
                producto_encontrado["Stock"] = nuevo_stock
                print("Stock actualizado correctamente.")
                print(f"Nuevo stock: {producto_encontrado['Stock']}")
        else:
            print("Producto no encontrado.")
    
    elif opcion == "6":
        codigo_buscar = input("Ingresa el código del producto a eliminar: ").strip().upper()

        producto_encontrado = next((producto for producto in productos if producto["Codigo"] == codigo_buscar), None)

        if producto_encontrado is not None:
            print(f"Producto encontrado: Código: {producto_encontrado['Codigo']}, "
                  f"Nombre: {producto_encontrado['Nombre']}, "
                  f"Precio: {producto_encontrado['Precio']}, "
                  f"Stock: {producto_encontrado['Stock']}")
            
            confirmacion = input("¿Estás seguro de que deseas eliminar este producto? (s/n): ").strip().lower()

            if confirmacion == "s":
                productos.remove(producto_encontrado)
                print("Producto eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
        else:
            print("Producto no encontrado.")

    elif opcion == "7":
        print("\n--- Reporte General ---")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            cantidad_productos = len(productos)
            total_stock = sum(producto["Stock"] for producto in productos)
            total_valor_inventario = sum(producto["Precio"] * producto["Stock"] for producto in productos)

            producto_mas_caro = max(productos, key=lambda x: x["Precio"])
            producto_mas_barato = min(productos, key=lambda x: x["Precio"])
            producto_mayor_stock = max(productos, key=lambda x: x["Stock"])
            producto_menor_stock = min(productos, key=lambda x: x["Stock"])

            hay_productos_sin_stock = any(producto["Stock"] == 0 for producto in productos)
            todos_tienen_precio_valido = all(producto["Precio"] > 0 for producto in productos)

            print()
            print("--- Reporte General ---")
            print(f"Cantidad de productos registrados: {cantidad_productos}")
            print(f"Total de stock disponible: {total_stock}")
            print(f"Valor total del inventario: {total_valor_inventario}")

            print()
            print("Producto mas caro:")
            print(f"Producto más caro: Código: {producto_mas_caro['Codigo']}, Nombre: {producto_mas_caro['Nombre']}, Precio: {producto_mas_caro['Precio']}")

            print()
            print("Producto mas barato:")
            print(f"Producto más barato: Código: {producto_mas_barato['Codigo']}, Nombre: {producto_mas_barato['Nombre']}, Precio: {producto_mas_barato['Precio']}")

            print()
            print("Producto con mayor stock:")
            print(f"Producto con mayor stock: Código: {producto_mayor_stock['Codigo']}, Nombre: {producto_mayor_stock['Nombre']}, Stock: {producto_mayor_stock['Stock']}")

            print()
            print("Producto con menor stock:")
            print(f"Producto con menor stock: Código: {producto_menor_stock['Codigo']}, Nombre: {producto_menor_stock['Nombre']}, Stock: {producto_menor_stock['Stock']}")

            print()
            print(f"Hay productos sin stock: {'Sí' if hay_productos_sin_stock else 'No'}")
            print(f"Todos los productos tienen un precio válido: {'Sí' if todos_tienen_precio_valido else 'No'}")

    elif opcion == "8":
        print("\n--- Filtrar Productos ---")
        print("1. Filtrar por productos disponibles")
        print("2. Filtrar por productos sin stock")
        print("3. Filtrar por productos caros")
        print("4. Filtrar por productos baratos")

        opcion_filtro = input("Seleccione una opción de filtro: ")

        if opcion_filtro == "1":
            productos_filtrados = [producto for producto in productos if producto["Stock"] > 0]

            print("\n--- Productos Disponibles ---")
            for producto in productos_filtrados:
                print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

        elif opcion_filtro == "2":
            productos_filtrados = [producto for producto in productos if producto["Stock"] == 0]

            print("\n--- Productos Sin Stock ---")
            for producto in productos_filtrados:
                print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

        elif opcion_filtro == "3":
            precio_minimo = float(input("Ingrese el precio mínimo para filtrar productos caros: "))
            productos_filtrados = [producto for producto in productos if producto["Precio"] >= precio_minimo]

            print(f"\n--- Productos Caros (Precio >= {precio_minimo}) ---")
            for producto in productos_filtrados:
                print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

        elif opcion_filtro == "4":
            precio_maximo = float(input("Ingrese el precio máximo para filtrar productos baratos: "))
            productos_filtrados = [producto for producto in productos if producto["Precio"] <= precio_maximo]

            print(f"\n--- Productos Baratos (Precio <= {precio_maximo}) ---")
            for producto in productos_filtrados:
                print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

        else:
            print("Opción de filtro inválida.")

    elif opcion == "9":

        if len(productos) == 0:
            print("No hay productos registrados para ordenar.")
        else:
            print("\n--- Ordenar Productos ---")
            print("1. Ordenar por precio (ascendente)")
            print("2. Ordenar por precio (descendente)")
            print("3. Ordenar por stock (ascendente)")
            print("4. Ordenar por stock (descendente)")
            print("5. Ordenar por nombre (A-Z)")

            opcion_orden = input("Seleccione una opción de ordenamiento: ")

            if opcion_orden == "1":
                productos_ordenados = sorted(productos, key=lambda x: x["Precio"])
                for producto in productos_ordenados:
                    print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

            elif opcion_orden == "2":
                productos_ordenados = sorted(productos, key=lambda x: x["Precio"], reverse=True)
                for producto in productos_ordenados:
                    print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

            elif opcion_orden == "3":
                productos_ordenados = sorted(productos, key=lambda x: x["Stock"])
                for producto in productos_ordenados:
                    print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

            elif opcion_orden == "4":
                productos_ordenados = sorted(productos, key=lambda x: x["Stock"], reverse=True)
                for producto in productos_ordenados:
                    print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")

            elif opcion_orden == "5":
                productos_ordenados = sorted(productos, key=lambda x: x["Nombre"])
                for producto in productos_ordenados:
                    print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}    ")

            else:
                print("Opción de ordenamiento inválida.")
                continue

    elif opcion == "10":
        print("Saliendo del programa...")
        break
    
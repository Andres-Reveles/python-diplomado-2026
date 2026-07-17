print("--- Inventario Básico ---")

productos = []

while True:

    print()
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código")
    print("4. Actualizar precio")
    print("5. Actualizar stock")
    print("6. Eliminar producto")
    print("7. Calcular valor total del inventario")
    print("8. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        codigo = input("Ingrese el código del producto: ").strip().upper()

        if codigo == "":
            print("El código no puede estar vacío.")
            continue

        existe = False

        for producto in productos:
            if producto["Codigo"] == codigo:
                existe = True
                break
        
        if existe:
            print("Error, ya existe el producto.")
        else:
            nombre = input("Ingrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio del producto: "))
            stock = int(input("Ingrese el stock del producto: "))

            if nombre == "":
                print("El nombre no puede estar vacío.")
            elif precio < 0:
                print("El precio no puede ser negativo.")
            elif stock < 0:
                print("El stock no puede ser negativo.")
            else:
                producto = {
                    "Codigo": codigo,
                    "Nombre": nombre,
                    "Precio": precio,
                    "Stock": stock
                }

                productos.append(producto)
                print("Producto registrado exitosamente.")
        
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("Productos registrados:")
            for indice, producto in enumerate(productos):
                print(f"{indice}. Código: {producto['Codigo']}")
                print(f"Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")
    
    elif opcion == "3":

        codigo_buscar = input("Ingrese el código del producto a buscar: ").strip().upper()

        encontrado = False

        for producto in productos:
            if producto["Codigo"] == codigo_buscar:
                print(f"Producto encontrado: Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    
    elif opcion == "4":
        codigo_buscar = input("Ingrese el código del producto para actualizar el precio: ").strip().upper()

        encontrado = False

        for producto in productos:
            if producto["Codigo"] == codigo_buscar:
                print(f"Producto encontrado")
                print(f"Precio actual: {producto['Precio']}")

                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                
                if nuevo_precio <= 0:
                    print("El precio debe ser mayor a cero.")
                else:
                    producto["Precio"] = nuevo_precio
                    print("Precio actualizado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "5":
        codigo_buscar = input("Ingrese el código del producto para actualizar el stock: ").strip().upper()

        encontrado = False

        for producto in productos:
            if producto["Codigo"] == codigo_buscar:
                print(f"Producto encontrado")
                print(f"Stock actual: {producto['Stock']}")

                nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
                
                if nuevo_stock < 0:
                    print("El stock no puede ser negativo.")
                else:
                    producto["Stock"] = nuevo_stock
                    print("Stock actualizado exitosamente.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "6":
        codigo_buscar = input("Ingrese el código del producto a eliminar: ").strip().upper()

        encontrado = False

        for indice, producto in enumerate(productos):
            if producto["Codigo"] == codigo_buscar:
                print(f"Producto encontrado: Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}, Stock: {producto['Stock']}")
                confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().lower()
                if confirmacion == "s":
                    productos.pop(indice)
                    print("Producto eliminado exitosamente.")
                else:
                    print("Eliminación cancelada.")
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado.")
    elif opcion == "7":
        if len(productos) == 0:
            print("No hay productos registrados.") 
        else:
            valor_total = 0

            print("Valor total del inventario:")
            for producto in productos:
                valor_producto = producto["Precio"] * producto["Stock"]
                valor_total += valor_producto
                print(f"Código: {producto['Codigo']}, Nombre: {producto['Nombre']}, Valor: {valor_producto}")
            print(f"Valor total del inventario: {valor_total}")
    
    elif opcion == "8":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


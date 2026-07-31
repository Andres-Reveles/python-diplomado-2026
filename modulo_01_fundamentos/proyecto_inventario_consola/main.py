from inventario_servicio import (
    mostrar_productos,
    registrar_producto,
    buscar_producto_menu,
    actualizar_precio,
    actualizar_stock,
    eliminar_producto
)
from reportes import (
    mostrar_reporte_general,
    obtener_productos_disponibles,
    obtener_productos_sin_stock,
    obtener_productos_caros,
    obtener_productos_baratos,
    ordenar_por_precio,
    ordenar_por_stock,
    ordenar_por_nombre,
    mostrar_productos_resumen
)
from archivos_productos import cargar_productos_txt, guardar_productos_txt


NOMBRE_ARCHIVO = "productos_inventario.txt"


print("=== Proyecto inventario de productos con persistencia TXT ===")


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
    print("10. Guardar cambios")
    print("11. Salir")


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


productos = cargar_productos_txt(NOMBRE_ARCHIVO)


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
        guardar_productos_txt(productos, NOMBRE_ARCHIVO)
        print("Cambios guardados correctamente")

    elif opcion == "11":
        guardar_productos_txt(productos, NOMBRE_ARCHIVO)
        print("Cambios guardados correctamente")
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
from producto import crear_producto
from producto_servicio import (
    mostrar_productos,
    registrar_producto,
    buscar_producto_menu
)
from venta_servicio import registrar_venta, mostrar_ventas
from persistencia import guardar_datos, cargar_datos
from reportes import mostrar_reporte_ventas, mostrar_ventas_resumen


ARCHIVO_PRODUCTOS = "productos_sistema_ventas.json"
ARCHIVO_VENTAS = "ventas_sistema_ventas.json"


print("=== Sistema de ventas con persistencia básica ===")


def mostrar_menu():
    print()
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Registrar venta")
    print("5. Mostrar ventas")
    print("6. Mostrar ventas resumidas")
    print("7. Reporte general de ventas")
    print("8. Guardar cambios")
    print("9. Salir")


productos = cargar_datos(ARCHIVO_PRODUCTOS)
ventas = cargar_datos(ARCHIVO_VENTAS)

if len(productos) == 0:
    productos = [
        crear_producto("P001", "Mouse", 250.0, 10),
        crear_producto("P002", "Teclado", 500.0, 5),
        crear_producto("P003", "Monitor", 3200.0, 2)
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
        registrar_venta(productos, ventas)

    elif opcion == "5":
        mostrar_ventas(ventas)

    elif opcion == "6":
        mostrar_ventas_resumen(ventas)

    elif opcion == "7":
        mostrar_reporte_ventas(ventas)

    elif opcion == "8":
        guardar_datos(ARCHIVO_PRODUCTOS, productos)
        guardar_datos(ARCHIVO_VENTAS, ventas)
        print("Cambios guardados correctamente")

    elif opcion == "9":
        guardar_datos(ARCHIVO_PRODUCTOS, productos)
        guardar_datos(ARCHIVO_VENTAS, ventas)
        print("Cambios guardados correctamente")
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
from persistencia import guardar_datos, cargar_datos
from cliente_servicio import (
    registrar_cliente,
    mostrar_clientes,
    buscar_cliente_menu,
    actualizar_telefono,
    actualizar_correo,
    eliminar_cliente
)
from reportes import mostrar_reporte_general


ARCHIVO_CLIENTES = "clientes_modulo_1.json"


print("=== Gestor de clientes - Cierre Módulo 1 ===")


def mostrar_menu():
    print()
    print("1. Registrar cliente")
    print("2. Mostrar clientes")
    print("3. Buscar cliente")
    print("4. Actualizar teléfono")
    print("5. Actualizar correo")
    print("6. Eliminar cliente")
    print("7. Reporte general")
    print("8. Guardar cambios")
    print("9. Salir")


clientes = cargar_datos(ARCHIVO_CLIENTES)


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_cliente(clientes)

    elif opcion == "2":
        mostrar_clientes(clientes)

    elif opcion == "3":
        buscar_cliente_menu(clientes)

    elif opcion == "4":
        actualizar_telefono(clientes)

    elif opcion == "5":
        actualizar_correo(clientes)

    elif opcion == "6":
        eliminar_cliente(clientes)

    elif opcion == "7":
        mostrar_reporte_general(clientes)

    elif opcion == "8":
        guardar_datos(ARCHIVO_CLIENTES, clientes)
        print("Cambios guardados correctamente")

    elif opcion == "9":
        guardar_datos(ARCHIVO_CLIENTES, clientes)
        print("Cambios guardados correctamente")
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
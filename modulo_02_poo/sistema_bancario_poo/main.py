from cuenta_bancaria import CuentaBancaria
from cuenta_servicio import (
    registrar_cuenta,
    mostrar_cuentas,
    buscar_cuenta_menu,
    depositar_menu,
    retirar_menu,
    dar_de_baja_cuenta
)
from reportes import mostrar_reporte_general
from persistencia import guardar_cuentas, cargar_cuentas


ARCHIVO_CUENTAS = "cuentas_bancarias.json"


print("=== Sistema bancario POO final ===")


def mostrar_menu():
    print()
    print("1. Registrar cuenta")
    print("2. Mostrar cuentas")
    print("3. Buscar cuenta")
    print("4. Depositar")
    print("5. Retirar")
    print("6. Dar de baja cuenta")
    print("7. Reporte general")
    print("8. Guardar cambios")
    print("9. Salir")


cuentas = cargar_cuentas(ARCHIVO_CUENTAS)

if len(cuentas) == 0:
    cuentas = [
        CuentaBancaria("001", "Andrés Reveles", 1000.0),
        CuentaBancaria("002", "Juan Pérez", 2500.0),
        CuentaBancaria("003", "María López", 500.0)
    ]


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_cuenta(cuentas)

    elif opcion == "2":
        mostrar_cuentas(cuentas)

    elif opcion == "3":
        buscar_cuenta_menu(cuentas)

    elif opcion == "4":
        depositar_menu(cuentas)

    elif opcion == "5":
        retirar_menu(cuentas)

    elif opcion == "6":
        dar_de_baja_cuenta(cuentas)

    elif opcion == "7":
        mostrar_reporte_general(cuentas)

    elif opcion == "8":
        guardar_cuentas(ARCHIVO_CUENTAS, cuentas)
        print("Cambios guardados correctamente")

    elif opcion == "9":
        guardar_cuentas(ARCHIVO_CUENTAS, cuentas)
        print("Cambios guardados correctamente")
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
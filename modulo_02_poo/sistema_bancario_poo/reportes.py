def calcular_saldo_total(cuentas):
    """
    Calcula el saldo total de todas las cuentas.
    """
    return sum(cuenta.saldo for cuenta in cuentas)


def contar_cuentas_activas(cuentas):
    """
    Cuenta cuántas cuentas están activas.
    """
    return sum(1 for cuenta in cuentas if cuenta.activa)


def contar_cuentas_inactivas(cuentas):
    """
    Cuenta cuántas cuentas están inactivas.
    """
    return sum(1 for cuenta in cuentas if not cuenta.activa)


def obtener_cuenta_mayor_saldo(cuentas):
    """
    Retorna la cuenta con mayor saldo.
    """
    if len(cuentas) == 0:
        return None

    return max(cuentas, key=lambda cuenta: cuenta.saldo)


def mostrar_reporte_general(cuentas):
    """
    Muestra un reporte general del sistema bancario.
    """
    if len(cuentas) == 0:
        print("No hay cuentas registradas")
        return

    saldo_total = calcular_saldo_total(cuentas)
    cuentas_activas = contar_cuentas_activas(cuentas)
    cuentas_inactivas = contar_cuentas_inactivas(cuentas)
    cuenta_mayor_saldo = obtener_cuenta_mayor_saldo(cuentas)

    print("=== Reporte general del sistema bancario ===")
    print(f"Total de cuentas: {len(cuentas)}")
    print(f"Cuentas activas: {cuentas_activas}")
    print(f"Cuentas inactivas: {cuentas_inactivas}")
    print(f"Saldo total del sistema: ${saldo_total}")

    print()
    print("Cuenta con mayor saldo:")

    if cuenta_mayor_saldo is not None:
        cuenta_mayor_saldo.mostrar_resumen()
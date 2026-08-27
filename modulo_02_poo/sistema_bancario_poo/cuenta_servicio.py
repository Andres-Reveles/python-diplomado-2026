from cuenta_bancaria import CuentaBancaria
from entradas import pedir_texto_no_vacio, pedir_decimal_positivo, confirmar_accion


def buscar_cuenta(cuentas, numero_cuenta):
    """
    Busca una cuenta por número.
    Retorna la cuenta si existe o None si no existe.
    """
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta

    return None


def numero_cuenta_disponible(cuentas, numero_cuenta):
    """
    Valida si un número de cuenta está disponible.
    """
    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    return cuenta is None


def registrar_cuenta(cuentas):
    """
    Registra una cuenta bancaria nueva.
    """
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    if not numero_cuenta_disponible(cuentas, numero_cuenta):
        print("Error: ya existe una cuenta con ese número")
        return

    titular = pedir_texto_no_vacio("Titular: ")
    saldo = pedir_decimal_positivo("Saldo inicial: ")

    cuenta = CuentaBancaria(numero_cuenta, titular, saldo)

    cuentas.append(cuenta)

    print("Cuenta registrada correctamente")


def mostrar_cuentas(cuentas):
    """
    Muestra todas las cuentas registradas.
    """
    if len(cuentas) == 0:
        print("No hay cuentas registradas")
        return

    print("=== Cuentas registradas ===")

    for cuenta in cuentas:
        cuenta.mostrar_resumen()


def buscar_cuenta_menu(cuentas):
    """
    Busca una cuenta desde el menú.
    """
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta a buscar: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    print("Cuenta encontrada:")
    cuenta.mostrar_informacion()


def depositar_menu(cuentas):
    """
    Deposita dinero en una cuenta.
    """
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    cantidad = pedir_decimal_positivo("Cantidad a depositar: ")

    cuenta.depositar(cantidad)


def retirar_menu(cuentas):
    """
    Retira dinero de una cuenta.
    """
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    cantidad = pedir_decimal_positivo("Cantidad a retirar: ")

    cuenta.retirar(cantidad)


def dar_de_baja_cuenta(cuentas):
    """
    Da de baja lógica a una cuenta.
    """
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta a dar de baja: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    print("Cuenta encontrada:")
    cuenta.mostrar_informacion()

    confirmar = confirmar_accion("¿Seguro que deseas dar de baja esta cuenta? S/N: ")

    if confirmar:
        cuenta.dar_de_baja()
    else:
        print("Operación cancelada")
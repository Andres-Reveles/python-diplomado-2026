print("=== Módulo 2 - POO en Python I ===")
print("=== Sistema bancario base ===")


class CuentaBancaria:

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def mostrar_informacion(self):
        print("=== Cuenta bancaria ===")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad a depositar debe ser mayor a cero")
            return

        self.saldo += cantidad
        print(f"Depósito realizado correctamente por ${cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad a retirar debe ser mayor a cero")
            return

        if cantidad > self.saldo:
            print("Error: saldo insuficiente")
            return

        self.saldo -= cantidad
        print(f"Retiro realizado correctamente por ${cantidad}")


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


def pedir_decimal_positivo(mensaje):
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


def buscar_cuenta(cuentas, numero_cuenta):
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta

    return None


def mostrar_cuentas(cuentas):
    if len(cuentas) == 0:
        print("No hay cuentas registradas")
        return

    print("=== Cuentas registradas ===")

    for cuenta in cuentas:
        cuenta.mostrar_informacion()
        print("--------------------")


def registrar_cuenta(cuentas):
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    cuenta_existente = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta_existente is not None:
        print("Error: ya existe una cuenta con ese número")
        return

    titular = pedir_texto_no_vacio("Titular: ")
    saldo_inicial = pedir_decimal_positivo("Saldo inicial: ")

    cuenta = CuentaBancaria(numero_cuenta, titular, saldo_inicial)

    cuentas.append(cuenta)

    print("Cuenta registrada correctamente")


def depositar_menu(cuentas):
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    cantidad = pedir_decimal_positivo("Cantidad a depositar: ")

    cuenta.depositar(cantidad)


def retirar_menu(cuentas):
    numero_cuenta = pedir_texto_no_vacio("Número de cuenta: ")

    cuenta = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta is None:
        print("Cuenta no encontrada")
        return

    cantidad = pedir_decimal_positivo("Cantidad a retirar: ")

    cuenta.retirar(cantidad)


def mostrar_menu():
    print()
    print("1. Registrar cuenta")
    print("2. Mostrar cuentas")
    print("3. Depositar")
    print("4. Retirar")
    print("5. Salir")


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
        depositar_menu(cuentas)

    elif opcion == "4":
        retirar_menu(cuentas)

    elif opcion == "5":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
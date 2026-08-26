print("=== Módulo 2 - POO en Python I ===")
print("=== Operaciones sobre objetos ===")


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


def buscar_cuenta(cuentas, numero_cuenta):
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta

    return None


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


cuentas = [
    CuentaBancaria("001", "Andrés Reveles", 1000.0),
    CuentaBancaria("002", "Juan Pérez", 2500.0),
    CuentaBancaria("003", "María López", 500.0)
]

numero = input("Ingresa el número de cuenta: ").strip()

cuenta_encontrada = buscar_cuenta(cuentas, numero)

if cuenta_encontrada is None:
    print("Cuenta no encontrada")
else:
    print("Cuenta encontrada:")
    cuenta_encontrada.mostrar_informacion()

    print()
    print("1. Depositar")
    print("2. Retirar")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        cantidad = pedir_decimal_positivo("Cantidad a depositar: ")
        cuenta_encontrada.depositar(cantidad)

    elif opcion == "2":
        cantidad = pedir_decimal_positivo("Cantidad a retirar: ")
        cuenta_encontrada.retirar(cantidad)

    else:
        print("Opción inválida")

    print()
    print("Estado final de la cuenta:")
    cuenta_encontrada.mostrar_informacion()
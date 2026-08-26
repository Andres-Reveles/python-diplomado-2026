print("=== Módulo 2 - POO en Python I ===")
print("=== Buscar objeto en lista ===")


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


cuentas = [
    CuentaBancaria("001", "Andrés Reveles", 1000.0),
    CuentaBancaria("002", "Juan Pérez", 2500.0),
    CuentaBancaria("003", "María López", 500.0)
]

numero = input("Ingresa el número de cuenta a buscar: ").strip()

cuenta_encontrada = buscar_cuenta(cuentas, numero)

if cuenta_encontrada is None:
    print("Cuenta no encontrada")
else:
    print("Cuenta encontrada:")
    cuenta_encontrada.mostrar_informacion()
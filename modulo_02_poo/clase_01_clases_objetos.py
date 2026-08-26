print("=== Módulo 2 - POO en Python I ===")
print("=== Clase 1 - Varios objetos ===")


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


cuenta_1 = CuentaBancaria("001", "Andrés Reveles", 1000.0)
cuenta_2 = CuentaBancaria("002", "Juan Pérez", 2500.0)
cuenta_3 = CuentaBancaria("003", "María López", 500.0)

cuenta_1.depositar(500)
cuenta_2.retirar(1000)
cuenta_3.retirar(800)

print()
cuenta_1.mostrar_informacion()

print()
cuenta_2.mostrar_informacion()

print()
cuenta_3.mostrar_informacion()
print("=== Módulo 2 - POO en Python I ===")
print("=== Corrección de errores comunes en POO ===")


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
            print("Error: la cantidad debe ser mayor a cero")
            return

        self.saldo += cantidad
        print(f"Depósito realizado por ${cantidad}")


cuenta = CuentaBancaria("001", "Andrés Reveles", 1000.0)

cuenta.mostrar_informacion()

print()
cuenta.depositar(500)

print()
cuenta.mostrar_informacion()
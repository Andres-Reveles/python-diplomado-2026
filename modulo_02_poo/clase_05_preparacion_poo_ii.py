print("=== Módulo 2 - POO en Python II ===")
print("=== Preparación: problema de atributos públicos ===")


class CuentaBancaria:

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.activa = True

    def mostrar_informacion(self):
        print("=== Cuenta bancaria ===")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")
        print(f"Activa: {self.activa}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        self.saldo += cantidad
        print(f"Depósito realizado por ${cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        if cantidad > self.saldo:
            print("Error: saldo insuficiente")
            return

        self.saldo -= cantidad
        print(f"Retiro realizado por ${cantidad}")


cuenta = CuentaBancaria("001", "Andrés Reveles", 1000.0)

cuenta.mostrar_informacion()

print()
print("Modificando saldo directamente desde fuera de la clase...")

cuenta.saldo = -5000

print()
cuenta.mostrar_informacion()
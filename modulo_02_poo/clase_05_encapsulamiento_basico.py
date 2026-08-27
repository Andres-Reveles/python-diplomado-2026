print("=== Módulo 2 - POO en Python II ===")
print("=== Encapsulamiento básico ===")


class CuentaBancaria:

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular

        if saldo < 0:
            print("Error: el saldo inicial no puede ser negativo")
            self._saldo = 0
        else:
            self._saldo = saldo

        self.activa = True

    def obtener_saldo(self):
        return self._saldo

    def mostrar_informacion(self):
        print("=== Cuenta bancaria ===")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self._saldo}")
        print(f"Activa: {self.activa}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        self._saldo += cantidad
        print(f"Depósito realizado por ${cantidad}")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        if cantidad > self._saldo:
            print("Error: saldo insuficiente")
            return

        self._saldo -= cantidad
        print(f"Retiro realizado por ${cantidad}")


cuenta = CuentaBancaria("001", "Andrés Reveles", 1000.0)

cuenta.mostrar_informacion()

print()
cuenta.depositar(500)

print()
cuenta.retirar(300)

print()
print(f"Saldo consultado con método: ${cuenta.obtener_saldo()}")

print()
cuenta.mostrar_informacion()
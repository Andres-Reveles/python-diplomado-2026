class CuentaBancaria:

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.activa = True

    def mostrar_informacion(self):
        estado = "Activa" if self.activa else "Inactiva"

        print("=== Cuenta bancaria ===")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: ${self.saldo}")
        print(f"Estado: {estado}")

    def mostrar_resumen(self):
        estado = "Activa" if self.activa else "Inactiva"
        print(f"{self.numero_cuenta} - {self.titular} - ${self.saldo} - {estado}")

    def depositar(self, cantidad):
        if not self.activa:
            print("Error: no se puede depositar a una cuenta inactiva")
            return

        if cantidad <= 0:
            print("Error: la cantidad a depositar debe ser mayor a cero")
            return

        self.saldo += cantidad
        print(f"Depósito realizado correctamente por ${cantidad}")

    def retirar(self, cantidad):
        if not self.activa:
            print("Error: no se puede retirar de una cuenta inactiva")
            return

        if cantidad <= 0:
            print("Error: la cantidad a retirar debe ser mayor a cero")
            return

        if cantidad > self.saldo:
            print("Error: saldo insuficiente")
            return

        self.saldo -= cantidad
        print(f"Retiro realizado correctamente por ${cantidad}")

    def dar_de_baja(self):
        if not self.activa:
            print("La cuenta ya está inactiva")
            return

        self.activa = False
        print("Cuenta dada de baja correctamente")
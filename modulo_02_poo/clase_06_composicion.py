print("=== Módulo 2 - POO en Python II ===")
print("=== Clase 6 - Composición entre objetos ===")


class Cliente:

    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.activo = True

    def mostrar_informacion(self):
        estado = "Activo" if self.activo else "Inactivo"

        print("=== Cliente ===")
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Estado: {estado}")

    def mostrar_resumen(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f"{self.id_cliente} - {self.nombre} - {self.correo} - {estado}")


class CuentaBancaria:

    def __init__(self, numero_cuenta, cliente, saldo):
        self.numero_cuenta = numero_cuenta
        self.cliente = cliente

        if saldo < 0:
            print("Error: el saldo inicial no puede ser negativo")
            self._saldo = 0
        else:
            self._saldo = saldo

        self.activa = True

    @property
    def saldo(self):
        return self._saldo

    def mostrar_informacion(self):
        estado = "Activa" if self.activa else "Inactiva"

        print("=== Cuenta bancaria ===")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.cliente.nombre}")
        print(f"Correo del titular: {self.cliente.correo}")
        print(f"Saldo: ${self.saldo}")
        print(f"Estado: {estado}")

    def depositar(self, cantidad):
        if not self.activa:
            print("Error: no se puede depositar a una cuenta inactiva")
            return

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        self._saldo += cantidad
        print(f"Depósito realizado por ${cantidad}")

    def retirar(self, cantidad):
        if not self.activa:
            print("Error: no se puede retirar de una cuenta inactiva")
            return

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return

        if cantidad > self._saldo:
            print("Error: saldo insuficiente")
            return

        self._saldo -= cantidad
        print(f"Retiro realizado por ${cantidad}")


cliente_1 = Cliente(1, "Andrés Reveles", "andres@email.com")

cuenta_1 = CuentaBancaria("001", cliente_1, 1000.0)

cliente_1.mostrar_informacion()

print()

cuenta_1.mostrar_informacion()

print()
cuenta_1.depositar(500)

print()
cuenta_1.retirar(300)

print()
cuenta_1.mostrar_informacion()
print("=== Módulo 2 - POO en Python II ===")
print("=== Lista de órdenes bancarias ===")


class Cliente:

    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.activo = True


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

    def depositar(self, cantidad):
        if not self.activa:
            return False

        if cantidad <= 0:
            return False

        self._saldo += cantidad
        return True

    def retirar(self, cantidad):
        if not self.activa:
            return False

        if cantidad <= 0:
            return False

        if cantidad > self._saldo:
            return False

        self._saldo -= cantidad
        return True

    def mostrar_resumen(self):
        estado = "Activa" if self.activa else "Inactiva"
        print(f"{self.numero_cuenta} - {self.cliente.nombre} - ${self.saldo} - {estado}")


class OrdenBancaria:

    def __init__(self, folio, cuenta_origen, cuenta_destino, monto, concepto):
        self.folio = folio
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino
        self.monto = monto
        self.concepto = concepto
        self.estado = "PENDIENTE"

    def ejecutar(self):
        if self.estado != "PENDIENTE":
            print(f"Orden {self.folio}: ya fue procesada")
            return

        if self.cuenta_origen.numero_cuenta == self.cuenta_destino.numero_cuenta:
            print(f"Orden {self.folio}: origen y destino no pueden ser iguales")
            self.estado = "RECHAZADA"
            return

        if self.monto <= 0:
            print(f"Orden {self.folio}: monto inválido")
            self.estado = "RECHAZADA"
            return

        retiro_exitoso = self.cuenta_origen.retirar(self.monto)

        if not retiro_exitoso:
            print(f"Orden {self.folio}: saldo insuficiente o cuenta origen inválida")
            self.estado = "RECHAZADA"
            return

        deposito_exitoso = self.cuenta_destino.depositar(self.monto)

        if not deposito_exitoso:
            print(f"Orden {self.folio}: no se pudo depositar en destino")
            self.estado = "RECHAZADA"
            return

        self.estado = "EJECUTADA"
        print(f"Orden {self.folio}: ejecutada correctamente")

    def mostrar_resumen(self):
        print(
            f"{self.folio} - "
            f"{self.cuenta_origen.numero_cuenta} → {self.cuenta_destino.numero_cuenta} - "
            f"${self.monto} - {self.estado}"
        )


cliente_1 = Cliente(1, "Andrés Reveles", "andres@email.com")
cliente_2 = Cliente(2, "Juan Pérez", "juan@email.com")
cliente_3 = Cliente(3, "María López", "maria@email.com")

cuenta_1 = CuentaBancaria("001", cliente_1, 1000.0)
cuenta_2 = CuentaBancaria("002", cliente_2, 500.0)
cuenta_3 = CuentaBancaria("003", cliente_3, 200.0)

cuentas = [cuenta_1, cuenta_2, cuenta_3]

ordenes = [
    OrdenBancaria("O001", cuenta_1, cuenta_2, 300.0, "Pago de servicio"),
    OrdenBancaria("O002", cuenta_2, cuenta_3, 100.0, "Pago pendiente"),
    OrdenBancaria("O003", cuenta_3, cuenta_1, 500.0, "Transferencia mayor al saldo")
]

print("=== Cuentas antes de ejecutar órdenes ===")

for cuenta in cuentas:
    cuenta.mostrar_resumen()

print()
print("=== Ejecutando órdenes ===")

for orden in ordenes:
    orden.ejecutar()

print()
print("=== Resumen de órdenes ===")

for orden in ordenes:
    orden.mostrar_resumen()

print()
print("=== Cuentas después de ejecutar órdenes ===")

for cuenta in cuentas:
    cuenta.mostrar_resumen()
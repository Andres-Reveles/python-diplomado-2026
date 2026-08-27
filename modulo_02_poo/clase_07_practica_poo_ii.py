print("=== Módulo 2 - POO en Python II ===")
print("=== Clase 7 - Práctica corta de composición ===")


class Cliente:

    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.activo = True

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

    def depositar(self, cantidad):
        if not self.activa:
            print("Error: no se puede depositar a una cuenta inactiva")
            return False

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return False

        self._saldo += cantidad
        return True

    def retirar(self, cantidad):
        if not self.activa:
            print("Error: no se puede retirar de una cuenta inactiva")
            return False

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a cero")
            return False

        if cantidad > self._saldo:
            print("Error: saldo insuficiente")
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
            print("Error: la orden ya fue procesada")
            return

        if self.cuenta_origen.numero_cuenta == self.cuenta_destino.numero_cuenta:
            print("Error: la cuenta origen y destino no pueden ser la misma")
            self.estado = "RECHAZADA"
            return

        if self.monto <= 0:
            print("Error: el monto debe ser mayor a cero")
            self.estado = "RECHAZADA"
            return

        retiro_exitoso = self.cuenta_origen.retirar(self.monto)

        if not retiro_exitoso:
            print("Error: no se pudo retirar de la cuenta origen")
            self.estado = "RECHAZADA"
            return

        deposito_exitoso = self.cuenta_destino.depositar(self.monto)

        if not deposito_exitoso:
            print("Error: no se pudo depositar en la cuenta destino")
            self.estado = "RECHAZADA"
            return

        self.estado = "EJECUTADA"
        print("Orden ejecutada correctamente")

    def mostrar_resumen(self):
        print(
            f"{self.folio} - "
            f"{self.cuenta_origen.numero_cuenta} → {self.cuenta_destino.numero_cuenta} - "
            f"${self.monto} - {self.estado}"
        )


cliente_1 = Cliente(1, "Andrés Reveles", "andres@email.com")
cliente_2 = Cliente(2, "Juan Pérez", "juan@email.com")

cuenta_1 = CuentaBancaria("001", cliente_1, 1000.0)
cuenta_2 = CuentaBancaria("002", cliente_2, 500.0)

print("=== Cuentas antes ===")
cuenta_1.mostrar_resumen()
cuenta_2.mostrar_resumen()

print()

orden = OrdenBancaria("O001", cuenta_1, cuenta_2, 300.0, "Pago de servicio")

orden.mostrar_resumen()

print()
orden.ejecutar()

print()
orden.mostrar_resumen()

print()
print("=== Cuentas después ===")
cuenta_1.mostrar_resumen()
cuenta_2.mostrar_resumen()
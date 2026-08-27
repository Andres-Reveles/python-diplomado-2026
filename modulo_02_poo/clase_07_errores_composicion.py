print("=== Módulo 2 - POO en Python II ===")
print("=== Errores comunes con composición ===")


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
            self._saldo = 0
        else:
            self._saldo = saldo

        self.activa = True

    @property
    def saldo(self):
        return self._saldo

    def mostrar_resumen(self):
        estado = "Activa" if self.activa else "Inactiva"
        print(f"{self.numero_cuenta} - {self.cliente.nombre} - ${self.saldo} - {estado}")


cliente_1 = Cliente(1, "Andrés Reveles", "andres@email.com")

cuenta_1 = CuentaBancaria("001", cliente_1, 1000.0)

cuenta_1.mostrar_resumen()

print()
print("Nombre del titular:")
print(cuenta_1.cliente.nombre)

print()
print("Correo del titular:")
print(cuenta_1.cliente.correo)
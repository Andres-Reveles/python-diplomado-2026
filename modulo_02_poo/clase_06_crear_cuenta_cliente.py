print("=== Módulo 2 - POO en Python II ===")
print("=== Crear cuenta para un cliente ===")


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

    def mostrar_resumen(self):
        estado = "Activa" if self.activa else "Inactiva"

        print(
            f"{self.numero_cuenta} - {self.cliente.nombre} - "
            f"{self.cliente.correo} - ${self.saldo} - {estado}"
        )


def pedir_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def pedir_decimal_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero <= 0:
                print("Error: el número debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


def buscar_cliente(clientes, id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente

    return None


def buscar_cuenta(cuentas, numero_cuenta):
    for cuenta in cuentas:
        if cuenta.numero_cuenta == numero_cuenta:
            return cuenta

    return None


clientes = [
    Cliente(1, "Andrés Reveles", "andres@email.com"),
    Cliente(2, "Juan Pérez", "juan@email.com"),
    Cliente(3, "María López", "maria@email.com")
]

cuentas = [
    CuentaBancaria("001", clientes[0], 1000.0),
    CuentaBancaria("002", clientes[1], 2500.0)
]

print("=== Clientes disponibles ===")

for cliente in clientes:
    cliente.mostrar_resumen()

print()
id_cliente = pedir_entero_positivo("Ingresa el ID del cliente para crear cuenta: ")

cliente_encontrado = buscar_cliente(clientes, id_cliente)

if cliente_encontrado is None:
    print("Cliente no encontrado")
else:
    print("Cliente encontrado:")
    cliente_encontrado.mostrar_resumen()

    numero_cuenta = pedir_texto_no_vacio("Número de cuenta nueva: ")

    cuenta_existente = buscar_cuenta(cuentas, numero_cuenta)

    if cuenta_existente is not None:
        print("Error: ya existe una cuenta con ese número")
    else:
        saldo_inicial = pedir_decimal_positivo("Saldo inicial: ")

        nueva_cuenta = CuentaBancaria(numero_cuenta, cliente_encontrado, saldo_inicial)

        cuentas.append(nueva_cuenta)

        print("Cuenta creada correctamente")

print()
print("=== Cuentas registradas ===")

for cuenta in cuentas:
    cuenta.mostrar_resumen()
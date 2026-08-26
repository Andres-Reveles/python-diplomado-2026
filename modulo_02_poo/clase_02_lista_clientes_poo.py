print("=== Módulo 2 - POO en Python I ===")
print("=== Lista de clientes con POO ===")


class Cliente:

    def __init__(self, id_cliente, nombre, telefono, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.activo = True

    def mostrar_informacion(self):
        estado = "Activo" if self.activo else "Inactivo"

        print("=== Cliente ===")
        print(f"ID: {self.id_cliente}")
        print(f"Nombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Estado: {estado}")

    def mostrar_resumen(self):
        estado = "Activo" if self.activo else "Inactivo"
        print(f"{self.id_cliente} - {self.nombre} - {self.telefono} - {self.correo} - {estado}")

    def actualizar_telefono(self, nuevo_telefono):
        if nuevo_telefono.strip() == "":
            print("Error: el teléfono no puede estar vacío")
            return

        self.telefono = nuevo_telefono
        print("Teléfono actualizado correctamente")

    def actualizar_correo(self, nuevo_correo):
        if nuevo_correo.strip() == "":
            print("Error: el correo no puede estar vacío")
            return

        self.correo = nuevo_correo
        print("Correo actualizado correctamente")

    def dar_de_baja(self):
        if not self.activo:
            print("El cliente ya está inactivo")
            return

        self.activo = False
        print("Cliente dado de baja correctamente")


def buscar_cliente(clientes, id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            return cliente

    return None


clientes = [
    Cliente(1, "Andrés Reveles", "5512345678", "andres@email.com"),
    Cliente(2, "Juan Pérez", "5598765432", "juan@email.com"),
    Cliente(3, "María López", "5544455566", "maria@email.com")
]

print("=== Clientes registrados ===")

for cliente in clientes:
    cliente.mostrar_resumen()

print()

try:
    id_buscado = int(input("Ingresa el ID del cliente a buscar: "))

    cliente_encontrado = buscar_cliente(clientes, id_buscado)

    if cliente_encontrado is None:
        print("Cliente no encontrado")
    else:
        print("Cliente encontrado:")
        cliente_encontrado.mostrar_informacion()

except ValueError:
    print("Error: debes ingresar un número entero válido")
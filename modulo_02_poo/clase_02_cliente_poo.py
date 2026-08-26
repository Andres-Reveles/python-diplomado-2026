print("=== Módulo 2 - POO en Python I ===")
print("=== Clase Cliente con POO ===")


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


cliente_1 = Cliente(1, "Andrés Reveles", "5512345678", "andres@email.com")

cliente_1.mostrar_informacion()

print()
cliente_1.actualizar_telefono("5599999999")

print()
cliente_1.actualizar_correo("andresnuevo@email.com")

print()
cliente_1.dar_de_baja()

print()
cliente_1.mostrar_informacion()
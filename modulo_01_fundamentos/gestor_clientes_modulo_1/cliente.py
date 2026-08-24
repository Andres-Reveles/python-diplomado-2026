def crear_cliente(id_cliente, nombre, telefono, correo):
    """
    Crea y retorna un diccionario que representa un cliente.
    """
    return {
        "id": id_cliente,
        "nombre": nombre,
        "telefono": telefono,
        "correo": correo,
        "activo": True
    }


def mostrar_cliente(cliente):
    """
    Muestra la información completa de un cliente.
    """
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Teléfono: {cliente['telefono']}")
    print(f"Correo: {cliente['correo']}")
    print(f"Activo: {cliente['activo']}")


def mostrar_cliente_resumen(cliente):
    """
    Muestra la información resumida de un cliente.
    """
    estado = "Activo" if cliente["activo"] else "Inactivo"

    print(
        f"{cliente['id']} - {cliente['nombre']} - "
        f"{cliente['telefono']} - {cliente['correo']} - {estado}"
    )
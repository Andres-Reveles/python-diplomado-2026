from cliente import crear_cliente, mostrar_cliente, mostrar_cliente_resumen
from entradas import pedir_entero_positivo, pedir_texto_no_vacio, confirmar_accion


def buscar_cliente(clientes, id_cliente):
    """
    Busca un cliente por ID.
    Retorna el cliente si existe o None si no existe.
    """
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return cliente

    return None


def id_disponible(clientes, id_cliente):
    """
    Valida si un ID de cliente está disponible.
    """
    cliente = buscar_cliente(clientes, id_cliente)

    return cliente is None


def registrar_cliente(clientes):
    """
    Registra un cliente nuevo.
    """
    id_cliente = pedir_entero_positivo("Ingresa el ID del cliente: ")

    if not id_disponible(clientes, id_cliente):
        print("Error: ya existe un cliente con ese ID")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre del cliente: ")
    telefono = pedir_texto_no_vacio("Ingresa el teléfono del cliente: ")
    correo = pedir_texto_no_vacio("Ingresa el correo del cliente: ")

    cliente = crear_cliente(id_cliente, nombre, telefono, correo)

    clientes.append(cliente)

    print("Cliente registrado correctamente")


def mostrar_clientes(clientes):
    """
    Muestra todos los clientes registrados.
    """
    if len(clientes) == 0:
        print("No hay clientes registrados")
        return

    print("=== Clientes registrados ===")

    for cliente in clientes:
        mostrar_cliente_resumen(cliente)


def buscar_cliente_menu(clientes):
    """
    Busca un cliente por ID desde el menú.
    """
    id_cliente = pedir_entero_positivo("Ingresa el ID del cliente a buscar: ")

    cliente = buscar_cliente(clientes, id_cliente)

    if cliente is None:
        print("Cliente no encontrado")
        return

    print("Cliente encontrado:")
    mostrar_cliente(cliente)


def actualizar_telefono(clientes):
    """
    Actualiza el teléfono de un cliente.
    """
    id_cliente = pedir_entero_positivo("Ingresa el ID del cliente: ")

    cliente = buscar_cliente(clientes, id_cliente)

    if cliente is None:
        print("Cliente no encontrado")
        return

    print("Cliente encontrado:")
    mostrar_cliente(cliente)

    nuevo_telefono = pedir_texto_no_vacio("Ingresa el nuevo teléfono: ")

    cliente["telefono"] = nuevo_telefono

    print("Teléfono actualizado correctamente")


def actualizar_correo(clientes):
    """
    Actualiza el correo de un cliente.
    """
    id_cliente = pedir_entero_positivo("Ingresa el ID del cliente: ")

    cliente = buscar_cliente(clientes, id_cliente)

    if cliente is None:
        print("Cliente no encontrado")
        return

    print("Cliente encontrado:")
    mostrar_cliente(cliente)

    nuevo_correo = pedir_texto_no_vacio("Ingresa el nuevo correo: ")

    cliente["correo"] = nuevo_correo

    print("Correo actualizado correctamente")


def eliminar_cliente(clientes):
    """
    Da de baja lógica a un cliente.
    No lo elimina de la lista, solo lo marca como inactivo.
    """
    id_cliente = pedir_entero_positivo("Ingresa el ID del cliente a eliminar: ")

    cliente = buscar_cliente(clientes, id_cliente)

    if cliente is None:
        print("Cliente no encontrado")
        return

    if not cliente["activo"]:
        print("El cliente ya está inactivo")
        return

    print("Cliente encontrado:")
    mostrar_cliente(cliente)

    confirmar = confirmar_accion("¿Seguro que deseas dar de baja este cliente? S/N: ")

    if confirmar:
        cliente["activo"] = False
        print("Cliente dado de baja correctamente")
    else:
        print("Operación cancelada")
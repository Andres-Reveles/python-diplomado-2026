from cliente import mostrar_cliente_resumen


def contar_clientes(clientes):
    """
    Cuenta el total de clientes registrados.
    """
    return len(clientes)


def contar_clientes_activos(clientes):
    """
    Cuenta los clientes activos.
    """
    return sum(1 for cliente in clientes if cliente["activo"])


def contar_clientes_inactivos(clientes):
    """
    Cuenta los clientes inactivos.
    """
    return sum(1 for cliente in clientes if not cliente["activo"])


def obtener_clientes_activos(clientes):
    """
    Retorna una lista con los clientes activos.
    """
    return [cliente for cliente in clientes if cliente["activo"]]


def mostrar_reporte_general(clientes):
    """
    Muestra un reporte general de clientes.
    """
    if len(clientes) == 0:
        print("No hay clientes registrados")
        return

    total_clientes = contar_clientes(clientes)
    clientes_activos = contar_clientes_activos(clientes)
    clientes_inactivos = contar_clientes_inactivos(clientes)

    print("=== Reporte general de clientes ===")
    print(f"Total de clientes: {total_clientes}")
    print(f"Clientes activos: {clientes_activos}")
    print(f"Clientes inactivos: {clientes_inactivos}")

    print()
    print("=== Clientes activos ===")

    activos = obtener_clientes_activos(clientes)

    if len(activos) == 0:
        print("No hay clientes activos")
        return

    for cliente in activos:
        mostrar_cliente_resumen(cliente)
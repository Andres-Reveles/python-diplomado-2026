print("=== Uso básico de **kwargs ===")


def mostrar_datos(**datos):
    print(datos)

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


mostrar_datos(nombre="Angel", edad=23, carrera="ISC")
print("=== Venta segura con excepciones ===")


def pedir_entero_positivo(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)

            if numero <= 0:
                print("Error: la cantidad debe ser mayor a cero")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def registrar_venta(nombre_producto, precio, stock):
    print(f"Producto: {nombre_producto}")
    print(f"Precio: ${precio}")
    print(f"Stock disponible: {stock}")

    cantidad = pedir_entero_positivo("Ingresa la cantidad a vender: ")

    if cantidad > stock:
        print("Error: no hay stock suficiente")
        return stock

    total = cantidad * precio
    stock -= cantidad

    print()
    print("Venta registrada correctamente")
    print(f"Cantidad vendida: {cantidad}")
    print(f"Total: ${total}")
    print(f"Stock restante: {stock}")

    return stock


producto = "Mouse"
precio = 250.0
stock = 10

stock = registrar_venta(producto, precio, stock)
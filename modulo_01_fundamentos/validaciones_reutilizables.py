print("=== Validaciones reutilizables ===")


def texto_no_vacio(texto):
    return texto.strip() != ""


def precio_valido(precio):
    return precio > 0


def stock_valido(stock):
    return stock >= 0


nombre = input("Ingresa el nombre del producto: ").strip()
precio = float(input("Ingresa el precio del producto: "))
stock = int(input("Ingresa el stock del producto: "))

if not texto_no_vacio(nombre):
    print("El nombre no puede estar vacío")

elif not precio_valido(precio):
    print("El precio debe ser mayor a cero")

elif not stock_valido(stock):
    print("El stock no puede ser negativo")

else:
    print("Producto válido")
    print(f"Nombre: {nombre}")
    print(f"Precio: ${precio}")
    print(f"Stock: {stock}")
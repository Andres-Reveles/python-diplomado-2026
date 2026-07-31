print("=== Cargar productos desde archivo TXT ===")

productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()

        datos = linea.split("|")

        codigo = datos[0]
        nombre = datos[1]
        precio = float(datos[2])
        stock = int(datos[3])

        producto = {
            "Codigo": codigo,
            "Nombre": nombre,
            "Precio": precio,
            "stock": stock
        }
        productos.append(producto)

print("Lista de productos cargada desde 'productos.txt' correctamente.")
print(productos)

print()
print("=== Productos registrados ===")
for producto in productos:
    print(f"Código: {producto['Codigo']}")
    print(f"Nombre: {producto['Nombre']}")
    print(f"Precio: {producto['Precio']}")
    print(f"Stock: {producto['stock']}")
    print("-----------------------------")
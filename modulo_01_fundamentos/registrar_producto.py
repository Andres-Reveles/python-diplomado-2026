print("--- Registrar Producto ---")

productos = [
    {
        "codigo": "P001",
        "nombre": "Laptop",
        "precio": 1200.00,
        "cantidad": 10
    },
    {
        "codigo": "P002",
        "nombre": "Mouse",
        "precio": 25.00,
        "cantidad": 100
    },
    {
        "codigo": "P003",
        "nombre": "Teclado",
        "precio": 45.00,
        "cantidad": 50
    }

]

codigo = input("Ingrese el código del producto: ")

existe = False

for producto in productos:
    if producto["codigo"] == codigo:
        existe = True
        break
if existe:
    print("El producto ya existe.")
else:
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    if nombre == "" or precio <= 0 or cantidad < 0:
        print("Error: Datos inválidos. El nombre no puede estar vacío, el precio debe ser mayor a cero y la cantidad no puede ser negativa.")
    else:
        nuevo_producto = {
            "codigo": codigo,
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        productos.append(nuevo_producto)
        print("Producto registrado exitosamente.")

print()
print("--- Inventario de Productos ---")

for producto in productos:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    
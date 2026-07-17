print("--- Eliminar Producto ---")

productos = [
    {
        "codigo": "P001",
        "nombre": "Mouse",
        "precio": 150.00,
        "stock": 50
    },
    {
        "codigo": "P002",
        "nombre": "Teclado",
        "precio": 300.00,
        "stock": 30
    },
    {
        "codigo": "P003",
        "nombre": "Monitor",
        "precio": 3200.00,
        "stock": 20
    }
]

codigo_buscar = input("Ingrese el código del producto a eliminar: ")
producto_encontrado = False

for producto in productos:
    if producto["codigo"] == codigo_buscar:
        print("Producto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Stock: {producto['stock']}")

        confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").strip().upper()
        if confirmacion == "S":
            productos.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
        producto_encontrado = True
        break

if not producto_encontrado:
    print("Producto no encontrado.")

print()
print("Inventario actualizado:")
for producto in productos:
    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
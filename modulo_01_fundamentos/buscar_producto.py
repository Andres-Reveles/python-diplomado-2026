print("--- Buscar Producto ---")

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

codigo_buscar = input("Ingrese el código del producto a buscar: ")

encontrado = False

for producto in productos:
    if producto["codigo"] == codigo_buscar:
        print(f"Producto encontrado: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Stock: {producto['stock']} unidades")
        encontrado = True
        break

if not encontrado:
    print("Producto no encontrado.")
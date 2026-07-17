print("--- Productos Básicos ---")

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
        "precio": 1200.00,
        "stock": 20
    }
]

print("--- Inventario de Productos ---")

for producto in productos:
    print(f"Código: {producto['codigo']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print(f"Stock: {producto['stock']} unidades")
    print("-----------------------------")
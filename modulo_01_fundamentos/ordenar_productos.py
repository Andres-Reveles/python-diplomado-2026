print("--- Ordenar Productos ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 340.67, "Stock": 50},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 150.75, "Stock": 30},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1200.00, "Stock": 20},
    {"Codigo": "P004", "Nombre": "Laptop", "Precio": 2500.50, "Stock": 10},
    {"Codigo": "P005", "Nombre": "Smartphone", "Precio": 800.99, "Stock": 15}
]

productos_ordenados_por_precio = sorted(productos, key=lambda producto: producto["Precio"])

productos_por_stock_descendente = sorted(productos, key=lambda producto: producto["Stock"], reverse=True)

print()
print("Productos ordenados por precio (ascendente):")
for producto in productos_ordenados_por_precio:
    print(f"{producto['Nombre']} - Precio: {producto['Precio']}")

print()
print("Productos ordenados por stock (descendente):")
for producto in productos_por_stock_descendente:
    print(f"{producto['Nombre']} - Stock: {producto['Stock']}")
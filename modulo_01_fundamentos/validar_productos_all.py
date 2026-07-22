print("--- Validar Productos All ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 340.67, "Stock": 50},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 150.75, "Stock": 30},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1200.00, "Stock": 20},
    {"Codigo": "P004", "Nombre": "Laptop", "Precio": 2500.50, "Stock": 10},
    {"Codigo": "P005", "Nombre": "Smartphone", "Precio": 800.99, "Stock": 15}
]

todos_tienen_stock = all(producto["Stock"] > 0 for producto in productos)
todos_tienen_precio_positivo = all(producto["Precio"] > 0 for producto in productos)

print(f"Todos tienen stock: {todos_tienen_stock}")
print(f"Todos tienen precio positivo: {todos_tienen_precio_positivo}")
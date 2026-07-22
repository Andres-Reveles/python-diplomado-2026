print("--- Sumar Diccionarios ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 340.67, "Stock": 50},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 150.75, "Stock": 30},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1200.00, "Stock": 20},
    {"Codigo": "P004", "Nombre": "Laptop", "Precio": 2500.50, "Stock": 10},
    {"Codigo": "P005", "Nombre": "Smartphone", "Precio": 800.99, "Stock": 15}
]

valor_total = sum(producto["Precio"] * producto["Stock"] for producto in productos)
stock_total = sum(producto["Stock"] for producto in productos)

print(f"Valor total de inventario: {valor_total}")
print(f"Stock total de productos: {stock_total}")
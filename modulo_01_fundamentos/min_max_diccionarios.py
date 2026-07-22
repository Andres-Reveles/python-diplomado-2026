print("--- Min y Max Diccionarios ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 340.67, "Stock": 50},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 150.75, "Stock": 30},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1200.00, "Stock": 20},
    {"Codigo": "P004", "Nombre": "Laptop", "Precio": 2500.50, "Stock": 10},
    {"Codigo": "P005", "Nombre": "Smartphone", "Precio":    800.99, "Stock": 15}
]

producto_mas_caro = max(productos, key=lambda producto: producto["Precio"])
producto_mas_barato = min(productos, key=lambda producto: producto["Precio"])
producto_mas_stock = max(productos, key=lambda producto: producto["Stock"])
producto_menos_stock = min(productos, key=lambda producto: producto["Stock"])

print(f"Producto más caro: {producto_mas_caro}")
print(f"Producto más barato: {producto_mas_barato}")
print(f"Producto con más stock: {producto_mas_stock}")
print(f"Producto con menos stock: {producto_menos_stock}")
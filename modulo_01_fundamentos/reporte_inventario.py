print("--- Reporte de Inventario ---")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 340.67, "Stock": 50},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 150.75, "Stock": 30},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1200.00, "Stock": 20},
    {"Codigo": "P004", "Nombre": "Laptop", "Precio": 2500.50, "Stock": 10},
    {"Codigo": "P005", "Nombre": "Smartphone", "Precio": 800.99, "Stock": 15}
]

productos_disponibles = [
    producto for producto in productos if producto["Stock"] > 0]

productos_sin_stock = [
    producto for producto in productos if producto["Stock"] == 0]

productos_caros = [
    producto for producto in productos if producto["Precio"] > 1000]

valor_total_inventario = sum(producto["Precio"] * producto["Stock"] for producto in productos)
stock_total = sum(producto["Stock"] for producto in productos)

producto_mas_caro = max(productos, key=lambda producto: producto["Precio"])
producto_mas_barato = min(productos, key=lambda producto: producto["Precio"])

productos_ordenados_por_precio = sorted(
    productos, key=lambda producto: producto["Precio"])

todos_tienen_precio_positivo = all(
    producto["Precio"] > 0 for producto in productos)

hay_productos_sin_stock = any(
    producto["Stock"] == 0 for producto in productos)

print()
print("--- Resumen general ---")
print(f"Cantidad de productos: {len(productos)}")
print(f"Stock total de productos: {stock_total}")
print(f"Valor total de inventario: {valor_total_inventario}")
print(f"Todos tienen precio valido?: {todos_tienen_precio_positivo}")
print(f"Hay productos sin stock?: {hay_productos_sin_stock}")

print()
print("--- Producto más caro ---")
print(f"{producto_mas_caro['Nombre']} - Precio: {producto_mas_caro['Precio']}")

print()
print("--- Producto más barato ---")
print(f"{producto_mas_barato['Nombre']} - Precio: {producto_mas_barato['Precio']}")

print()
print("--- Productos disponibles ---")
for producto in productos_disponibles:
    print(f"{producto['Nombre']} - Stock: {producto['Stock']}")

print()
print("--- Productos sin stock ---")
for producto in productos_sin_stock:
    print(f"{producto['Nombre']} - Stock: {producto['Stock']}")

print()
print("--- Productos caros (Precio > 1000) ---")
for producto in productos_caros:
    print(f"{producto['Nombre']} - Precio: {producto['Precio']}")

print()

print("--- Productos ordenados por precio (ascendente) ---")
for producto in productos_ordenados_por_precio:
    print(f"{producto['Nombre']} - Precio: {producto['Precio']}")
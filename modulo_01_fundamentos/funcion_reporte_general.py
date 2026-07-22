print("=== Función para reporte general ===")

productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250.0, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500.0, "stock": 5},
    {"codigo": "P003", "nombre": "Monitor", "precio": 3200.0, "stock": 2},
    {"codigo": "P004", "nombre": "Webcam", "precio": 850.0, "stock": 0},
    {"codigo": "P005", "nombre": "USB", "precio": 120.0, "stock": 20}
]


def mostrar_reporte_general(productos):
    if len(productos) == 0:
        print("No hay productos registrados")
        return

    cantidad_productos = len(productos)
    stock_total = sum(producto["stock"] for producto in productos)
    valor_total = sum(producto["precio"] * producto["stock"] for producto in productos)

    producto_mas_caro = max(productos, key=lambda producto: producto["precio"])
    producto_mas_barato = min(productos, key=lambda producto: producto["precio"])

    hay_productos_sin_stock = any(producto["stock"] == 0 for producto in productos)
    todos_tienen_precio_valido = all(producto["precio"] > 0 for producto in productos)

    print("=== Reporte general ===")
    print(f"Cantidad de productos: {cantidad_productos}")
    print(f"Stock total: {stock_total}")
    print(f"Valor total del inventario: ${valor_total}")

    print()
    print("Producto más caro:")
    print(f"{producto_mas_caro['codigo']} - {producto_mas_caro['nombre']} - ${producto_mas_caro['precio']}")

    print()
    print("Producto más barato:")
    print(f"{producto_mas_barato['codigo']} - {producto_mas_barato['nombre']} - ${producto_mas_barato['precio']}")

    print()
    print(f"¿Hay productos sin stock?: {hay_productos_sin_stock}")
    print(f"¿Todos tienen precio válido?: {todos_tienen_precio_valido}")


mostrar_reporte_general(productos)

print("--- Valor Inventario ---")

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

valor_total = 0
print("Productos en inventario:")
for producto in productos:
    valor_producto = producto["precio"] * producto["stock"]
    
    valor_total += valor_producto

    print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}, Valor Total: {valor_producto}")

print(f"Valor total del inventario: {valor_total}")

print("=== Parámetros por defecto aplicados a IVA ===")


def calcular_precio_con_iva(precio, iva=0.16):
    total = precio + (precio * iva)
    return total


precio_producto = float(input("Ingresa el precio del producto: "))

total_con_iva_mexico = calcular_precio_con_iva(precio_producto)
total_con_iva_especial = calcular_precio_con_iva(precio_producto, 0.08)

print(f"Precio base: ${precio_producto}")
print(f"Total con IVA 16%: ${total_con_iva_mexico}")
print(f"Total con IVA 8%: ${total_con_iva_especial}")
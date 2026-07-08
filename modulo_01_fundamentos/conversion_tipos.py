edad_texto = "24"
precio_texto = "199.99"

edad = int(edad_texto)
precio = float(precio_texto)

print("=== Conversión de tipos ===")
print(f"Edad como texto: {edad_texto}")
print(f"Edad convertida a entero: {edad}")

print(f"Precio como texto: {precio_texto}")
print(f"Precio convertido a decimal: {precio}")

print(type(edad_texto))
print(type(edad))
print(type(precio_texto))
print(type(precio))

numero_1 = "10"
numero_2 = "5"

print(numero_1 + numero_2)
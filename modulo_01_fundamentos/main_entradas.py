from entradas import pedir_texto_no_vacio, pedir_float_positivo, pedir_int_no_negativo, pedir_float_rango

print("=== Uso del módulo entradas ===")

nombre = pedir_texto_no_vacio("Ingresa tu nombre: ")
precio = pedir_float_positivo("Ingresa un precio: ")
stock = pedir_int_no_negativo("Ingresa el stock: ")
calificacion = pedir_float_rango("Ingresa una calificación: ", 0, 10)

print()
print("Datos capturados correctamente")
print(f"Nombre: {nombre}")
print(f"Precio: ${precio}")
print(f"Stock: {stock}")
print(f"Calificación: {calificacion}")
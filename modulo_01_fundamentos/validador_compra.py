print("=== Validador de compra ===")

edad = int(input("Ingresa tu edad: "))
saldo = float(input("Ingresa tu saldo disponible: "))
total_compra = float(input("Ingresa el total de la compra: "))
respuesta_ine = input("¿Tienes INE? Escribe si o no: ").strip().lower()

tiene_ine = respuesta_ine == "si" or respuesta_ine == "sí"

es_mayor_de_edad = edad >= 18
saldo_suficiente = saldo >= total_compra

puede_comprar = es_mayor_de_edad and tiene_ine and saldo_suficiente

print()
print("=== Resultado de validación ===")
print(f"Edad: {edad}")
print(f"Saldo disponible: {saldo}")
print(f"Total de compra: {total_compra}")
print(f"Tiene INE: {tiene_ine}")
print(f"Es mayor de edad: {es_mayor_de_edad}")
print(f"Saldo suficiente: {saldo_suficiente}")
print(f"Puede comprar: {puede_comprar}")
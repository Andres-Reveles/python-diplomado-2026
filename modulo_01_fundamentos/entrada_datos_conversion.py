print("=== Registro básico con conversión ===")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

edad_proximo_anio = edad + 1

print(f"Nombre registrado: {nombre}")
print(f"Edad actual: {edad}")
print(f"Edad el próximo año: {edad_proximo_anio}")

print(type(nombre))
print(type(edad))
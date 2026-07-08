print("=== Ficha personal ===")

nombre = input("Nombre: ")
edad = int(input("Edad: "))
carrera = input("Carrera: ")
trabaja = input("¿Actualmente trabajas? ")

edad_en_5_anios = edad + 5

print()
print("=== Resultado ===")
print(f"Nombre: {nombre}")
print(f"Edad actual: {edad}")
print(f"Edad en 5 años: {edad_en_5_anios}")
print(f"Carrera: {carrera}")
print(f"Trabaja actualmente: {trabaja}")
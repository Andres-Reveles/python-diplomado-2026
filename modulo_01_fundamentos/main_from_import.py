from operaciones import sumar, restar, multiplicar, dividir

print("=== From import ===")

resultado_suma = sumar(20, 10)
resultado_resta = restar(20, 10)
resultado_multiplicacion = multiplicar(20, 10)
resultado_division = dividir(20, 10)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
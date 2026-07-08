print("=== Calculadora básica validada ===")

numero_1 = float(input("Ingresa el primer número: "))
numero_2 = float(input("Ingresa el segundo número: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2

print()
print("=== Resultados ===")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")

if numero_2 != 0:
    division = numero_1 / numero_2
    print(f"División: {division}")
else:
    print("División: no se puede dividir entre cero")
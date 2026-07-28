import operaciones

print("=== Import básico ===")

resultado_suma = operaciones.sumar(10, 5)
resultado_resta = operaciones.restar(10, 5)
resultado_multiplicacion = operaciones.multiplicar(10, 5)
resultado_division = operaciones.dividir(10, 5)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
import operaciones as op

print("=== Import con alias ===")

resultado_suma = op.sumar(50, 25)
resultado_resta = op.restar(50, 25)
resultado_multiplicacion = op.multiplicar(50, 25)
resultado_division = op.dividir(50, 25)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
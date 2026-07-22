print("=== Uso básico de *args ===")


def sumar_numeros(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total


resultado_1 = sumar_numeros(10, 20)
resultado_2 = sumar_numeros(10, 20, 30)
resultado_3 = sumar_numeros(5, 8, 9, 10, 20)

print(f"Resultado 1: {resultado_1}")
print(f"Resultado 2: {resultado_2}")
print(f"Resultado 3: {resultado_3}")
print("=== División segura ===")

try:
    numero_1 = float(input("Ingresa el primer número: "))
    numero_2 = float(input("Ingresa el segundo número: "))

    resultado = numero_1 / numero_2

    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes ingresar números válidos")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
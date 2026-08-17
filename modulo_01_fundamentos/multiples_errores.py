print("=== Múltiples errores ===")

numeros = [10, 20, 30]

try:
    indice = int(input("Ingresa la posición que quieres consultar: "))

    numero = numeros[indice]

    divisor = int(input("Ingresa el divisor: "))

    resultado = numero / divisor

    print(f"Número elegido: {numero}")
    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes ingresar números enteros válidos")

except IndexError:
    print("Error: esa posición no existe en la lista")

except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")

finally:
    print("Fin del programa")
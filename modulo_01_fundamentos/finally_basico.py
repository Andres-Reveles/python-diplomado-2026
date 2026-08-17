print("=== Ejemplo básico de finally ===")

try:
    numero = int(input("Ingresa un número entero: "))

    print(f"Número ingresado: {numero}")

except ValueError:
    print("Error: debes ingresar un número entero válido")

finally:
    print("Fin del intento de captura")
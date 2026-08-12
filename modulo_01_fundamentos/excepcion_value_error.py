print("=== Ejemplo de ValueError ===")

try:
    edad = int(input("Ingresa tu edad: "))

    print(f"Tu edad es: {edad}")

except ValueError:
    print("Error: debes ingresar un número entero")
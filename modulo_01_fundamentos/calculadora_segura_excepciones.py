print("=== Calculadora segura con excepciones ===")


def pedir_decimal(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero")
        return None


def mostrar_menu():
    print()
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        numero_1 = pedir_decimal("Ingresa el primer número: ")
        numero_2 = pedir_decimal("Ingresa el segundo número: ")

        resultado = sumar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "2":
        numero_1 = pedir_decimal("Ingresa el primer número: ")
        numero_2 = pedir_decimal("Ingresa el segundo número: ")

        resultado = restar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "3":
        numero_1 = pedir_decimal("Ingresa el primer número: ")
        numero_2 = pedir_decimal("Ingresa el segundo número: ")

        resultado = multiplicar(numero_1, numero_2)
        print(f"Resultado: {resultado}")

    elif opcion == "4":
        numero_1 = pedir_decimal("Ingresa el primer número: ")
        numero_2 = pedir_decimal("Ingresa el segundo número: ")

        resultado = dividir(numero_1, numero_2)

        if resultado is not None:
            print(f"Resultado: {resultado}")

    elif opcion == "5":
        print("Saliendo de la calculadora")
        break

    else:
        print("Opción inválida")
print("=== Calculadora repetitiva ===")

while True:
    print()
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "5":
        print("Saliendo de la calculadora")
        break

    elif opcion in ["1", "2", "3", "4"]:
        numero_1 = float(input("Ingresa el primer número: "))
        numero_2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = numero_1 + numero_2
            print(f"Resultado de la suma: {resultado}")

        elif opcion == "2":
            resultado = numero_1 - numero_2
            print(f"Resultado de la resta: {resultado}")

        elif opcion == "3":
            resultado = numero_1 * numero_2
            print(f"Resultado de la multiplicación: {resultado}")

        elif opcion == "4":
            if numero_2 != 0:
                resultado = numero_1 / numero_2
                print(f"Resultado de la división: {resultado}")
            else:
                print("Error: no se puede dividir entre cero")

    else:
        print("Opción inválida")
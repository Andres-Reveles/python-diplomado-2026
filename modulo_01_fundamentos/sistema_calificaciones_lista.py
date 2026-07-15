print("--- Sistema de calificaciones con lista ---")

calificaciones = []

while True:
    print()
    print("1. Registrar calificación")
    print("2. Mostrar calificaciones")
    print("3. Calcular promedio")
    print("4. Mostrar calificación mayor")
    print("5. Mostrar calificación menor")
    print("6. Eliminar calificación")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        calificacion = int(input("Ingrese la calificación (0-10): "))

        if calificacion < 0 or calificacion > 10:
            print("La calificación debe estar entre 0 y 10.") 
        else:
            calificaciones.append(calificacion)
            print(f"Calificación {calificacion} registrada.")
    elif opcion == "2":
        if len(calificaciones) == 0:
            print("No hay calificaciones registradas.")
        else:
            print("Lista de calificaciones:")
            for indice, calificacion in enumerate(calificaciones, start=1):
                print(f"{indice}. {calificacion}")
    elif opcion == "3":
        if len(calificaciones) == 0:
            print("No hay calificaciones registradas.")
        else:
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"El promedio de las calificaciones es: {promedio:.2f}")
    elif opcion == "4":
        if len(calificaciones) == 0:
            print("No hay calificaciones registradas.")
        else:
            mayor = max(calificaciones)
            print(f"La calificación mayor es: {mayor}")
    elif opcion == "5":
        if len(calificaciones) == 0:
            print("No hay calificaciones registradas.")
        else:
            menor = min(calificaciones)
            print(f"La calificación menor es: {menor}")
    elif opcion == "6":
        if len(calificaciones) == 0:
            print("No hay calificaciones para eliminar.")
        else:
            print("=== Calificaciones registradas ===")
            for indice, calificacion in enumerate(calificaciones, start=1):
                print(f"{indice}. {calificacion}")

            posicion = int(input("Ingrese el numero de la calificación a eliminar: "))

            if posicion < 1 or posicion > len(calificaciones):
                print("Posición inválida.")
            else:
                calificacion_eliminada = calificaciones.pop(posicion - 1)
                print(f"Calificación {calificacion_eliminada} eliminada.")
    elif opcion == "7":
        break
    else:
        print("Opción no válida.")
    
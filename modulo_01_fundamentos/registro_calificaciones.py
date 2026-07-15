print("=== Registro de calificaciones ===")
print("Escribe -1 para terminar")

suma_calificaciones = 0
cantidad_calificaciones = 0

while True:
    calificacion = float(input("Ingresa una calificación: "))

    if calificacion == -1:
        print("Terminando captura...")
        break

    if calificacion < 0 or calificacion > 10:
        print("Calificación inválida. Debe estar entre 0 y 10.")
        continue

    suma_calificaciones += calificacion
    cantidad_calificaciones += 1

    print("Calificación registrada correctamente")

print()
print("=== Resultado final ===")

if cantidad_calificaciones > 0:
    promedio = suma_calificaciones / cantidad_calificaciones
    print(f"Calificaciones válidas capturadas: {cantidad_calificaciones}")
    print(f"Promedio: {promedio}")
else:
    print("No se capturaron calificaciones válidas")
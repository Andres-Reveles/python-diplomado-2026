print("--- Captura de calificaciones en una lista ---")
print("Escribe -1 para terminar la captura de calificaciones.")

calificaciones = []

while True:
    calificacion = int(input("Ingrese una calificación (o -1 para terminar): "))
    
    if calificacion == -1:
        break
    
    if calificacion < 0 or calificacion > 10:
        print("Calificación inválida. Debe estar entre 0 y 10.")
        continue


    calificaciones.append(calificacion)
    print("Calificaciones capturadas:", calificaciones)

print()
print("--- Resultado final ---")
print("Calificaciones capturadas:", calificaciones)

if len(calificaciones) > 0:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Cantidad de calificaciones capturadas: {len(calificaciones)}")
    print(f"Promedio de calificaciones: {promedio:.2f}")
else:
    print("No se capturaron calificaciones.")    
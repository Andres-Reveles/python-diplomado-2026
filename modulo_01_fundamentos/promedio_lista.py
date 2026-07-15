print("--- Promedio de elementos de una lista ---")

calificaciones = [10, 9, 8, 7]

suma = 0
#for calificacion in calificaciones:
#    suma += calificacion
#promedio = suma / len(calificaciones)

promedio = sum(calificaciones) / len(calificaciones)

print(f"Calificaciones: {calificaciones}")
print(f"El promedio de las calificaciones es: {promedio}")
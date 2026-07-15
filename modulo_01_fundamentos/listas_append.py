print("--- Agregando elementos a una lista ---")

calificaciones = []
calificaciones.append(10)
calificaciones.append(9)
calificaciones.append(8)

print(calificaciones)

calificacion_nueva = float(input("Ingrese una nueva calificación: "))
calificaciones.append(calificacion_nueva)

print(f"Lista actualizada de calificaciones: {calificaciones}")
print(f"Cantidad de calificaciones: {len(calificaciones)}")

                           
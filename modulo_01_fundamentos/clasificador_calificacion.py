print("=== Clasificador de calificación ===")

calificacion = float(input("Ingresa la calificación: "))

if calificacion < 0 or calificacion > 10:
    print("Calificación inválida")
elif calificacion >= 9:
    print("Excelente")
elif calificacion >= 8:
    print("Muy bien")
elif calificacion >= 7:
    print("Bien")
elif calificacion >= 6:
    print("Aprobado")
else:
    print("Reprobado")

print("Fin del programa")
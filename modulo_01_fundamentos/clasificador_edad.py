print("=== Clasificador de edad ===")

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
elif edad <= 12:
    print("Clasificación: Niño")
elif edad <= 17:
    print("Clasificación: Adolescente")
elif edad <= 59:
    print("Clasificación: Adulto")
else:
    print("Clasificación: Adulto mayor")

print("Fin del programa")
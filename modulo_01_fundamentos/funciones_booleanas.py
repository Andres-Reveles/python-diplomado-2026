print("--- Funciones booleanas ---")

def es_mayyor_de_edad(edad):
    return edad >= 18

def calificacion_valida(calificacion):
    return 0 <= calificacion <= 10

edad = int(input("Ingrese su edad: "))

calificacion = float(input("Ingrese su calificación (0-10): "))

if es_mayyor_de_edad(edad):
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")

if calificacion_valida(calificacion):
    print("La calificación es válida.")
else:
    print("La calificación no es válida.")
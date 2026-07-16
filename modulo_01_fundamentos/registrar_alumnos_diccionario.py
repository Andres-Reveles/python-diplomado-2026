print("--- Registrar Alumnos ---")

alumnos = []

while True:
    nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    edad = int(input("Ingrese la edad del alumno: "))
    carrera = input("Ingrese la carrera del alumno: ")

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera
    }

    alumnos.append(alumno)
    print(f"Alumno {nombre} registrado exitosamente.\n")

print("\n--- Lista de Alumnos Registrados ---")
if len(alumnos) == 0:
    print("No hay alumnos registrados.")
else:
    for alumno in alumnos:
        print(f"Nombre: {alumno['nombre']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Carrera: {alumno['carrera']}")
        print("--------------------")
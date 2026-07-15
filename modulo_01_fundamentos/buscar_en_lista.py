print("--- Buscar en lista ---")

alumnos = ["Juan", "María", "Pedro", "Ana"]

nombre = input("Ingrese el nombre del alumno que desea buscar: ").strip()

if nombre in alumnos:
    print(f"{nombre} si está registrado.")
else:
    print(f"{nombre} no está registrado.")

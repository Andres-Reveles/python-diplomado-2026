print("--- Validar alumno no repetido ---")

alumnos = ["Juan", "María", "Pedro", "Ana"]
nombre = input("Ingrese el nombre del alumno que desea registrar: ").strip()

if nombre not in alumnos:
    alumnos.append(nombre)
    print("Alummno registrado exitosamente.")
else:
    print("El alumno ya está registrado.")

print(f"Lista de alumnos: {alumnos}")
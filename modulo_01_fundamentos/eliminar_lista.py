print("--- Eliminar elemento de una lista ---")

alumnos = ["Juan", "María", "Pedro", "Ana"]
print(f"Alumnos registrados: {alumnos}")

nombre = input("Ingrese el nombre del alumno que desea eliminar: ").strip()

if nombre in alumnos:
    alumnos.remove(nombre)
    print(f"{nombre} ha sido eliminado de la lista.")
else:
    print(f"{nombre} no se encuentra en la lista de alumnos.")
print(f"Lista de alumnos actualizada: {alumnos}")


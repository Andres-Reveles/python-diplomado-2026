print("--- Sistema de alumnos con lista ---")

alumnos = []

while True:
    print()
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")

        if nombre == "":
            print("El nombre del alumno no puede estar vacío.")
        elif nombre in alumnos:
            print("El alumno ya está registrado.")
        else:
            alumnos.append(nombre)
            print(f"Alumno {nombre} registrado.")


    elif opcion == "2":
        if len(alumnos) == 0:
            print("No hay alumnos registrados.")
        else:
            print("Lista de alumnos:")
            for indice, alumno in enumerate(alumnos, start=1):
                print(f"{indice}. {alumno}")
    
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno a buscar: ")
        if nombre in alumnos:
            print(f"Alumno {nombre} encontrado.")
        else:
            print(f"Alumno {nombre} no encontrado.")
    
    elif opcion == "4":
        
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        
        if nombre in alumnos:
            alumnos.remove(nombre)
            print(f"Alumno {nombre} eliminado.")
        else:
            print(f"Alumno {nombre} no encontrado.")
    
    elif opcion == "5":
        break
    
    else:
        print("Opción no válida.")
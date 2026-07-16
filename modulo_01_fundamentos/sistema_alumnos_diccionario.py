print("--- Sistema de Alumnos (Diccionario) ---")

alumnos = []

while True:
    print()
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Eliminar alumno")
    print("5. Mostrar promedios")
    print("6. Salir")

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ").strip()

        if nombre == "":
            print("El nombre no puede estar vacío")
            continue

        existe = False

        for alumno in alumnos:
            if alumno["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print("El alumno ya está registrado")
        else:
            edad = int(input("Ingresa la edad: "))
            promedio = float(input("Ingresa el promedio: "))

            if edad < 0:
                print("Edad inválida")
            elif promedio < 0 or promedio > 10:
                print("Promedio inválido")
            else:
                alumno = {
                    "nombre": nombre,
                    "edad": edad,
                    "promedio": promedio
                }

                alumnos.append(alumno)
                print("Alumno registrado correctamente")

    elif opcion == "2":
        if len(alumnos) == 0:
            print("No hay alumnos registrados")
        else:
            print("=== Lista de alumnos ===")

            for indice, alumno in enumerate(alumnos, start=1):
                print(f"{indice}. Nombre: {alumno['nombre']}")
                print(f"   Edad: {alumno['edad']}")
                print(f"   Promedio: {alumno['promedio']}")

    elif opcion == "3":
        nombre = input("Ingresa el nombre a buscar: ").strip()
        encontrado = False

        for alumno in alumnos:
            if alumno["nombre"].lower() == nombre.lower():
                print("Alumno encontrado")
                print(f"Nombre: {alumno['nombre']}")
                print(f"Edad: {alumno['edad']}")
                print(f"Promedio: {alumno['promedio']}")
                encontrado = True
                break

        if not encontrado:
            print("Alumno no encontrado")

    elif opcion == "4":
        nombre = input("Ingresa el nombre del alumno a eliminar: ").strip()
        eliminado = False

        for alumno in alumnos:
            if alumno["nombre"].lower() == nombre.lower():
                alumnos.remove(alumno)
                print("Alumno eliminado correctamente")
                eliminado = True
                break

        if not eliminado:
            print("Alumno no encontrado")

    elif opcion == "5":
        if len(alumnos) == 0:
            print("No hay alumnos registrados")
        else:
            suma = 0

            for alumno in alumnos:
                suma += alumno["promedio"]

            promedio_general = suma / len(alumnos)

            print(f"Promedio general del grupo: {promedio_general}")

    elif opcion == "6":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
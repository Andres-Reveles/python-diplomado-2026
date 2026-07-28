from alumnos import crear_alumno, mostrar_alumnos, buscar_alumno, mostrar_alumno_con_estado

print("=== Uso del módulo alumnos ===")

alumno_1 = crear_alumno("A001", "Angel", "ISC")
alumno_2 = crear_alumno("A002", "Luis", "Contaduría")
alumno_3 = crear_alumno("A003", "María", "Administración")

alumno_1["calificaciones"] = [9, 8, 10]
alumno_2["calificaciones"] = [5, 6, 5]

alumnos = [alumno_1, alumno_2, alumno_3]

mostrar_alumnos(alumnos)

print()
matricula = input("Ingresa una matrícula para buscar: ").strip().upper()

alumno_encontrado = buscar_alumno(alumnos, matricula)

if alumno_encontrado is None:
    print("Alumno no encontrado")
else:
    print("Alumno encontrado:")
    mostrar_alumno_con_estado(alumno_encontrado)
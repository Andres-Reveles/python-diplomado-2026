from entradas import pedir_texto_no_vacio, pedir_float_rango
from alumnos import (
    crear_alumno,
    buscar_alumno,
    matricula_disponible,
    mostrar_alumnos,
    mostrar_alumno_con_estado
)
from reportes import mostrar_reporte_grupo


print("=== Sistema modular de alumnos y calificaciones ===")


def mostrar_menu():
    print()
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Registrar calificación")
    print("5. Ver promedio y estado")
    print("6. Reporte general del grupo")
    print("7. Salir")


def pedir_alumno_existente(alumnos):
    matricula = pedir_texto_no_vacio("Ingresa la matrícula del alumno: ").upper()

    alumno = buscar_alumno(alumnos, matricula)

    if alumno is None:
        print("Alumno no encontrado")
        return None

    return alumno


def registrar_alumno(alumnos):
    matricula = pedir_texto_no_vacio("Ingresa la matrícula: ").upper()

    if not matricula_disponible(alumnos, matricula):
        print("Error: ya existe un alumno con esa matrícula")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
    carrera = pedir_texto_no_vacio("Ingresa la carrera: ")

    alumno = crear_alumno(matricula, nombre, carrera)

    alumnos.append(alumno)

    print("Alumno registrado correctamente")


def buscar_alumno_menu(alumnos):
    alumno = pedir_alumno_existente(alumnos)

    if alumno is None:
        return

    print("Alumno encontrado:")
    mostrar_alumno_con_estado(alumno)


def registrar_calificacion(alumnos):
    alumno = pedir_alumno_existente(alumnos)

    if alumno is None:
        return

    print("Alumno encontrado:")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")

    calificacion = pedir_float_rango("Ingresa la calificación: ", 0, 10)

    alumno["calificaciones"].append(calificacion)

    print("Calificación registrada correctamente")


def ver_promedio_estado(alumnos):
    alumno = pedir_alumno_existente(alumnos)

    if alumno is None:
        return

    print("=== Promedio y estado del alumno ===")
    mostrar_alumno_con_estado(alumno)


alumno_1 = crear_alumno("A001", "Angel", "ISC")
alumno_2 = crear_alumno("A002", "Luis", "Contaduría")
alumno_3 = crear_alumno("A003", "María", "Administración")

alumno_1["calificaciones"] = [9, 8, 10]
alumno_2["calificaciones"] = [5, 6, 5]

alumnos = [alumno_1, alumno_2, alumno_3]


while True:
    mostrar_menu()

    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_alumno(alumnos)

    elif opcion == "2":
        mostrar_alumnos(alumnos)

    elif opcion == "3":
        buscar_alumno_menu(alumnos)

    elif opcion == "4":
        registrar_calificacion(alumnos)

    elif opcion == "5":
        ver_promedio_estado(alumnos)

    elif opcion == "6":
        mostrar_reporte_grupo(alumnos)

    elif opcion == "7":
        print("Saliendo del sistema")
        break

    else:
        print("Opción inválida")
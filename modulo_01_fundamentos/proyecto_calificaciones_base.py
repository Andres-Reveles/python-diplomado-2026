print("=== Sistema de alumnos y calificaciones ===")


def crear_alumno(matricula, nombre, carrera):
    """
    Crea y retorna un diccionario que representa a un alumno.
    """
    return {
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera,
        "calificaciones": []
    }


def mostrar_alumno(alumno):
    """
    Muestra la información de un alumno.
    """
    print(f"Matrícula: {alumno['matricula']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Calificaciones: {alumno['calificaciones']}")


def mostrar_alumnos(alumnos):
    """
    Muestra todos los alumnos registrados.
    """
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return

    print("=== Alumnos registrados ===")

    for indice, alumno in enumerate(alumnos, start=1):
        print(f"Alumno {indice}")
        mostrar_alumno(alumno)
        print("--------------------")


alumno_1 = crear_alumno("A001", "Angel", "ISC")
alumno_2 = crear_alumno("A002", "Luis", "Contaduría")
alumno_3 = crear_alumno("A003", "María", "Administración")

alumnos = [alumno_1, alumno_2, alumno_3]

mostrar_alumnos(alumnos)
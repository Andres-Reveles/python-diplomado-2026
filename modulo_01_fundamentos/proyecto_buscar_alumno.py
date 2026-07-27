print("=== Buscar alumno por matrícula ===")


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


def buscar_alumno(alumnos, matricula):
    """
    Busca un alumno por matrícula.

    Retorna el alumno si existe.
    Retorna None si no existe.
    """
    for alumno in alumnos:
        if alumno["matricula"] == matricula:
            return alumno

    return None


alumnos = [
    crear_alumno("A001", "Angel", "ISC"),
    crear_alumno("A002", "Luis", "Contaduría"),
    crear_alumno("A003", "María", "Administración")
]

matricula_buscar = input("Ingresa la matrícula del alumno: ").strip().upper()

alumno_encontrado = buscar_alumno(alumnos, matricula_buscar)

if alumno_encontrado is None:
    print("Alumno no encontrado")
else:
    print("Alumno encontrado:")
    mostrar_alumno(alumno_encontrado)
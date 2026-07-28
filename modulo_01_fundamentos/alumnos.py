def crear_alumno(matricula, nombre, carrera):
    return {
        "matricula": matricula,
        "nombre": nombre,
        "carrera": carrera,
        "calificaciones": []
    }


def buscar_alumno(alumnos, matricula):
    for alumno in alumnos:
        if alumno["matricula"] == matricula:
            return alumno

    return None


def matricula_disponible(alumnos, matricula):
    alumno = buscar_alumno(alumnos, matricula)
    return alumno is None


def calcular_promedio(alumno):
    calificaciones = alumno["calificaciones"]

    if len(calificaciones) == 0:
        return None

    return sum(calificaciones) / len(calificaciones)


def obtener_estado(alumno):
    promedio = calcular_promedio(alumno)

    if promedio is None:
        return "Sin calificaciones"

    if promedio >= 6:
        return "Aprobado"

    return "Reprobado"


def mostrar_alumno(alumno):
    print(f"Matrícula: {alumno['matricula']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Calificaciones: {alumno['calificaciones']}")


def mostrar_alumno_con_estado(alumno):
    promedio = calcular_promedio(alumno)
    estado = obtener_estado(alumno)

    print(f"Matrícula: {alumno['matricula']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Calificaciones: {alumno['calificaciones']}")

    if promedio is None:
        print("Promedio: Sin calificaciones")
    else:
        print(f"Promedio: {promedio:.2f}")

    print(f"Estado: {estado}")


def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return

    print("=== Alumnos registrados ===")

    for indice, alumno in enumerate(alumnos, start=1):
        print(f"Alumno {indice}")
        mostrar_alumno_con_estado(alumno)
        print("--------------------")
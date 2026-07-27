print("=== Promedio y estado del alumno ===")


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


def calcular_promedio(alumno):
    """
    Calcula el promedio de un alumno.

    Retorna None si no tiene calificaciones.
    """
    calificaciones = alumno["calificaciones"]

    if len(calificaciones) == 0:
        return None

    return sum(calificaciones) / len(calificaciones)


def obtener_estado(alumno):
    """
    Retorna el estado académico del alumno.
    """
    promedio = calcular_promedio(alumno)

    if promedio is None:
        return "Sin calificaciones"

    if promedio >= 6:
        return "Aprobado"

    return "Reprobado"


def mostrar_alumno_con_estado(alumno):
    """
    Muestra los datos del alumno, su promedio y su estado.
    """
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


alumno_1 = crear_alumno("A001", "Angel", "ISC")
alumno_2 = crear_alumno("A002", "Luis", "Contaduría")
alumno_3 = crear_alumno("A003", "María", "Administración")

alumno_1["calificaciones"].append(9)
alumno_1["calificaciones"].append(8)
alumno_1["calificaciones"].append(10)

alumno_2["calificaciones"].append(5)
alumno_2["calificaciones"].append(6)
alumno_2["calificaciones"].append(5)

alumnos = [alumno_1, alumno_2, alumno_3]

for alumno in alumnos:
    mostrar_alumno_con_estado(alumno)
    print("--------------------")
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


def matricula_disponible(alumnos, matricula):
    """
    Valida si una matrícula está disponible.
    """
    alumno = buscar_alumno(alumnos, matricula)

    return alumno is None


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
    Obtiene el estado académico del alumno.
    """
    promedio = calcular_promedio(alumno)

    if promedio is None:
        return "Sin calificaciones"

    if promedio >= 6:
        return "Aprobado"

    return "Reprobado"
from alumnos import calcular_promedio, obtener_estado


def obtener_alumnos_con_calificaciones(alumnos):
    return [
        alumno for alumno in alumnos
        if len(alumno["calificaciones"]) > 0
    ]


def obtener_alumnos_aprobados(alumnos):
    return [
        alumno for alumno in alumnos
        if obtener_estado(alumno) == "Aprobado"
    ]


def obtener_alumnos_reprobados(alumnos):
    return [
        alumno for alumno in alumnos
        if obtener_estado(alumno) == "Reprobado"
    ]


def calcular_promedio_grupo(alumnos):
    alumnos_con_calificaciones = obtener_alumnos_con_calificaciones(alumnos)

    if len(alumnos_con_calificaciones) == 0:
        return None

    suma_promedios = sum(
        calcular_promedio(alumno)
        for alumno in alumnos_con_calificaciones
    )

    return suma_promedios / len(alumnos_con_calificaciones)


def obtener_mejor_alumno(alumnos):
    alumnos_con_calificaciones = obtener_alumnos_con_calificaciones(alumnos)

    if len(alumnos_con_calificaciones) == 0:
        return None

    return max(
        alumnos_con_calificaciones,
        key=lambda alumno: calcular_promedio(alumno)
    )


def obtener_alumno_menor_promedio(alumnos):
    alumnos_con_calificaciones = obtener_alumnos_con_calificaciones(alumnos)

    if len(alumnos_con_calificaciones) == 0:
        return None

    return min(
        alumnos_con_calificaciones,
        key=lambda alumno: calcular_promedio(alumno)
    )


def mostrar_alumno_resumen(alumno):
    promedio = calcular_promedio(alumno)
    estado = obtener_estado(alumno)

    if promedio is None:
        promedio_texto = "Sin calificaciones"
    else:
        promedio_texto = f"{promedio:.2f}"

    print(f"{alumno['matricula']} - {alumno['nombre']} - Promedio: {promedio_texto} - Estado: {estado}")


def mostrar_reporte_grupo(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return

    cantidad_alumnos = len(alumnos)
    alumnos_con_calificaciones = obtener_alumnos_con_calificaciones(alumnos)
    alumnos_aprobados = obtener_alumnos_aprobados(alumnos)
    alumnos_reprobados = obtener_alumnos_reprobados(alumnos)

    promedio_grupo = calcular_promedio_grupo(alumnos)
    mejor_alumno = obtener_mejor_alumno(alumnos)
    alumno_menor_promedio = obtener_alumno_menor_promedio(alumnos)

    print("=== Reporte general del grupo ===")
    print(f"Cantidad de alumnos registrados: {cantidad_alumnos}")
    print(f"Alumnos con calificaciones: {len(alumnos_con_calificaciones)}")
    print(f"Alumnos aprobados: {len(alumnos_aprobados)}")
    print(f"Alumnos reprobados: {len(alumnos_reprobados)}")

    if promedio_grupo is None:
        print("Promedio general del grupo: Sin calificaciones")
    else:
        print(f"Promedio general del grupo: {promedio_grupo:.2f}")

    print()

    if mejor_alumno is None:
        print("Mejor alumno: Sin calificaciones")
    else:
        print("Mejor alumno:")
        mostrar_alumno_resumen(mejor_alumno)

    print()

    if alumno_menor_promedio is None:
        print("Alumno con menor promedio: Sin calificaciones")
    else:
        print("Alumno con menor promedio:")
        mostrar_alumno_resumen(alumno_menor_promedio)
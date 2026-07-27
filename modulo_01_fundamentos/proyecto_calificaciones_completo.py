print("=== Sistema de alumnos y calificaciones ===")


def mostrar_menu():
    print()
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Buscar alumno")
    print("4. Registrar calificación")
    print("5. Ver promedio y estado de un alumno")
    print("6. Reporte general del grupo")
    print("7. Salir")


def pedir_texto_no_vacio(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


def pedir_float_rango(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = float(entrada)

            if numero < minimo or numero > maximo:
                print(f"Error: el número debe estar entre {minimo} y {maximo}")
                continue

            return numero

        except ValueError:
            print("Error: debes ingresar un número válido")


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


def pedir_alumno_existente(alumnos):
    matricula = pedir_texto_no_vacio("Ingresa la matrícula del alumno: ").upper()

    alumno = buscar_alumno(alumnos, matricula)

    if alumno is None:
        print("Alumno no encontrado")
        return None

    return alumno


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


def mostrar_alumno_resumen(alumno):
    promedio = calcular_promedio(alumno)
    estado = obtener_estado(alumno)

    if promedio is None:
        promedio_texto = "Sin calificaciones"
    else:
        promedio_texto = f"{promedio:.2f}"

    print(f"{alumno['matricula']} - {alumno['nombre']} - Promedio: {promedio_texto} - Estado: {estado}")


def mostrar_alumnos(alumnos):
    if len(alumnos) == 0:
        print("No hay alumnos registrados")
        return

    print("=== Alumnos registrados ===")

    for indice, alumno in enumerate(alumnos, start=1):
        print(f"Alumno {indice}")
        mostrar_alumno_con_estado(alumno)
        print("--------------------")


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
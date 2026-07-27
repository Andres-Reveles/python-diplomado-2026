print("=== Registrar calificaciones ===")


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


def pedir_texto_no_vacio(mensaje):
    """
    Pide un texto y no permite que esté vacío.
    """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: el texto no puede estar vacío")
            continue

        return texto


def pedir_float_rango(mensaje, minimo, maximo):
    """
    Pide un número decimal dentro de un rango.
    """
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


def pedir_alumno_existente(alumnos):
    """
    Pide una matrícula y retorna el alumno si existe.
    Si no existe, retorna None.
    """
    matricula = pedir_texto_no_vacio("Ingresa la matrícula del alumno: ").upper()

    alumno = buscar_alumno(alumnos, matricula)

    if alumno is None:
        print("Alumno no encontrado")
        return None

    return alumno


def registrar_calificacion(alumnos):
    """
    Registra una calificación a un alumno existente.
    """
    alumno = pedir_alumno_existente(alumnos)

    if alumno is None:
        return

    print("Alumno encontrado:")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")

    calificacion = pedir_float_rango("Ingresa la calificación: ", 0, 10)

    alumno["calificaciones"].append(calificacion)

    print("Calificación registrada correctamente")


alumnos = [
    crear_alumno("A001", "Angel", "ISC"),
    crear_alumno("A002", "Luis", "Contaduría"),
    crear_alumno("A003", "María", "Administración")
]

registrar_calificacion(alumnos)

print()
print("=== Alumno actualizado ===")

matricula_buscar = input("Ingresa nuevamente la matrícula para consultar: ").strip().upper()
alumno_encontrado = buscar_alumno(alumnos, matricula_buscar)

if alumno_encontrado is None:
    print("Alumno no encontrado")
else:
    mostrar_alumno(alumno_encontrado)
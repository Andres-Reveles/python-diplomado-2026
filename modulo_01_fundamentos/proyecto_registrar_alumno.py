print("=== Registrar alumno ===")


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


def matricula_disponible(alumnos, matricula):
    """
    Valida que no exista un alumno con la misma matrícula.
    """
    alumno = buscar_alumno(alumnos, matricula)

    return alumno is None


def registrar_alumno(alumnos):
    """
    Registra un alumno nuevo en la lista de alumnos.
    """
    matricula = pedir_texto_no_vacio("Ingresa la matrícula: ").upper()

    if not matricula_disponible(alumnos, matricula):
        print("Error: ya existe un alumno con esa matrícula")
        return

    nombre = pedir_texto_no_vacio("Ingresa el nombre: ")
    carrera = pedir_texto_no_vacio("Ingresa la carrera: ")

    alumno = crear_alumno(matricula, nombre, carrera)

    alumnos.append(alumno)

    print("Alumno registrado correctamente")


alumnos = [
    crear_alumno("A001", "Angel", "ISC"),
    crear_alumno("A002", "Luis", "Contaduría"),
    crear_alumno("A003", "María", "Administración")
]

registrar_alumno(alumnos)

print()
mostrar_alumnos(alumnos)
print("=== Corrección de errores comunes ===")


def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()

        try:
            numero = int(entrada)
            return numero

        except ValueError:
            print("Error: debes ingresar un número entero válido")


def calcular_promedio(calificaciones):
    try:
        promedio = sum(calificaciones) / len(calificaciones)
        return promedio

    except ZeroDivisionError:
        print("Error: no hay calificaciones registradas")
        return None


def obtener_calificacion(calificaciones):
    if len(calificaciones) == 0:
        print("No hay calificaciones registradas")
        return

    for indice, calificacion in enumerate(calificaciones, start=1):
        print(f"{indice}. {calificacion}")

    opcion = pedir_entero("Elige el número de calificación: ")

    try:
        calificacion = calificaciones[opcion - 1]
        print(f"Calificación elegida: {calificacion}")

    except IndexError:
        print("Error: esa calificación no existe")


def mostrar_dato_alumno(alumno):
    clave = input("¿Qué dato quieres ver? nombre/edad/promedio: ").strip().lower()

    try:
        print(f"{clave}: {alumno[clave]}")

    except KeyError:
        print("Error: ese dato no existe")


calificaciones = []

print()
print("Calculando promedio...")
promedio = calcular_promedio(calificaciones)

if promedio is not None:
    print(f"Promedio: {promedio}")

print()
print("Agregando calificaciones...")
calificaciones.append(10)
calificaciones.append(8)
calificaciones.append(9)

promedio = calcular_promedio(calificaciones)

if promedio is not None:
    print(f"Promedio: {promedio}")

print()
obtener_calificacion(calificaciones)

alumno = {
    "nombre": "Andrés",
    "edad": 23
}

print()
mostrar_dato_alumno(alumno)
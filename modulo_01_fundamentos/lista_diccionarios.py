print("--- Lista de Diccionarios ---")

alumnos = [
    {
        "nombre": "Andres",
        "edad": 23,
        "carrera": "ISC",
        "promedio": 9.5
    },
    {
        "nombre": "Maria",
        "edad": 52,
        "carrera": "Enfermeria",
        "promedio": 9.0
    },
    {
        "nombre": "Enrique",
        "edad": 54,
        "carrera": "Arquitectura",
        "promedio": 8.5
    }
]

print("Lista de alumnos:")
for alumno in alumnos:
    print(f"Nombre: {alumno['nombre']}")
    print(f"Edad: {alumno['edad']}")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Promedio: {alumno['promedio']}")
    print("--------------------")
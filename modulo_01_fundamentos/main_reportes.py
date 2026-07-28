from alumnos import crear_alumno, mostrar_alumnos
from reportes import mostrar_reporte_grupo

print("=== Uso del módulo reportes ===")

alumno_1 = crear_alumno("A001", "Angel", "ISC")
alumno_2 = crear_alumno("A002", "Luis", "Contaduría")
alumno_3 = crear_alumno("A003", "María", "Administración")
alumno_4 = crear_alumno("A004", "Dylan", "ISC")

alumno_1["calificaciones"] = [9, 8, 10]
alumno_2["calificaciones"] = [5, 6, 5]
alumno_3["calificaciones"] = []
alumno_4["calificaciones"] = [7, 8, 8]

alumnos = [alumno_1, alumno_2, alumno_3, alumno_4]

mostrar_alumnos(alumnos)

print()
mostrar_reporte_grupo(alumnos)
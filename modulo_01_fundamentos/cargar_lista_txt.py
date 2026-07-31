print("=== Cargar lista desde archivo TXT ===")

alumnos = []
with open("alumnos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        alumno = linea.strip()  # Eliminar espacios en blanco y saltos de línea
        alumnos.append(alumno)

print("Lista de alumnos cargada desde 'alumnos.txt' correctamente.")
print(alumnos)

print()
print("=== Alumnos registrados ===")
for alumno in alumnos:
    print(f"- {alumno}")
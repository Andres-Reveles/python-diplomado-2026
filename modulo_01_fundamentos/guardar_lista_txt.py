print("=== Guardar lista en archivo TXT ===")

alumnos = ["Angel", "Enrique", "Gisela"]

with open("alumnos.txt", "w", encoding="utf-8") as archivo:  # Abrir archivo en modo escritura
    for alumno in alumnos:  # Iterar sobre cada alumno en la lista
        archivo.write(alumno + "\n")  # Escribir el nombre del alumno en el archivo, seguido de un salto de línea

print("Lista de alumnos guardada en 'alumnos.txt' correctamente.")
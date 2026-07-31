print("=== Escritura de archivo TXT ===")

archivo = open("notas.txt", "w", encoding="utf-8")  # Abrir archivo en modo escritura

archivo.write("Hola, este archivo fue creado desde Python\n")  # Escribir contenido en el archivo
archivo.write("Estoy aprendiendo persistencia de datos.\n")  # Escribir otra línea en el archivo
archivo.write("Clase 18 - Archivos TXT.\n")  # Escribir otra línea en el archivo
archivo.close()  # Cerrar el archivo


print("Archivo 'notas.txt' creado y contenido escrito correctamente.")
print("=== Lectura de archivo TXT ===   " )

archivo = open("notas.txt", "r", encoding="utf-8")  # Abrir archivo en modo lectura

contenido = archivo.read()  # Leer todo el contenido del archivo

archivo.close()  # Cerrar el archivo

print("Contenido del archivo 'notas.txt':")
print(contenido)

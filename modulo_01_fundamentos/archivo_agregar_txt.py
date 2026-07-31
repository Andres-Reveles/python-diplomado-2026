print("=== Agregar contenido a archivo TXT ===")

with open("notas.txt", "a", encoding="utf-8") as archivo:  # Abrir archivo en modo agregar
    archivo.write("Esta linea fue agregada después.\n")  # Agregar contenido al archivo
    archivo.write("Estoy usando el modo append.\n")  # Agregar otra línea al archivo

print("Contenido agregado al archivo 'notas.txt' correctamente.")


# "w" = escribir desde cero
# "r" = leer
# "a" = agregar al final
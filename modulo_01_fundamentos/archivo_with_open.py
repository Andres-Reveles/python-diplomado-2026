print("=== Escritura de archivo TXT con 'with open' ===")

with open("notas.txt", "r", encoding="utf-8") as archivo:  # Abrir archivo en modo lectura con 'with open'
    contenido = archivo.read()  # Leer todo el contenido del archivo

print("Contenido del archivo 'notas.txt':")
print(contenido)
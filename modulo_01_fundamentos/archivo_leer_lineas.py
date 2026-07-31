print("=== Lectura de archivo TXT línea por línea ===")

with open("notas.txt", "r", encoding="utf-8") as archivo:  # Abrir archivo en modo lectura
    for linea in archivo:  # Iterar sobre cada línea del archivo
        print(linea.strip())  # Imprimir la línea sin espacios en blanco al inicio y al final
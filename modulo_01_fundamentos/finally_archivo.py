print("=== finally con archivos ===")

archivo = None

try:
    archivo = open("archivo_prueba_finally.txt", "r", encoding="utf-8")

    contenido = archivo.read()

    print("Contenido del archivo:")
    print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe")

finally:
    if archivo is not None:
        archivo.close()
        print("Archivo cerrado correctamente")

    print("Operación finalizada")
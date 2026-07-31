print("=== Cargar archivo inexistente ===")


def cargar_productos_txt(nombre_archivo):
    productos = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()

                datos = linea.split("|")

                producto = {
                    "codigo": datos[0],
                    "nombre": datos[1],
                    "precio": float(datos[2]),
                    "stock": int(datos[3])
                }

                productos.append(producto)

    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe. Se iniciará con lista vacía.")

    return productos


productos = cargar_productos_txt("archivo_que_no_existe.txt")

print()
print("Productos cargados:")
print(productos)
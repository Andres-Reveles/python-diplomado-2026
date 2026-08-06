import csv
import json

print(" ---Funciones CSV y JSON---")

def crear_producto(nombre, precio, cantidad, stock):
    return {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "stock": stock
    }

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos para mostrar.")
        return
    
    print("Lista de productos:")

    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Stock: {producto['stock']}")


def guardar_productos_csv(productos, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        campos = ['nombre', 'precio', 'cantidad', 'stock']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
        
        escritor_csv.writeheader()
        for producto in productos:
            escritor_csv.writerow(producto)

    print(f"Productos guardados en el archivo CSV: {nombre_archivo}")

def guardar_productos_json(productos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(productos, archivo_json, indent=4)

    print(f"Productos guardados en el archivo JSON: {nombre_archivo}")

def cargar_productos_csv(nombre_archivo):
    productos = []
    try:
        with open(nombre_archivo, mode='r') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            for fila in lector_csv:
                producto = {
                    "Codigo": fila['Codigo'],
                    "nombre": fila['nombre'],
                    "precio": float(fila['precio']),
                    "stock": fila['stock']
                }
                productos.append(producto)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los productos desde CSV: {e}")

    return productos

def guardar_productos_json(productos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo_json:
        json.dump(productos, archivo_json, indent=4)

    print(f"Productos guardados en el archivo JSON: {nombre_archivo}")

def cargar_productos_json(nombre_archivo):
    productos = []
    try:
        with open(nombre_archivo, 'r') as archivo_json:
            productos = json.load(archivo_json)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al cargar los productos desde JSON: {e}")

    return productos


productos = [
    crear_producto("P001", "Mouse", 250, 10),
    crear_producto("P002", "Teclado", 500, 5),
    crear_producto("P003", "Monitor", 1500, 3)
]

guardar_productos_csv(productos, "productos.csv")
guardar_productos_json(productos, "productos.json")

print("Productos guardados en CSV y JSON")

print()

print(" ---Cargando productos desde CSV---")
productos_desde_csv = cargar_productos_csv("productos.csv")
mostrar_productos(productos_desde_csv)

print()
print(" ---Cargando productos desde JSON---")
productos_desde_json = cargar_productos_json("productos.json")
mostrar_productos(productos_desde_json)

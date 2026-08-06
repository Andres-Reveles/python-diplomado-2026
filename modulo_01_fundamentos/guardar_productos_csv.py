import csv

print("-- Guardar productos en un archivo CSV --")

productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 10.99, "stock": 50},
    {"codigo": "P002", "nombre": "Teclado", "precio": 15.49, "stock": 30},
    {"codigo": "P003", "nombre": "Monitor", "precio": 7.99, "stock": 20}
]

with open("productos.csv", mode="w", newline="") as archivo_csv:
    columnas = ["codigo", "nombre", "precio", "stock"]

    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=columnas)
    escritor_csv.writeheader()

    for producto in productos:
        escritor_csv.writerow(producto)

print("Productos guardados en 'productos.csv' exitosamente.")
print("=== Guardar productos en archivo TXT ===")

productos = [
    {"Codigo": "P001", "Nombre": "Mouse", "Precio": 250.99, "stock": 10},
    {"Codigo": "P002", "Nombre": "Teclado", "Precio": 500.99, "stock": 5},
    {"Codigo": "P003", "Nombre": "Monitor", "Precio": 1500.99, "stock": 3},
    {"Codigo": "P004", "Nombre": "Impresora", "Precio": 2000.99, "stock": 2},

]

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for producto in productos:
        linea = f"{producto['Codigo']}|{producto['Nombre']}|{producto['Precio']}|{producto['stock']}\n"
        archivo.write(linea)

print("Productos guardados en 'productos.txt' correctamente.")
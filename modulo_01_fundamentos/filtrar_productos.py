print("--- Filtrar Productos ---")

productos = [
    {"codigo": "P001", "nombre": "Mouse", "precio": 250, "stock": 10},
    {"codigo": "P002", "nombre": "Teclado", "precio": 500, "stock": 5},
    {"codigo": "P003", "nombre": "Monitor", "precio": 1500, "stock": 2},
    {"codigo": "P004", "nombre": "Impresora", "precio": 2000, "stock": 0},
]

#aqui solo hacemos la lista con la condicion
productos_caros = [p for p in productos if p["precio"] > 1000]

productos_sin_stock = [p for p in productos if p["stock"] == 0]

productos_disponibles = [p for p in productos if p["stock"] > 0]


#en cada uno de los casos imprimimos la lista resultante

print("Productos caros:")
for p in productos_caros:
    print(p)

print("Productos sin stock:")
for p in productos_sin_stock:
    print(p)

print("Productos disponibles:")
for p in productos_disponibles:
    print(p)
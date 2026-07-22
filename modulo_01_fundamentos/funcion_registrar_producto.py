print("--- Función registrar producto ---")

productos = [
    {"Codigo": "P001", "nombre": "Laptop", "precio": 12000, "stock": 10},
    {"Codigo": "P002", "nombre": "Mouse", "precio": 500, "stock": 50},
    {"Codigo": "P003", "nombre": "Teclado", "precio": 800, "stock": 30},
    {"Codigo": "P004", "nombre": "Monitor", "precio": 3000, "stock": 20}
]

def buscar_producto(productos, codigo):
    for producto in productos:
        if producto["Codigo"] == codigo:
            return producto
    return None

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No hay productos disponibles.")
        return
    for indice, producto in enumerate(productos, start=1):
        print(f"{indice}. Código: {producto['Codigo']}")
        print(f"   Nombre: {producto['nombre']}")
        print(f"   Precio: {producto['precio']}")
        print(f"   Stock: {producto['stock']}")
        print("--------------------")


def registrar_producto(productos):
    codigo = input("Ingrese el código del producto: ")
    
    if codigo.strip() == "":
        print("El código del producto no puede estar vacío.")
        return
    
    producto_existente = buscar_producto(productos, codigo)
    if producto_existente is not None:
        print("El código del producto ya existe. No se puede registrar.")
        return
    
    nombre = input("Ingrese el nombre del producto: ")
    if nombre.strip() == "":
        print("El nombre del producto no puede estar vacío.")
        return
    precio = input("Ingrese el precio del producto: ")
    if precio.strip() == "":
        print("El precio del producto no puede estar vacío.")
        return
    stock = input("Ingrese el stock del producto: ")
    if stock.strip() == "":
        print("El stock del producto no puede estar vacío.")
        return
    productos.append({
        "Codigo": codigo,
        "nombre": nombre,
        "precio": float(precio),
        "stock": int(stock)
    })
    print("Producto registrado exitosamente.")

registrar_producto(productos)
print("Lista de productos actualizada:")
mostrar_productos(productos)
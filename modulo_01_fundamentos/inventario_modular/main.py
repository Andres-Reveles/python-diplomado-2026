from producto import crear_producto
from inventario_servicio import (
    mostrar_productos,
    registrar_producto,
    buscar_producto_menu,
    actualizar_precio,
    actualizar_stock,
    eliminar_producto
)

print("=== Inventario modular ===")

productos = [
    crear_producto("P001", "Mouse", 250.0, 10),
    crear_producto("P002", "Teclado", 500.0, 5),
    crear_producto("P003", "Monitor", 3200.0, 2)
]

mostrar_productos(productos)

print()
registrar_producto(productos)

print()
buscar_producto_menu(productos)

print()
actualizar_precio(productos)

print()
actualizar_stock(productos)

print()
eliminar_producto(productos)

print()
print("=== Inventario actualizado ===")
mostrar_productos(productos)
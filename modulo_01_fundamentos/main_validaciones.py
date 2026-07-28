from validaciones import texto_no_vacio, numero_positivo, calificacion_valida

print("=== Uso de módulo validaciones ===")

nombre = input("Ingresa tu nombre: ").strip()
precio = float(input("Ingresa un precio: "))
calificacion = float(input("Ingresa una calificación: "))

if texto_no_vacio(nombre):
    print("Nombre válido")
else:
    print("Nombre inválido")

if numero_positivo(precio):
    print("Precio válido")
else:
    print("Precio inválido")

if calificacion_valida(calificacion):
    print("Calificación válida")
else:
    print("Calificación inválida")
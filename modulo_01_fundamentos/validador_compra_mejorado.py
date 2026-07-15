print("=== Validador de compra mejorado ===")

edad = int(input("Ingresa tu edad: "))
saldo = float(input("Ingresa tu saldo disponible: "))
total_compra = float(input("Ingresa el total de la compra: "))
respuesta_ine = input("¿Tienes INE? Escribe si o no: ").strip().lower()

tiene_ine = respuesta_ine == "si" or respuesta_ine == "sí"

if edad < 0:
    print("Edad inválida")

elif saldo < 0:
    print("Saldo inválido")

elif total_compra <= 0:
    print("El total de la compra debe ser mayor a cero")

elif edad < 18:
    print("Compra rechazada: debes ser mayor de edad")

elif not tiene_ine:
    print("Compra rechazada: necesitas INE")

elif saldo < total_compra:
    print("Compra rechazada: saldo insuficiente")

else:
    cambio = saldo - total_compra
    print("Compra aprobada")
    print(f"Cambio restante: {cambio}")
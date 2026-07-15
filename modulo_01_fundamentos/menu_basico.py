print("=== Menú básico ===")
print("1. Saludar")
print("2. Mostrar edad")
print("3. Salir")

opcion = input("Elige una opción: ")

if opcion == "1":
    print("Hola, bienvenido al programa")
elif opcion == "2":
    edad = int(input("Ingresa tu edad: "))
    print(f"Tu edad es: {edad}")
elif opcion == "3":
    print("Saliendo del programa")
else:
    print("Opción inválida")
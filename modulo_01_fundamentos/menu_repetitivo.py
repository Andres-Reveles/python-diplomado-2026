print("---Menu Repetitivo---")

while True:
    print()
    print("1 - Saludar")
    print("2 - Mostrar mensaje")
    print("3 - Salir")
    
    opcion = input("Ingrese una opcion: ").strip()

    if opcion == "1":
        print("Hola, Bienvenido al programa")

    elif opcion == "2": 
        mensaeje = input("Ingrese un mensaje: ")
        print(f"El mensaje ingresado es: {mensaeje}")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida, por favor ingrese una opcion valida")

print("=== Repetir mensaje con break ===")

while True:
    mensaje = input("Escribe algo o escribe 'salir' para terminar: ").strip().lower()

    if mensaje == "salir":
        print("Programa terminado")
        break

    print(f"Escribiste: {mensaje}")
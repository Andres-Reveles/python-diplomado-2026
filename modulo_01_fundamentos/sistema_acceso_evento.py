print("-----Sistema accesso a evento-----")
edad = int(input("Ingrese su edad: "))
respuesta_boleto = input("¿Tiene boleto? (si/no): ").lower().strip()
respuesta_bloqueado = input("¿Está bloqueado? (si/no): ").lower().strip()
tiene_boleto = respuesta_boleto == "si" or respuesta_bloqueado == "no"
esta_bloqueado = respuesta_bloqueado == "si" or respuesta_boleto == "no"

if edad < 0:
    print("Edad inválida. Por favor, ingrese una edad válida.")
elif respuesta_boleto not in ["si", "no"]:
    print("Respuesta inválida. Por favor, responda con 'si' o 'no'.")
elif respuesta_bloqueado not in ["si", "no"]:
    print("Respuesta inválida. Por favor, responda con 'si' o 'no'.")
elif edad < 18:
    print("Acceso denegado. Debe ser mayor de edad para ingresar al evento.") 
elif not tiene_boleto:
    print("Acceso denegado. Debe tener un boleto válido para ingresar al evento.")
elif esta_bloqueado:
    print("Acceso denegado. Su acceso está bloqueado.")
else:
    print("Acceso permitido. ¡Bienvenido al evento!")

print("---Tabla de multiplicar ---")

numero = int(input("Ingrese un número: "))

for num in range(1, 11):
    resultado = numero * num
    print(f"{numero} x {num} = {resultado}")
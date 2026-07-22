print("--- Funciones de calculadora ---")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
    
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print()
print("--- Resultados ---")
print(f"Suma: {sumar(numero1, numero2)}")
print(f"Resta: {restar(numero1, numero2)}")
print(f"Multiplicación: {multiplicar(numero1, numero2)}")
print(f"División: {dividir(numero1, numero2)}")
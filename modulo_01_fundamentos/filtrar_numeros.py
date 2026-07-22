print("--- Filtrar Números ---")

#nueva_lista = [elemento for elemento in lista if condicion]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [n for n in numeros if n % 2 == 0]
print(pares)
impares = [n for n in numeros if n % 2 != 0]
print(impares)
mayores_a_cinco = [n for n in numeros if n > 5]
print(mayores_a_cinco)
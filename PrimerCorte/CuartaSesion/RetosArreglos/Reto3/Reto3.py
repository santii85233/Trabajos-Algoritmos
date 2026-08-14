palindromo = [1, 5, 9, 5, 1]
inicio = 0

while inicio < 5:
    if palindromo[inicio] != palindromo[5 - (inicio + 1)]:
        prueba = False
        break
    inicio += 1
    prueba = True

if prueba:
    print("El codigo ingresado es válido.")
else:
    print("El codigo ingresado es invalido.")

"""
inicio = 0
N = int(input("Ingrese la cantidad de numeros del codigo a ingresar:"))
if n<=0:
    print("La cantidad ingresada es invalida.")
palindromo = []
if N > 0:
    for i in range(N):
        valor = int(input(f"Ingrese el valor {i + 1} de su medición:"))
        palindromo.append(valor)

while inicio < N:
    if palindromo[inicio] != palindromo[N - (inicio + 1)]:
        prueba = False
        break
    inicio += 1
    prueba = True

if prueba:
    print("El codigo ingresado es válido.")
else:
    print("El codigo ingresado es invalido.")
"""
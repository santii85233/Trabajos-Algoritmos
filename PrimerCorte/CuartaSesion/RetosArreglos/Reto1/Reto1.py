Temperaturas =[20, -999, 22, 24, -999, 26]
error = -999
suma = 0
valido = 0
descartados = 0
promedio =0

for t in range(len(Temperaturas)):
    if Temperaturas[t] != error:
        suma += Temperaturas[t]
        valido += 1
    else:
        descartados +=1

promedio= suma/valido

print("Promedio:", promedio)
print("Valores Correctos: ", valido)
print("Valores invalidos:", descartados)
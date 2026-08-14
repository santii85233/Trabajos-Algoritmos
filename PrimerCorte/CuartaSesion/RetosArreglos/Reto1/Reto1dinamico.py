error = -999
suma = 0
valido = 0
descartados = 0
promedio =0
N= int(input("Ingrese la cantidad de temperaturas a ingresar:"))
Temperaturas=[]

if N > 0:
        for i in range(N):
                valor =int(input(f"Ingrese el valor {i+1} de su medición: "))
                Temperaturas.append(valor)
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
else:
    print("Ingrese un valor válido")


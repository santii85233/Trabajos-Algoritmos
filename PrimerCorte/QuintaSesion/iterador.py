matrizcosas=[[2,5,8,3,4],
             [1,3,3,6,9],
             [4,3,2,5,1]]
suma = 0
usos=[]
for c in range(len(matrizcosas)):
    for f in range(len(matrizcosas)):
        print("[",matrizcosas[f][c],"]", end="\t")
        suma +=matrizcosas[f][c]
        print(suma)
    usos.append(suma)
    suma = 0
    print()
    print(usos)
    #Que es una clase, que es un objeto, estructura en python, en c++, que cambia y principios fundamentales del poo
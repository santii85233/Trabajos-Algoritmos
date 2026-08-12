import random

dado1= random.randint(1, 6)
dado2= random.randint(1, 6)
suma=dado1+dado2

print("El dado 1 te ha dado:", dado1)
print("El dado 2 te ha dado:", dado2)

if dado1==1 and dado2==1:
    print("¡¡¡Eso es un PAR de Unos, has ganado!!!")
elif suma==3:
    print("¡¡¡Eso es un Tres, has ganado!!!")
elif suma==11:
    print("¡¡¡Eso es un Once, has ganado!!!")
elif suma==12:
    print(f"¡¡¡Eso es un Doce, has ganado!!!")
elif suma==7:
    print("¡¡¡Eso es un Siete, has ganado!!!")
else:
    print("has Perdido. Intenta denuevo.")
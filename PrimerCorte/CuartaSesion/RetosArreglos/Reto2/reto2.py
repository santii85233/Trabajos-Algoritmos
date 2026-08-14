lluvias=[0,1,1,0,1,1,1,0,1]
rachaActual=0
mejorRacha = 0
for i in lluvias:
    if lluvias[i]==1:
        rachaActual +=1
    if lluvias[i]==0: 
        mejorRacha = rachaActual
        rachaActual =0
print(f"La mayor racha de lluvias fue de {mejorRacha} dias.")
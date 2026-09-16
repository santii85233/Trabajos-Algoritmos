
#RETO 2
def potencia(a,b):
    if b==0:    return 1 #Caso Base si b es 0
    else:
        return a *potencia(a,b-1)   #Caso recursivo con a multiplicado por el resultado recursivo anterior

print(potencia(2,145))
#print(potencia(2,1000)) Si probara con esta potencia habria un stackoverflow

#RETO 2.1

def potenciapar(a,b):
    if b==0:    return 1 #Caso Base si b es 0
    elif b%2==0:    #Caso b Par
        b1=potenciapar(a,b/2)# Temporal para multiplicarla por si misma
        return b1*b1
    elif b%2!=0:    #Caso b Impar
        return a *potenciapar(a,b-1)   #Caso recursivo con a multiplicado por el resultado de potenciapar de b par


print(potenciapar(2,1000))
  

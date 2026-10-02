entrada=[73,74,75,71,69,72,76,73]
#Salida: [1,1,4,2,1,1,0,0]
def siguiente_mayor(a):
    n=len(a)
    res=[0]*n
    print(res)
    pila=[]
    for i in range (n):
        while pila and a[pila[-1]]<a[i]:
            j=pila.pop()
            res[j]=i-j
        pila.append(i)
    return res
   
print(siguiente_mayor(entrada))
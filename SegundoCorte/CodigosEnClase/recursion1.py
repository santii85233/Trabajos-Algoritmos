import time
nivel = 0

def factorial(n):
    global nivel
    print("|  " * nivel + f"factorial({n}) entra")
    nivel += 1
    r = 1 if n <= 1 else n * factorial(n - 1)
    nivel -= 1
    print("|  " * nivel + f"factorial({n}) devuelve {r}")
    return r

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("--- traza de la pila de llamadas ---")
start1= time.time()
rr1 = factorial(5)
end1= time.time()
time1= end1-start1
print("Resultado:", rr1)
print(f"Con un tiempo de: {time1:.7f} s")

start2= time.time()
rr2 = factorial(10)
end2= time.time()
time2= end2-start2
print("Resultado:", rr2)
print(f"Con un tiempo de: {time2:.7f} s")


start3= time.time()
rr3 = factorial(15)
end3= time.time()
time3= end3-start3
print("Resultado:", rr3)
print(f"Con un tiempo de: {time3:.7f} s")


print()

inicio1= time.time()
r1=fibonacci(5)
fin1= time.time()
tiempo1=fin1-inicio1

inicio2= time.time()
r2=fibonacci(10)
fin2= time.time()
tiempo2=fin2-inicio2

inicio3= time.time()
r3=fibonacci(15)
fin3= time.time()
tiempo3=fin3-inicio3

print("fibonacci(5) =", r1)
print(f"Con un tiempo de: {tiempo1:.7f} s")
print("fibonacci(10) =",r2)
print(f"Con un tiempo de: {tiempo2:.7f} s")
print("fibonacci(15) =", r3)
print(f"Con un tiempo de: {tiempo3:.7f} s")



"""
factorial(5) entra
|  factorial(4) entra
|  |  factorial(3) entra
|  |  |  factorial(2) entra
|  |  |  |  factorial(1) entra
|  |  |  |  factorial(1) devuelve 1
|  |  |  factorial(2) devuelve 2
|  |  factorial(3) devuelve 6
|  factorial(4) devuelve 24
factorial(5) devuelve 120
Resultado: 120
Con un tiempo de: 0.0003600 s
factorial(10) entra
|  factorial(9) entra
|  |  factorial(8) entra
|  |  |  factorial(7) entra
|  |  |  |  factorial(6) entra
|  |  |  |  |  factorial(5) entra
|  |  |  |  |  |  factorial(4) entra
|  |  |  |  |  |  |  factorial(3) entra
|  |  |  |  |  |  |  |  factorial(2) entra
|  |  |  |  |  |  |  |  |  factorial(1) entra
|  |  |  |  |  |  |  |  |  factorial(1) devuelve 1
|  |  |  |  |  |  |  |  factorial(2) devuelve 2
|  |  |  |  |  |  |  factorial(3) devuelve 6
|  |  |  |  |  |  factorial(4) devuelve 24
|  |  |  |  |  factorial(5) devuelve 120
|  |  |  |  factorial(6) devuelve 720
|  |  |  factorial(7) devuelve 5040
|  |  factorial(8) devuelve 40320
|  factorial(9) devuelve 362880
factorial(10) devuelve 3628800
Resultado: 3628800
Con un tiempo de: 0.0005362 s
factorial(15) entra
|  factorial(14) entra
|  |  factorial(13) entra
|  |  |  factorial(12) entra
|  |  |  |  factorial(11) entra
|  |  |  |  |  factorial(10) entra
|  |  |  |  |  |  factorial(9) entra
|  |  |  |  |  |  |  factorial(8) entra
|  |  |  |  |  |  |  |  factorial(7) entra
|  |  |  |  |  |  |  |  |  factorial(6) entra
|  |  |  |  |  |  |  |  |  |  factorial(5) entra
|  |  |  |  |  |  |  |  |  |  |  factorial(4) entra
|  |  |  |  |  |  |  |  |  |  |  |  factorial(3) entra
|  |  |  |  |  |  |  |  |  |  |  |  |  factorial(2) entra
|  |  |  |  |  |  |  |  |  |  |  |  |  |  factorial(1) entra
|  |  |  |  |  |  |  |  |  |  |  |  |  |  factorial(1) devuelve 1
|  |  |  |  |  |  |  |  |  |  |  |  |  factorial(2) devuelve 2
|  |  |  |  |  |  |  |  |  |  |  |  factorial(3) devuelve 6
|  |  |  |  |  |  |  |  |  |  |  factorial(4) devuelve 24
|  |  |  |  |  |  |  |  |  |  factorial(5) devuelve 120
|  |  |  |  |  |  |  |  |  factorial(6) devuelve 720
|  |  |  |  |  |  |  |  factorial(7) devuelve 5040
|  |  |  |  |  |  |  factorial(8) devuelve 40320
|  |  |  |  |  |  factorial(9) devuelve 362880
|  |  |  |  |  factorial(10) devuelve 3628800
|  |  |  |  factorial(11) devuelve 39916800
|  |  |  factorial(12) devuelve 479001600
|  |  factorial(13) devuelve 6227020800
|  factorial(14) devuelve 87178291200
factorial(15) devuelve 1307674368000
Resultado: 1307674368000
Con un tiempo de: 0.0008156 s

fibonacci(5) = 5
Con un tiempo de: 0.0000033 s
fibonacci(10) = 55
Con un tiempo de: 0.0000122 s
fibonacci(15) = 610
Con un tiempo de: 0.0001168 s

"""
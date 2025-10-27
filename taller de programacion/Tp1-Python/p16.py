#Generar los N números de la serie de Fibonacci. 
N = int(input("Ingrese la cantidad de números de la serie de Fibonacci: "))
a = 0
b = 1
if N >= 1:
    print(a)
if N >= 2:
    print(b)
for i in range(3, N + 1):
    c = a + b
    print(c)
    a = b
    b = c
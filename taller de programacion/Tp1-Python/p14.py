#Dado un número determinar si un número es primo o no. 
num = int(input("Ingresa el número: "))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
if cont == 2:
    print(num, "es primo")
else:
    print(num, "no es primo")

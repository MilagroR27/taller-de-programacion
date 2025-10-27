#Dado un número de 4 dígitos, presentar por pantalla todos sus divisores. 
num=int(input("Ingrese el número de 4 digitos"))
for i in range (1,num):
    if num % i ==0:
        print(i)
#Se ingresan N números enteros, presentar por pantalla el promedio de los pares y el promedio de los impares
contI=0
contP=0
sumP=0
sumI=0
N=int(input("Ingrese cuantos numeros desea colocar"))
for i in range(N):
    num=int(input("ingrese los numeros"))
    if num % 2 == 0:
        contP +=1
        sumP +=num
    else:
        contI +=1
        sumI +=num
if contP == 0:
    print("Usted no Ingreso numeros pares")
else:
    prom_P=sumP/contP
    print("El promedio de numeros pares es: ", prom_P)
if contI == 0:
    print("Usted no Ingreso numeros impares")
else:
    prom_I=sumI/contI
    print("El promedio de numeros impares es: ", prom_I)
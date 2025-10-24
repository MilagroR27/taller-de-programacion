#Se ingresan N valores numéricos. Se desea saber cuántos son positivos, cuantos negativos y cuantos iguales a cero. 
cont_p=0
cont_n=0
cont_c=0
N=int(input("Ingresa la cantidad de numeros que desea colocar "))
for i in range(N):
    num=int(input("Ingrese los numeros "))
    if num == 0:
        cont_c +=1
    elif num > 0:
        cont_p +=1
    else:
        cont_n +=1


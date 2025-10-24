#Se ingresan N valores numéricos. Determinar el mayor y el menor de los valores ingresados.
N=int(input("Ingrese la cantidad de Números "))
num=int(input("Ingrese un Número "))
num_M=num
num_Mi=num
for i in range (1,N):
    num1=int(input("Ingrese un Número "))
    if  num1 > num_M:
        num_M=num1
    else:
        if num1 < num_Mi:
            num_Mi=num1
print("El Número más grande es: ", num_M)
print("El Número más chico es: ", num_Mi)

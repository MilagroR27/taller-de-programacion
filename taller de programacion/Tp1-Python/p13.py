#Se ingresan N valores numéricos. Determinar la posición y el valor del mayor número par y el menor número impar de los valores 
# ingresados. Presentar por pantalla los resultados. 
mayorPar = 0
menorImpar = 0
posPar = 0
posImpar = 0
contPar = 0
contImpar = 0
i = 0
num = int(input("Ingrese números (0 para terminar): "))
while num != 0:
    i += 1
    if num % 2 == 0:
        if contPar == 0 or num > mayorPar:
            mayorPar = num
            posPar = i
        contPar += 1
    else:
        if contImpar == 0 or num < menorImpar:
            menorImpar = num
            posImpar = i
        contImpar += 1
    num = int(input())
if contPar > 0:
    print("El mayor número par es", mayorPar, "en la posición", posPar)
else:
    print("No se ingresó ningún número par")
if contImpar > 0:
    print("El menor número impar es", menorImpar, "en la posición", posImpar)
else:
    print("No se ingresó ningún número impar")

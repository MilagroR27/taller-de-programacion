#Se ingresan N números naturales presentar por pantalla la cantidad de números primos ingresados. 
contPrimos = 0
num = int(input("Ingrese números naturales (0 para terminar): "))
while num != 0:
    contDiv = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contDiv += 1
    if contDiv == 2:
        contPrimos += 1
    num = int(input())
print("La cantidad de números primos ingresados es:", contPrimos)

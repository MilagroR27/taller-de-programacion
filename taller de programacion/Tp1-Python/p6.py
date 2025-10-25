#Dado un número, expresado en el sistema binario, convertirlo al sistema decimal. Presentar ambos números. 
binario=int(input("Ingrese el número Binario: "))
binario_original=binario
potencia=1
decimal=0
while binario > 0:
    digito= binario % 10
    decimal= decimal + digito * potencia
    potencia= potencia * 2
    binario= binario//10
print("El Decimal del Binario", binario_original, "es: ", decimal)
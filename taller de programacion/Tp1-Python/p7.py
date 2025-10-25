#Dado un número, entero positivo, expresado en el sistema decimal, convertirlo al sistema binario. Presentar los dos números.
decimal=int(input("Ingrese el número Decimal: "))
decimal_original=decimal
posicion=1
binario=0
while decimal > 0:
    resto= decimal % 2
    binario= binario + resto * posicion
    posicion = posicion * 10
    decimal= decimal //2
print("El número Binario, del Decimal ",decimal_original, "es: ", binario)
#Ingresar un número natural N. Sin dividir ni multiplicar determinar si ese valor es o no par. Presentar por pantalla el resultado. 
n=int(input("Ingrese un número natural: "))
while n >= 1:
    n= n -2
if n == 0:
    print("El número es par")
else:
    print("El número es impar")
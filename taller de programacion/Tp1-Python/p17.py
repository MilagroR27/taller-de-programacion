#Se ingresa N números naturales, presentar por pantalla el número compuesto por los N valores ingresados. 
resultado = 0
num = int(input("Ingrese números naturales (0 para terminar): "))
while num != 0:
    resultado = resultado * 10 + num
    num = int(input())
print("El número compuesto es:", resultado)
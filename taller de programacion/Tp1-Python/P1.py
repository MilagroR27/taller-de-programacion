
#Escribir un programa que presente por pantalla en forma ordenada las tablas de multiplicar del 1 al 10. 
for i in range(1,11):
    print("tabla del", i, ":")
    for num in range (1,11):
        print(i, "X", num, "=", i*num)
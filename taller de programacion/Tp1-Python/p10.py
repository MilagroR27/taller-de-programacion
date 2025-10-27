#Ingresar N números naturales y presentar por pantalla cuantas series de números estrictamente crecientes aparecen.
cont_s = 0
largo_s = 1
N = int(input("Ingrese la cantidad de números: "))
anterior = int(input("Ingrese un número: "))
for i in range(2, N + 1):
    num = int(input("Ingrese un número: "))
    if num > anterior:
        largo_s += 1
    else:
        if largo_s >= 2:
            cont_s = cont_s + 1
        largo_s = 1 
    anterior = num
if largo_s >= 2:
    cont_s = cont_s + 1
print("Cantidad de series estrictamente crecientes:", cont_s)

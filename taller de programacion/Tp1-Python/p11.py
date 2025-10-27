# Dados N1 menor que N2, diseñar un algoritmo que sume los números enteros comprendidos entre N1 y N2. Presentar por pantalla dicha
# suma y un mensaje que indique de donde proviene la suma. 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    inicio = num2
    final = num1
else:
    inicio = num1
    final = num2
suma = 0
if final - inicio <= 1:
    print("No hay números comprendidos entre", inicio, "y", final, ". Suma = 0")
else:
    for i in range(inicio + 1, final):
        suma += i
    print("La suma de los números comprendidos entre", inicio, "y", final, "es:", suma)

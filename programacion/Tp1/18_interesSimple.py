#Numero Interes Simple que ingrese tres valores (capital, tasa, tiempo) y muestre por pantalla el resultado de calcular el Numero interes simple
capital=float(input("Ingrese su capital: "))
tasa=float(input("Ingrese la tasa: "))
tiempo=float(input("Ingrese el tiempo: "))
constante=100
resultadoInteres=(capital*tasa*tiempo)/constante
print("El interes de tres simple es: ", resultadoInteres)
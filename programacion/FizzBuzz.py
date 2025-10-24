#Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre
#cada impresión), sustituyendo los siguientes:
#Múltiplos de 3 por la palabra "fizz".
#Múltiplos de 5 por la palabra "buzz".
#Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#Algoritmo fizzbuzz
"""	Definir num1, num2 Como Entero
i= 0
	Mientras i <= 15 Hacer
		i = i +1
		Si i mod 3 = 0 Entonces
			escribir "fizz"
		SiNo
			si i mod 5 = 0 Entonces
				Escribir "buzz"
			SiNo
				Si i mod 5 = 0 y i mod 3 = 0 Entonces
					Escribir "fizzbuzz"
				FinSi
			FinSi
		Fin Si
		Escribir i
	Fin Mientras
FinAlgoritmo"""

i = 0

while i< 100:
    i += 1 
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)



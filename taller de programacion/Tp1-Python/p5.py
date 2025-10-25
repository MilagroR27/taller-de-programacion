#Dado un número natural de 4 o más dígitos, presentar por pantalla el número y su invertido.
num=int(input("Ingrese el Número: "))
num_original=num
num_inverso=0
while num >0:
    digito= num % 10
    num_inverso= num_inverso * 10 + digito
    num= num//10
print("El Número Original era:", num_original, "Y El Número Inverso es: ", num_inverso)
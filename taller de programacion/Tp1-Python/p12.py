#Si se ingresa un número natural presentar por pantalla el desarrollo del factorial de dicho número, como así también 
# el valor del factorial. 
n = int(input("Ingrese un número natural: "))
resultado = 1
print("El desarrollo del factorial de", n, "es:")
for i in range(n, 0, -1):
    print(i)
    if i > 1:
        print("*")
    resultado = resultado * i
print("El factorial de", n, "es:", resultado)

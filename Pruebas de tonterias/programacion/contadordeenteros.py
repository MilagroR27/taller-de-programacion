cont_c = 0   # Contador de ceros
cont_p = 0   # Contador de positivos
cont_n = 0   # Contador de negativos

for i in range(10):
    num = int(input("Ingresa un número: "))
    if num == 0:
        cont_c += 1
    elif num > 0:
        cont_p += 1
    else:
        cont_n += 1

# Mostrar los resultados al final
print("Cantidad de ceros:", cont_c)
print("Cantidad de positivos:", cont_p)
print("Cantidad de negativos:", cont_n)

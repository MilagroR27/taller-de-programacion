#llamado SueldoMensual que ingrese el valor de la hora y las horas que trabaja el empleado por día y muestre por pantalla el mensual que recibe. Suponga que trabaja 22 dias al mes
valorHora=float(input("Ingrese el valor de las horas trabajadas "))
horaTrabajada=int(input("Ingrese las horas trabajadas "))
dias=int(input("Ingrese los dias trabajados"))
resultadoSueldoMensual=(valorHora*horaTrabajada*dias)
print("Su sueldo mensual sera de: ", resultadoSueldoMensual)
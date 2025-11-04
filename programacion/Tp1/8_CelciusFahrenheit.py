#ConvertirCelsiusaFahrenheit que ingrese el valor en grados Celsius y muestre por pantalla el resultado en grados Fahrenheit
gradosC=float(input("Ingrese la temperatura en grados celsius: "))
constante1=9/5
constante2=32
resultadoFahrenheit = (constante1 * gradosC) + constante2
resultadoFahrenheit = "{:.2f}".format(resultadoFahrenheit)
print("Los grados en Fahrenheit son:", resultadoFahrenheit)

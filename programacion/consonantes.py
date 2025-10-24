# //Lea 5 letras y decir cuántas son vocales, cuántas consonantes y cuántas no son letras. 
"""Algoritmo vocales_consonantes
	Definir letra, palabra_L, palabra_M Como Caracter
	Definir const_voc, const_cons Como Entero
	const_cons=0
	const_voc=0
	para i=1 hasta 5 Hacer
		Escribir "ingrese su palabra"
		Leer palabra
		palabra = Minusculas(palabra)
		para j=1 hasta Longitud(palabra) Hacer
			letra=SubCadena(palabra,j,j)
		si letra >="a" y letra <= "z" Entonces
		Si letra = "a" O letra = "e" O letra = "i" O letra = "o" O letra = "u" Entonces
			const_voc= const_voc +1
		SiNo
			const_cons= const_cons +1
		FinSi
	FinSi
FinPara
FinPara
	Escribir const_cons
	Escribir const_voc
FinAlgoritmo"""
const_cons=0
const_voc=0
for i in range (5):
    palabra= input("ingrese su palabra: ")
    palabra_m= palabra.lower()
    for j in range (len(palabra_m)):
        sub=palabra_m[j]
        if sub >= "a" and sub<= "z":
            if sub in ("a" or "e" or "i" or "o" or "u"):
                const_voc +=1
            else:
                const_cons +=1
            
print(const_cons)
print(const_voc)

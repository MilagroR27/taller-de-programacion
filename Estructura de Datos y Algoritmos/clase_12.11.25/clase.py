"""#  nombre.py  --> def. pronombre  (nombre):
def pronombre(nombre):
        print(nombre)   #definimos el procedimiento
resultado="Milagro"
pronombre(resultado)    #llamamos al procedimiento, "resultado ": es una variable,  
print(resultado) #Si ponemos print(nombre), nos da error porque se "destruye" la variable y se la cambia a "resultado"

#procedimiento lo hace todo en el mismo lugar (encapsulamiento), y la funcion si devuelve un valor"""
 #------------------------ Funcion--------------
"""def pronom(nombre):
    return nombre
resultado="Milagro"
print(pronom(resultado))"""
#--------------------Promedio de 3 notas con funcion-----------
"""n1=int(input("Ingrese una nota"))
n2=int(input("Ingrese una nota"))
n3=int(input("Ingrese una nota"))
def promedio(n1,n2,n3):
    prom=(n1+n2+n3)/3
    return prom
print(promedio(n1,n2,n3))"""

#----------------Promedio de 3 notas con procedimiento-----------

def notas(n1,n2,n3):
    promedio=(n1+n2+n3)/3
    print(promedio)
notas(6,6,6)
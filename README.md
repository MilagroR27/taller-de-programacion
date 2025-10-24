# 📘 Repositorio de Estudios – Milagro Rodríguez

Bienvenida/o a mi repositorio personal de estudio 👩‍💻  
Aquí guardo **todos mis ejercicios, trabajos prácticos y proyectos** realizados durante la **Tecnicatura Superior en Desarrollo de Software**.  
El propósito de este espacio es practicar, organizar mi progreso y tener un respaldo digital de todo lo que voy aprendiendo.

---

## 🗂️ Estructura del repositorio

### 🧩 **Estructura de Datos y Algoritmos**
En esta carpeta voy incorporando los ejercicios de la materia **Estructura de Datos y Algoritmos**.  
Primero los desarrollo en hoja (a mano), luego los paso a **PSeInt** y finalmente los practico en **Python**.  
La idea es mostrar la evolución de cada ejercicio desde su planteo teórico hasta su implementación en código.

---

### 🐍 **Programacion**
Contiene los ejercicios de la materia **Programación**, realizados inicialmente en **PSeInt** y luego convertidos a **Python** para practicar la sintaxis y el razonamiento lógico en código real.  
Todos los ejercicios pertenecen a la materia.

---

### 🧱 **Taller de Programacion**
Incluye los **trabajos prácticos (TPs)** de la materia **Taller de Programación**.  
Cada ejercicio fue primero realizado en **PSeInt** y luego traducido a **Python** para consolidar los conceptos aprendidos en clase.

---

### 🧪 **Sandbox**
Zona de práctica libre o “laboratorio de código”.  
Aquí guardo pequeños programas o pruebas sueltas que uso para experimentar o repasar conceptos (por ejemplo, el clásico `FizzBuzz.py`).  
No pertenecen a ninguna materia en particular.

---

### 🧱 **Proyecto Final**
Espacio reservado para el **proyecto integrador** de la Tecnicatura.  
Todavía no está definido, pero en principio se desarrollará en **Python**, y posiblemente integre **Arduino** o alguna aplicación práctica (como un proyecto físico o interactivo).

---

## 💻 Ejemplo de ejercicio

**Ejercicio:**  
Se ingresan N valores numéricos. Se desea saber cuántos son positivos, cuántos negativos y cuántos iguales a cero.

```python
cont_p = 0
cont_n = 0
cont_c = 0

N = int(input("Ingresa la cantidad de numeros: "))
for i in range(N):
    num = int(input("Ingrese un numero: "))
    if num == 0:
        cont_c += 1
    elif num > 0:
        cont_p += 1
    else:
        cont_n += 1

print("Ceros:", cont_c)
print("Positivos:", cont_p)
print("Negativos:", cont_n)

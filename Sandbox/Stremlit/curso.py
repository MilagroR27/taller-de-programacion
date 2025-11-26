import streamlit as st
import pandas as pd
import numpy as np
"""
==============================================================
CURSO COMPLETO DE STREAMLIT
Teoría + ejemplos de cada función
==============================================================

Este archivo NO es una app, sino un curso:
- Explica TODAS las funciones de Streamlit.
- Explica para qué sirve cada una.
- Muestra cómo se usa con un ejemplo.
- Está ordenado para que estudies desde cero a avanzado.

Podés leerlo, ejecutarlo o copiar partes para tus propias apps.
"""


# =============================================================
# 1. ¿QUÉ ES STREAMLIT?
# =============================================================
"""
Streamlit es una librería de Python para crear aplicaciones web
de forma ultra simple, sin usar HTML, CSS o JavaScript.

Es ideal para:
- Sistemas de gestión
- Dashboards
- Formularios
- Prototipos rápidos
- Apps con bases de datos

Siempre se usa así:

1) Instalás streamlit
2) Lo importás
3) Ejecutás la app con: python -m streamlit run archivo.py
"""


# =============================================================
# 2. INSTALACIÓN
# =============================================================
"""
Instalar Streamlit:

    pip install streamlit

Verificar instalación:

    python -m streamlit --version
"""


# =============================================================
# 3. IMPORTACIÓN
# =============================================================



"""
Siempre se importa así:

    import streamlit as st
"""


# =============================================================
# 4. EJECUTAR UNA APP
# =============================================================
"""
Para ejecutar, ir a la carpeta del archivo y ejecutar:

    python -m streamlit run archivo.py
"""


# =============================================================
# 5. CONFIGURACIÓN DE LA PÁGINA
# =============================================================

st.set_page_config(
    page_title="Curso Completo Streamlit",
    layout="centered"  # puede ser "centered" o "wide"
)

"""
Sirve para configurar:
- Título del navegador
- Layout (ancho de la página)
"""


# =============================================================
# 6. TÍTULOS Y TEXTO
# =============================================================

st.title("6. Títulos y Texto")
st.header("Header")
st.subheader("Subheader")
st.write("st.write() sirve para mostrar cualquier cosa.")
st.text("Texto simple sin formato.")
st.markdown("**Markdown permite negritas, *cursivas*, listas, etc.**")
st.caption("Texto pequeño, estilo nota al pie.")

"""
Funciones:
- st.title(): título grande
- st.header(): título mediano
- st.subheader(): subtítulo
- st.text(): texto plano
- st.write(): muestra cualquier cosa
- st.markdown(): formato tipo Markdown o HTML
- st.caption(): texto pequeño, aclaración
"""


# =============================================================
# 7. ENTRADAS (INPUTS)
# =============================================================
st.title("7. Entradas (Inputs)")

nombre = st.text_input("text_input: texto")
edad = st.number_input("number_input: número", min_value=0)
comentarios = st.text_area("text_area: texto largo")

genero = st.selectbox("selectbox: menú", ["Femenino", "Masculino", "Otro"])
opcion = st.radio("radio: una sola opción", ["A", "B", "C"])

acepto = st.checkbox("checkbox: verdadero o falso")
nivel = st.slider("slider: rango", 0, 100)

fecha = st.date_input("date_input: fecha")
hora = st.time_input("time_input: hora")

archivo = st.file_uploader("file_uploader: subir archivo")

color = st.color_picker("color_picker: elegir color")

"""
RESUMEN:

- st.text_input(): texto corto
- st.text_area(): texto largo
- st.number_input(): números
- st.selectbox(): menú desplegable
- st.radio(): opciones tipo botones
- st.checkbox(): verdadero/falso
- st.slider(): seleccionar un número o rango
- st.date_input(): fecha
- st.time_input(): hora
- st.file_uploader(): subir archivos
- st.color_picker(): elegir color
"""


# =============================================================
# 8. BOTONES
# =============================================================

st.title("8. Botones")

if st.button("Hacer clic"):
    st.success("¡Botón presionado!")

"""
st.button("Texto"):
- Devuelve True SOLO cuando se hace clic.
"""


# =============================================================
# 9. MENSAJES VISUALES
# =============================================================

st.title("9. Mensajes visuales")

st.success("Éxito")
st.error("Error")
st.warning("Advertencia")
st.info("Información")

"""
Sirven para dar feedback al usuario.
"""


# =============================================================
# 10. TABLAS Y DATOS
# =============================================================

st.title("10. Tablas y Datos")

tabla_simple = [
    ["Coca Cola", 900, 25],
    ["Fanta", 850, 20],
    ["Sprite", 780, 18]
]

st.table(tabla_simple)
st.dataframe(tabla_simple)

st.json({"producto": "Coca Cola", "precio": 900})

"""
- st.table(): tabla estática
- st.dataframe(): tabla interactiva (scroll, ordenamiento)
- st.json(): muestra JSON bonito
"""


# =============================================================
# 11. LAYOUT: columnas, contenedores, expander
# =============================================================

st.title("11. Layout")

col1, col2 = st.columns(2)

with col1:
    st.write("Columna 1")

with col2:
    st.write("Columna 2")

with st.container():
    st.write("Contenido agrupado")

with st.expander("Mostrar más"):
    st.write("Contenido oculto al inicio")

"""
- st.columns(): divide en columnas
- st.container(): agrupa elementos
- st.expander(): contenido oculto desplegable
"""


# =============================================================
# 12. SIDEBAR (barra lateral)
# =============================================================

st.title("12. Sidebar (Barra lateral)")

op = st.sidebar.selectbox("Menú lateral", ["Inicio", "Productos", "Ventas"])
st.write("Elegiste:", op)

"""
Todo lo que uses con st.sidebar aparecerá a la izquierda.
"""


# =============================================================
# 13. session_state (variables persistentes)
# =============================================================

st.title("13. session_state (persistencia)")

if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Sumar"):
    st.session_state.contador += 1

st.write("Valor:", st.session_state.contador)

"""
session_state permite que datos NO se borren al recargar la app.
"""


# =============================================================
# 14. ARCHIVOS
# =============================================================

st.title("14. Archivos")

archivo_subido = st.file_uploader("Subir archivo")
if archivo_subido:
    st.success("Archivo recibido")

st.download_button(
    label="Descargar archivo",
    data="Ejemplo de contenido",
    file_name="archivo.txt"
)

"""
- st.file_uploader(): subir archivos
- st.download_button(): descargar archivos
"""


# =============================================================
# 15. GRÁFICOS
# =============================================================

st.title("15. Gráficos (charts)")

#import pandas as pd
#import numpy as np

df = pd.DataFrame({
    "x": np.arange(10),
    "y": np.random.randint(1, 10, 10)
})

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

"""
- st.line_chart(): gráfico de líneas
- st.bar_chart(): gráfico de barras
- st.area_chart(): gráfico de área
"""


# =============================================================
# 16. st.experimental_rerun()
# =============================================================

st.title("16. Rerun")

if st.button("Recargar página"):
    st.experimental_rerun()

"""
Recarga completamente la app.
Útil cuando editás, eliminás o actualizás datos.
"""


# =============================================================
# 17. st.set_page_config() (config inicial)
# =============================================================

"""
Ya lo usamos arriba:

st.set_page_config(
    page_title="Curso Streamlit",
    layout="wide"
)
"""


# =============================================================
# 18. PÁGINAS MULTIPLE (estructura profesional)
# =============================================================
"""
Estructura recomendada:

/mi_app
    app.py
    pages/
        1_Productos.py
        2_Ventas.py
        3_Reportes.py

Streamlit detecta automáticamente las páginas de /pages.

"""


# =============================================================
# FIN DEL CURSO
# =============================================================

st.title("FIN DEL CURSO")
st.success("Curso completo de Streamlit finalizado.")

"""
=====================================================================
 STREAMLIT — CURSO PROFESIONAL COMPLETO
 Arquitectura + SQLite + CRUD + Optimización
=====================================================================

Este archivo es un documento educativo completo.
Podés leerlo, estudiarlo y copiar partes en tus apps reales.

NO es una app; es un curso escrito dentro de un archivo .py,
con explicaciones claras + ejemplos cortos.
"""

# import streamlit as st

# =====================================================================
# 0. CONFIGURACIÓN DE PÁGINA
# =====================================================================
st.set_page_config(
    page_title="Curso Profesional de Streamlit",
    layout="wide",
)

# =====================================================================
# 1. CURSO 2 — ARQUITECTURA PROFESIONAL PARA APPS STREAMLIT
# =====================================================================
st.title("CURSO 2 — Arquitectura Profesional en Streamlit")
st.write("""
Este curso explica CÓMO organizar una app Streamlit como un sistema real.

Cuando una app crece, NO podés tener todo en un solo archivo.  
Lo correcto es separar tu proyecto en estas capas:

📌 **1. Capa de Datos (Base de Datos y Acceso a Datos)**  
    - db.py  
    - Funciones como: crear_conexion(), obtener_productos(), insertar(), etc.

📌 **2. Capa de Lógica de Negocio (Reglas, cálculos)**  
    - utils.py  
    - Funciones: calcular_precio_final(), validar_campos(), etc.

📌 **3. Capa de Presentación (Interfaz Streamlit)**  
    - app.py  
    - Código visual: inputs, botones, tablas, charts

📌 **4. Múltiples páginas (pages/)**  
    - 1_Inicio.py  
    - 2_Productos.py  
    - 3_Ventas.py  
    - 4_Reportes.py

Esta estructura permite:
- reusar código
- mantenimiento más fácil
- apps grandes sin enredos
- navegación automática entre páginas
""")

# ---------------------------------------------------------------------
# Estructura recomendada
# ---------------------------------------------------------------------
st.header("Estructura recomendada de carpetas")
st.code("""
/mi_app
    app.py                # Página principal
    db.py                 # Acceso a SQLite
    utils.py              # Funciones auxiliares
    styles.py             # (opcional) Estilos
    /pages
        1_Inicio.py
        2_Productos.py
        3_Ventas.py
        4_Reportes.py
    /assets               # imágenes, css, csv, etc.
""")

# ---------------------------------------------------------------------
# Ejemplo de db.py
# ---------------------------------------------------------------------
st.subheader("Ejemplo de archivo db.py (acceso a SQLite)")
st.code("""
import sqlite3

DB_NAME = "negocio.db"

def crear_conexion():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def obtener_productos():
    conn = crear_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return datos
""")

# ---------------------------------------------------------------------
# Ejemplo de utils.py
# ---------------------------------------------------------------------
st.subheader("Ejemplo de archivo utils.py (lógica de negocio)")
st.code("""
def calcular_precio_venta(costo, margen):
    return costo * (1 + margen/100)
""")

# ---------------------------------------------------------------------
# Ejemplo de app.py
# ---------------------------------------------------------------------
st.subheader("Ejemplo de app.py usando todo lo anterior")
st.code("""
import streamlit as st
from db import obtener_productos
from utils import calcular_precio_venta

productos = obtener_productos()

for p in productos:
    precio = calcular_precio_venta(p["costo"], p["margen"])
    st.write(p["nombre"], "-", precio)
""")

# =====================================================================
# 2. CURSO 3 — STREAMLIT + SQLITE: CRUD PROFESIONAL
# =====================================================================
st.title("CURSO 3 — Streamlit + SQLite (CRUD Profesional)")
st.write("""
Este curso explica:
✔ cómo conectar Streamlit con SQLite  
✔ cómo crear, leer, actualizar y borrar datos  
✔ patrones reales para apps de negocio  
✔ cómo diseñar formularios profesionales  
✔ cómo evitar errores de concurrencia  
""")

# ---------------------------------------------------------------------
# Concepto: CRUD
# ---------------------------------------------------------------------
st.header("¿Qué es un CRUD?")
st.write("""
CRUD significa:

- **C**reate → Crear registros  
- **R**ead → Leer registros  
- **U**pdate → Actualizar  
- **D**elete → Eliminar  

Toda aplicación de gestión usa un CRUD.
""")

# ---------------------------------------------------------------------
# 1. Crear conexión
# ---------------------------------------------------------------------
st.subheader("1. Conexión a SQLite")
st.code("""
def get_conn():
    conn = sqlite3.connect("negocio.db")
    conn.row_factory = sqlite3.Row
    return conn
""")

# ---------------------------------------------------------------------
# 2. Crear
# ---------------------------------------------------------------------
st.subheader("2. Crear registros")
st.code("""
def insertar_producto(nombre, categoria, costo):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre,categoria,costo) VALUES (?,?,?)",
        (nombre, categoria, costo)
    )
    conn.commit()
    conn.close()
""")

# ---------------------------------------------------------------------
# 3. Leer
# ---------------------------------------------------------------------
st.subheader("3. Leer registros")
st.code("""
def obtener_productos():
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM productos")
    datos = c.fetchall()
    conn.close()
    return datos
""")

# ---------------------------------------------------------------------
# 4. Actualizar
# ---------------------------------------------------------------------
st.subheader("4. Actualizar registros")
st.code("""
def actualizar(id, nombre, costo):
    conn = get_conn()
    c = conn.cursor()
    c.execute(
        "UPDATE productos SET nombre=?, costo=? WHERE id=?",
        (nombre, costo, id)
    )
    conn.commit()
    conn.close()
""")

# ---------------------------------------------------------------------
# 5. Eliminar
# ---------------------------------------------------------------------
st.subheader("5. Eliminar registros")
st.code("""
def eliminar(id):
    conn = get_conn()
    c = conn.cursor()
    c.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
""")

# ---------------------------------------------------------------------
# Uso en Streamlit
# ---------------------------------------------------------------------
st.subheader("Cómo se usa un CRUD en Streamlit")
st.code("""
productos = obtener_productos()

for p in productos:
    st.write(p["id"], p["nombre"], p["costo"])

if st.button("Añadir"):
    insertar_producto("Nuevo", "Categoria", 100)
    st.experimental_rerun()
""")

# =====================================================================
# 3. CURSO 4 — OPTIMIZACIÓN Y BUENAS PRÁCTICAS
# =====================================================================
st.title("CURSO 4 — Optimización + Buenas Prácticas en Streamlit")
st.write("""
Aquí ves cómo hacer que tu app:

✔ cargue más rápido  
✔ consuma menos recursos  
✔ no se recargue innecesariamente  
✔ mantenga datos persistentes  
✔ sea apta para producción  
""")

# ---------------------------------------------------------------------
# 1. Usar session_state para evitar recargas
# ---------------------------------------------------------------------
st.header("1. session_state para evitar recargas")
st.code("""
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Sumar"):
    st.session_state.contador += 1

st.write(st.session_state.contador)
""")

st.write("""
❗Sin session_state, cada clic reinicia la app completa.
""")

# ---------------------------------------------------------------------
# 2. Guardar datos temporalmente (cache)
# ---------------------------------------------------------------------
st.header("2. Cacheo de funciones (cache de datos)")

st.code("""
@st.cache_data
def obtener_datos():
    ... consulta lenta ...
    return datos
""")

st.write("""
✔ Permite que Streamlit NO ejecute funciones pesadas en cada recarga  
✔ Especialmente útil con SQLite, Excel o consultas remotas  
""")

# ---------------------------------------------------------------------
# 3. Evitar consultas repetidas
# ---------------------------------------------------------------------
st.header("3. Evitar consultas repetidas")

st.code("""
productos = obtener_datos()   # Se ejecuta 1 sola vez
""")

# ---------------------------------------------------------------------
# 4. Usar formularios (st.form)
# ---------------------------------------------------------------------
st.header("4. Usar st.form para evitar recargas molestas")
st.code("""
with st.form("form1"):
    nombre = st.text_input("Nombre")
    precio = st.number_input("Precio")
    enviar = st.form_submit_button("Guardar")
""")

st.write("""
Los formularios permiten enviar TODO junto sin recargar por cada input.
""")

# ---------------------------------------------------------------------
# 5. Dividir la app en componentes
# ---------------------------------------------------------------------
st.header("5. Dividir tu app en funciones")

st.code("""
def vista_agregar():
    nombre = st.text_input("Nombre")
    if st.button("Guardar"):
        insertar(nombre)

def vista_listar():
    productos = obtener()
    st.table(productos)
""")

# ---------------------------------------------------------------------
# 6. Buenas prácticas generales
# ---------------------------------------------------------------------
st.header("6. Buenas prácticas")

st.markdown("""
### ✔ Usar nombres claros
### ✔ Separar vistas en funciones
### ✔ Separar DB en `db.py`
### ✔ Evitar lógica dentro del botón
### ✔ Usar `st.experimental_rerun()` luego de CRUD
### ✔ Usar session_state
### ✔ Evitar consultas repetidas
""")

# =====================================================================
# FIN DE LOS 3 CURSOS
# =====================================================================
st.title("FIN DE LOS CURSOS AVANZADOS")
st.success("Completaste los 3 cursos profesionales de Streamlit 🎉")

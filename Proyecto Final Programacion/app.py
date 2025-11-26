# Importamos streamlit, y le decimos que para llamarlo usaremos "st"
import streamlit as st

# Importamos insertar_producto y obtener_productos desde db
from db import insertar_producto, obtener_productos

# Le colocamos el título a la página
st.title("Gestión de Productos")

# Creamos un menú en la barra lateral
opcion = st.sidebar.selectbox("Menú", ["Agregar Producto", "Ver Productos"])

# -----------------------------
# OPCIÓN: AGREGAR PRODUCTO
# -----------------------------
if opcion == "Agregar Producto":
    st.subheader("Agregar un nuevo producto")

    # Inputs del formulario
    nombre = st.text_input("Nombre")
    categoria = st.text_input("Categoría")
    costo = st.number_input("Costo", min_value=0.0, help="")
    margen = st.number_input("Margen (%)", min_value=0.0, help="")
    stock = st.number_input("Stock", min_value=0, step=1, help="")
    stock_minimo = st.number_input("Stock mínimo", min_value=0, step=1, help="")

    # Botón guardar
    if st.button("Guardar"):
        insertar_producto(nombre, categoria, costo, margen, stock, stock_minimo)
        st.success("Producto guardado con éxito")


# -----------------------------
# OPCIÓN: VER PRODUCTOS
# -----------------------------
elif opcion == "Ver Productos":
    st.subheader("Lista de productos")
    productos = obtener_productos()
    st.dataframe(productos)

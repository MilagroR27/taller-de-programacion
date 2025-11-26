import sqlite3

DB_NAME = "negocio.db"

def crear_conexion():
    conn = sqlite3.connect(DB_NAME)
    return conn

# PRAGMA: sirve para ver información interna de la base o de una tabla
# table_info: Es una instrucción interna de SQLite, que se usa únicamente con PRAGMA.
# fetchall devuelve una lista de tuplas
def verificar_tabla():
    # Iniciamos la conexion con la tabla
    conn = crear_conexion()
    cursor = conn.cursor()
    # Ejecutamos PRAGMA para ver la estructura
    cursor.execute("PRAGMA table_info(Productos)")
    info = cursor.fetchall()
    conn.close()
    print(info)

def insertar_producto(Nombre, Categoria, Costo, Margen, Stock, Stock_Minimo):
    # Abrir conexión
    conn = crear_conexion()
    cursor = conn.cursor()
    # Armar y ejecutar el INSERT
    cursor.execute(
        """
        INSERT INTO Productos (Nombre, Categoria, Costo, Margen, Stock, Stock_Minimo)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (Nombre, Categoria, Costo, Margen, Stock, Stock_Minimo)
    )
    # Guardar cambios
    conn.commit()
    # Cerrar la conexión
    conn.close()

def obtener_productos():
    # Abrir conexión
    conn = crear_conexion()
    cursor = conn.cursor()
    # Ejecutar el SELECT
    cursor.execute("SELECT * FROM Productos")
    # Traer todas las filas
    productos = cursor.fetchall()
    # Cerrar la conexión
    conn.close()
    return productos

# "__name__" es una variable especial que Python crea automáticamente en cada archivo:
# "__main__" es simplemente un texto (un string) que Python usa para decir:
# Si este archivo se ejecuta directamente, se entra en este bloque.
if __name__ == "__main__":
    print("Conexión exitosa")
    verificar_tabla()

    # Insertar un producto de prueba
    insertar_producto(
        "Coca Cola 2.25L",
        "Bebidas",
        950.0,   # costo
        25.0,    # margen
        10,      # stock
        2        # stock mínimo
    )

    # Ver todos los productos
    productos = obtener_productos()
    print(productos)

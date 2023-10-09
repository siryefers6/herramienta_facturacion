from .conexion_db import ConexionDB


# Función para crear la tabla 'clientes' en la base de datos.


def crear_tabla() -> None:
    conexion = ConexionDB()

    sql = """CREATE TABLE clientes(
    rut_cliente INTEGER,
    nombre_cliente VARCHAR(100),
    PRIMARY KEY(rut_cliente)
    )"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        print('Tabla "clientes", Creada.')

    except:
        print('Tabla "clientes", ya existe.')

# Función para borrar la tabla 'clientes' de la base de datos.


def borrar_tabla() -> None:
    conexion = ConexionDB()

    sql = 'DROP TABLE clientes'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        print('Tabla "clientes", eliminada.')

    except:
        print('Tabla "clientes", no existe.')

# Clase cliente que representa un cliente.


class Cliente:
    def __init__(self, rut_cliente: int, nombre_cliente: str) -> None:
        self.rut_cliente = rut_cliente
        self.nombre_cliente = nombre_cliente.strip().upper()

    def __str__(self) -> str:
        return f'Cliente[{self.rut_cliente}, {self.nombre_cliente}]'

# Función para guardar cliente en base de datos.


def guardar(cliente: object) -> None:
    conexion = ConexionDB()

    sql = f"""INSERT INTO clientes(rut_cliente, nombre_cliente)
    VALUES({cliente.rut_cliente}, '{cliente.nombre_cliente}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except Exception as e:
        print(
            f'Error al intentar guardar cliente:\n{e}.\nCliente no guardado.')

# Función para listar todos los clientes de la base de datos.


def listar() -> list:
    conexion = ConexionDB()

    lista_clientes = []
    sql = 'SELECT * FROM clientes'

    try:
        conexion.cursor.execute(sql)
        lista_clientes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        print('Debe crear tabla "clientes" en base de datos.')

    return lista_clientes

# Función para editar un cliente en la base de datos.


def editar(cliente: object, rut_cliente: int) -> None:
    conexion = ConexionDB()

    sql = f"""UPDATE clientes
    SET nombre_cliente = '{cliente.nombre_cliente}'
    WHERE rut_cliente = {rut_cliente}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except Exception as e:
        print(f'Error al intentar editar cliente:\n{e}.\nCliente no editado.')

# Función para eliminar un cliente de la base de datos.


def eliminar(rut_cliente: int) -> None:
    conexion = ConexionDB()

    sql = f"DELETE FROM clientes WHERE rut_cliente = {rut_cliente}"

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except Exception as e:
        print(
            f'Error al intentar eliminar cliente:\n{e}.\nCliente no eliminado.')

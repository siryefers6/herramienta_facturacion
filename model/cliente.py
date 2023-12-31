import pandas as pd
from .conexion_db import ConexionDB


# Clase cliente que representa un cliente.


class Cliente:
    def __init__(self, rut_cliente: int, nombre_cliente: str) -> None:
        self.rut_cliente = rut_cliente
        self.nombre_cliente = nombre_cliente.strip().upper()

    def __str__(self) -> str:
        return f'Cliente[{self.rut_cliente}, {self.nombre_cliente}]'

    # Función para crear la tabla 'clientes' en la base de datos.


    def crear_tabla(self) -> None:
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


    def borrar_tabla(self) -> None:
        conexion = ConexionDB()

        sql = 'DROP TABLE clientes'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "clientes", eliminada.')

        except:
            print('Tabla "clientes", no existe.')
    # Función para guardar cliente en base de datos.


    def guardar(self) -> None:
        conexion = ConexionDB()

        sql = f"""INSERT INTO clientes(rut_cliente, nombre_cliente)
        VALUES({self.rut_cliente}, '{self.nombre_cliente}')"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except Exception as e:
            print(
                f'Error al intentar guardar cliente:\n{e}.\nCliente no guardado.')

    # Función para listar todos los clientes de la base de datos.


    def listar(self) -> list:
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


    def editar(self) -> None:
        conexion = ConexionDB()

        sql = f"""UPDATE clientes
        SET nombre_cliente = '{self.nombre_cliente}'
        WHERE rut_cliente = {self.rut_cliente}"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(f'Error al intentar editar cliente:\n{e}.\nCliente no editado.')

    # Función para eliminar un cliente de la base de datos.


    def eliminar(self) -> None:
        conexion = ConexionDB()

        sql = f"DELETE FROM clientes WHERE rut_cliente = {self.rut_cliente}"

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar eliminar cliente:\n{e}.\nCliente no eliminado.')

    def importar_csv(self) -> None:
        i = 0
        # Intenta leer el archivo CSV con diferentes encodings
        encodings = ['utf-8', 'ISO-8859-1', 'latin1']
        for encoding in encodings:
            try:
                df = pd.read_csv('clientes.csv', encoding=encoding, header=None)
                # Si tiene éxito, rompe el bucle
                break
            except UnicodeDecodeError:
                print(f'Error al leer con encoding {encoding}. Intentando con otro.')

        df.columns = ['rut_cliente', 'nombre_cliente']

        lista_clientes = df.to_dict(orient='records')
        for cliente in lista_clientes:
            try:
                Cliente(cliente['rut_cliente'], cliente['nombre_cliente']).guardar()
            except Exception as e:
                i += 1
                continue

        print('Documentos importados.')
        print(f'Documentos ya existentes {i}.')

    # Función para listar todos los rut de clientes de la base de datos.


    def listar_ruts(self) -> list:
        lista_clientes = self.listar(Cliente)
        lista_ruts = []
        for cliente in lista_clientes:
            lista_ruts.append(cliente[0])

        return lista_ruts
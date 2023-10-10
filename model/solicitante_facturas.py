import pandas as pd
from .conexion_db import ConexionDB


# Clase SolicitanteFacturas que representa un Solicitante de facturas.


class SolicitanteFacturas:
    def __init__(self, cod_solicitante: int, nombre_solicitante: str, cod_planilla: int) -> None:
        self.cod_solicitante = cod_solicitante
        self.nombre_solicitante = nombre_solicitante.strip().upper()
        self.cod_planilla = cod_planilla

    def __str__(self) -> str:
        return f'SolicitanteFacturas[{self.cod_solicitante}, {self.nombre_solicitante}, {self.cod_planilla}]'

    # Función para crear la tabla 'solicitantes_facturas' en la base de datos.

    def crear_tabla(self) -> None:
        conexion = ConexionDB()

        sql = """CREATE TABLE solicitantes_facturas(
        cod_solicitante INTEGER,
        nombre_solicitante VARCHAR(100),
        cod_planilla INTEGER,
        PRIMARY KEY(cod_solicitante)
        )"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "solicitantes_facturas", Creada.')

        except:
            print('Tabla "solicitantes_facturas", ya existe.')

    # Función para borrar la tabla 'solicitantes_facturas' de la base de datos.

    def borrar_tabla(self) -> None:
        conexion = ConexionDB()

        sql = 'DROP TABLE solicitantes_facturas'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "solicitantes_facturas", eliminada.')

        except:
            print('Tabla "solicitantes_facturas", no existe.')

    # Función para guardar solicitante de facturas en base de datos.

    def guardar(self) -> None:
        conexion = ConexionDB()

        sql = f"""INSERT INTO solicitantes_facturas(cod_solicitante, nombre_solicitante, cod_planilla)
        VALUES({self.cod_solicitante}, '{self.nombre_solicitante}', {self.cod_planilla})"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except Exception as e:
            print(
                f'Error al intentar guardar solicitante de facturas:\n{e}.\nSolicitante no guardado.')

    # Función para listar todos los solicitantes de facturas de la base de datos.

    def listar(self) -> list:
        conexion = ConexionDB()

        lista_solicitantes_facturas = []
        sql = 'SELECT * FROM solicitantes_facturas'

        try:
            conexion.cursor.execute(sql)
            lista_solicitantes_facturas = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            print('Debe crear tabla "solicitantes_facturas" en base de datos.')

        return lista_solicitantes_facturas

    # Función para editar un solicitante de facturas en la base de datos.

    def editar(self) -> None:
        conexion = ConexionDB()

        sql = f"""UPDATE solicitantes_facturas
        SET nombre_solicitante = '{self.nombre_solicitante}',
        cod_planilla = {self.cod_planilla}
        WHERE cod_solicitante = {self.cod_solicitante}"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar editar solicitante de facturas:\n{e}.\nSolicitante no editado.')

    # Función para eliminar un solicitante de facturas de la base de datos.

    def eliminar(self) -> None:
        conexion = ConexionDB()

        sql = f"DELETE FROM solicitantes_facturas WHERE cod_solicitante = '{self.cod_solicitante}'"

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar eliminar solicitante de facturas:\n{e}.\nSolicitante no eliminado.')

    def importar_csv(self) -> None:
        i = 0
        # Intenta leer el archivo CSV con diferentes encodings
        encodings = ['utf-8', 'ISO-8859-1', 'latin1']
        for encoding in encodings:
            try:
                df = pd.read_csv('solicitantes_facturas.csv', encoding=encoding)
                # Si tiene éxito, rompe el bucle
                break
            except UnicodeDecodeError:
                print(f'Error al leer con encoding {encoding}. Intentando con otro.')

        df.columns = ['cod_solicitante', 'nombre_solicitante', 'cod_planilla']

        lista_solicitantes = df.to_dict(orient='records')
        for solicitante in lista_solicitantes:
            try:
                SolicitanteFacturas(solicitante['cod_solicitante'], solicitante['nombre_solicitante'], solicitante['cod_planilla']).guardar()
            except Exception as e:
                i += 1
                continue

        print('Solicitantes importados.')
        print(f'Solicitnates ya existentes {i}.')
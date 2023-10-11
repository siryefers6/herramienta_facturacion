import pandas as pd
from .conexion_db import ConexionDB


# Clase CcEspecial que representa un Centro de costo especial.


class CcEspecial:
    def __init__(self, cod_ccosto: int, desc_ccosto: str) -> None:
        self.cod_ccosto = cod_ccosto
        self.desc_ccosto = desc_ccosto.strip().upper()

    def __str__(self) -> str:
        return f'CcEspecial[{self.cod_ccosto}, {self.desc_ccosto}]'

    # Función para crear la tabla 'cc_especiales' en la base de datos.

    def crear_tabla(self) -> None:
        conexion = ConexionDB()

        sql = """CREATE TABLE cc_especiales(
        cod_ccosto INTEGER,
        desc_ccosto VARCHAR(100),
        PRIMARY KEY(cod_ccosto)
        )"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "cc_especiales", Creada.')

        except:
            print('Tabla "cc_especiales", ya existe.')

    # Función para borrar la tabla 'cc_especiales' de la base de datos.

    def borrar_tabla(self) -> None:
        conexion = ConexionDB()

        sql = 'DROP TABLE cc_especiales'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "cc_especiales", eliminada.')

        except:
            print('Tabla "cc_especiales", no existe.')

    # Función para guardar cc_especial en base de datos.

    def guardar(self) -> None:
        conexion = ConexionDB()

        sql = f"""INSERT INTO cc_especiales(cod_ccosto, desc_ccosto)
        VALUES({self.cod_ccosto}, '{self.desc_ccosto}')"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except Exception as e:
            print(
                f'Error al intentar guardar cc_especial:\n{e}.\nCc_especial no guardado.')

    # Función para listar todos los cc_especiales de la base de datos.

    def listar(self) -> list:
        conexion = ConexionDB()

        lista_cc_especiales = []
        sql = 'SELECT * FROM cc_especiales'

        try:
            conexion.cursor.execute(sql)
            lista_cc_especiales = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            print('Debe crear tabla "cc_especiales" en base de datos.')

        return lista_cc_especiales

    # Función para editar un cc_especial en la base de datos.

    def editar(self) -> None:
        conexion = ConexionDB()

        sql = f"""UPDATE cc_especiales
        SET desc_ccosto = '{self.desc_ccosto}'
        WHERE cod_ccosto = {self.cod_ccosto}"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar editar cc_especial:\n{e}.\nCc_especial no editado.')

    # Función para eliminar un cc_especial de la base de datos.

    def eliminar(self) -> None:
        conexion = ConexionDB()

        sql = f"DELETE FROM cc_especiales WHERE cod_ccosto = {self.cod_ccosto}"

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar eliminar cc_especial:\n{e}.\nCc_especial no eliminado.')

    def importar_csv(self) -> None:
        i = 0
        # Intenta leer el archivo CSV con diferentes encodings
        encodings = ['utf-8', 'ISO-8859-1', 'latin1']
        for encoding in encodings:
            try:
                df = pd.read_csv('cc_especiales.csv', encoding=encoding, header=None)
                # Si tiene éxito, rompe el bucle
                break
            except UnicodeDecodeError:
                print(f'Error al leer con encoding {encoding}. Intentando con otro.')

        df.columns = ['cod_ccosto', 'desc_ccosto']

        lista_ccostos = df.to_dict(orient='records')
        for ccosto in lista_ccostos:
            try:
                CcEspecial(ccosto['cod_ccosto'], ccosto['desc_ccosto']).guardar()
            except Exception as e:
                i += 1
                continue

        print('Ccostos_especiales importados.')
        print(f'Ccostos_especiales  ya existentes {i}.')

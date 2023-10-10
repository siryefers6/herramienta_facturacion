from .conexion_db import ConexionDB
import pandas as pd

# Clase item que representa un item.


class Item:
    def __init__(self, cod_item: str, desc_item: str, cod_codelco: int) -> None:
        self.cod_item = cod_item.strip().upper()
        self.desc_item = desc_item.strip().upper()
        self.cod_codelco = cod_codelco

    def __str__(self) -> str:
        return f'Item[{self.cod_item}, {self.desc_item}, {self.cod_codelco}]'

    # Función para crear la tabla 'items' en la base de datos.

    def crear_tabla(self) -> None:
        conexion = ConexionDB()

        sql = """CREATE TABLE items(
        cod_item VARCHAR(100),
        desc_item VARCHAR(100),
        cod_codelco INTEGER,
        PRIMARY KEY(cod_item)
        )"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "items", Creada.')

        except:
            print('Tabla "items", ya existe.')

    # Función para borrar la tabla 'items' de la base de datos.

    def borrar_tabla(self) -> None:
        conexion = ConexionDB()

        sql = 'DROP TABLE items'

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            print('Tabla "items", eliminada.')

        except:
            print('Tabla "items", no existe.')

    # Función para guardar item en base de datos.

    def guardar(self) -> None:
        conexion = ConexionDB()

        sql = f"""INSERT INTO items(cod_item, desc_item, cod_codelco)
        VALUES('{self.cod_item}', '{self.desc_item}', {self.cod_codelco})"""
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
        except Exception as e:
            print(
                f'Error al intentar guardar item:\n{e}.\nItem no guardado.')

    # Función para listar todos los items de la base de datos.

    def listar(self) -> list:
        conexion = ConexionDB()

        lista_items = []
        sql = 'SELECT * FROM items'

        try:
            conexion.cursor.execute(sql)
            lista_items = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            print('Debe crear tabla "items" en base de datos.')

        return lista_items

    # Función para editar un item en la base de datos.

    def editar(self) -> None:
        conexion = ConexionDB()

        sql = f"""UPDATE items
        SET desc_item = '{self.desc_item}',
        cod_codelco = {self.cod_codelco}
        WHERE cod_item = '{self.cod_item}'"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar editar item:\n{e}.\nItem no editado.')

    # Función para eliminar un item de la base de datos.

    def eliminar(self) -> None:
        conexion = ConexionDB()

        sql = f"DELETE FROM items WHERE cod_item = '{self.cod_item}'"

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()

        except Exception as e:
            print(
                f'Error al intentar eliminar item:\n{e}.\nItem no eliminado.')

    def importar_csv(self) -> None:
        i = 0
        # Intenta leer el archivo CSV con diferentes encodings
        encodings = ['utf-8', 'ISO-8859-1', 'latin1']
        for encoding in encodings:
            try:
                df = pd.read_csv('items.csv', encoding=encoding)
                # Si tiene éxito, rompe el bucle
                break
            except UnicodeDecodeError:
                print(f'Error al leer con encoding {encoding}. Intentando con otro.')

        df.columns = ['cod_item', 'desc_item', 'cod_codelco']

        lista_items = df.to_dict(orient='records')
        for item in lista_items:
            try:
                Item(item['cod_item'], item['desc_item'], item['cod_codelco']).guardar()
            except Exception as e:
                i += 1
                continue

        print('Items importados.')
        print(f'Items ya existentes {i}.')
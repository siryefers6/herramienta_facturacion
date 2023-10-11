import sqlite3


class ConexionDB:

    def __init__(self) -> None:
        # Define el nombre y la ubicación de la base de datos.
        self.base_datos = 'database/company.db'

        # Establece una conexión a la base de datos.
        self.conexion = sqlite3.connect(self.base_datos)

        # Crea un objeto cursor para interactuar con la base de datos.
        self.cursor = self.conexion.cursor()

    def cerrar(self) -> None:
        # Guarda los cambios en la base de datos y cierra la conexión.
        self.conexion.commit()
        self.conexion.close()
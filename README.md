# Herramienta Facturación

Esta aplicación automatiza algunos procesos realizados en el área de Facturación.

## Estructura de archivos:
```
herramienta_facturacion/
|-- herramienta_facturacion.py
|
|-- client/
|   |-- __init__.py
|   |-- gui_app.py
|
|-- model/
|   |-- __init__.py
|   |-- conexion_db.py
|   |-- cliente.py
|   |-- item.py
|   |-- cc_especial.py
|   |-- solicitante_facturas.py
|
|-- database/
|   |-- company.db
|
|-- README.md
|-- .gitignore
|-- requirements.txt
|-- venv/
```

---

## Pasos realizados en proceso de desarrollo:

- Crear carpeta del proyecto llamada `herramienta_facturacion`

- Crear archivo `README.md` y empezar descripción del proyecto.

- Crear entorno virtual Python dentro de carpeta raiz del proyecto.
```terminal
python -m venv venv

```

- Activar entorno virtual.
```terminal
source venv/Scripts/activate

```

- Iniciar git:
```terminal
git init

```

- Crear archivo .gitignore y agregar siguiente código:
```.gitignore
/venv
__pycache__/
*.py[cod]
*$py.class

```

- Crear repositorio remoto en GitHub, necesario para guardar repositorio local.

- Ejecutar primer add:
```
git add .

```

- Ejecutar primer commit:
```
git commit -m 'Primer commit.'

```

- Enlazar repositorio remoto con repositorio local, realizando primer push.
```
git remote add origin git@github.com:siryefers6/herramienta_facturacion.git
git branch -M main
git push -u origin main

```

- Crear estructura de archivos y carpetas por consola:
```
mkdir client model database
touch client/__init__.py client/gui_app.py
touch model/__init__.py model/conexion_db.py model/cliente.py
touch model/item.py model/cc_especial.py model/solicitante_facturas.py
touch herramienta_facturacion.py

```

- Pushear antes de crear primera rama.

- Crear y cambiar a rama `conexion_db.py`, para construir conexión a base de datos.


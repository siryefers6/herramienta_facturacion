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

- Archivo `conexion_db.py` terminado, mergear con rama main, pushear y eliminar rama `conexion_db.py`:

```
git add .
git commit -m 'Archivo `conexion_db.py`, terminado y probado.'
git checkout main
git merge conexion_db.py
git push origin main
git branch -d conexion_db.py
```

- Crear y cambiar a rama `cliente.py`, para construir modelo cliente e interacción con la base de datos.

- Archivo `cliente.py` terminado, mergear con rama main, pushear y eliminar rama `cliente.py`:

```
git add .
git commit -m 'Archivo `cliente.py`, terminado y probado.'
git checkout main
git merge cliente.py
git push origin main
git branch -d cliente.py
```

- Crear y cambiar a rama `item.py`, para construir modelo item e interacción con la base de datos.

- Archivo `item.py` terminado, mergear con rama main, pushear y eliminar rama `item.py`:

```
git add .
git commit -m 'Archivo `item.py`, terminado y testeado.'
git checkout main
git merge item.py
git push origin main
git branch -d item.py
```

**Nota importante: Tener muy presente en consultas SQL encerrar variables str en '' e integers no encerrar en comillas. De lo contrario dará error.**

- Crear y cambiar a rama `solicitante_facturas.py`, para construir modelo solicitante facturas e interacción con la base de datos.

- Archivo `solicitante_facturas.py` terminado, mergear con rama main, pushear y eliminar rama `solicitante_facturas.py`:

```
git add .
git commit -m 'Archivo `solicitante_facturas.py`, terminado y testeado.'
git checkout main
git merge solicitante_facturas.py
git push origin main
git branch -d solicitante_facturas.py
```

- Crear y cambiar a rama `cc_especial.py`, para construir modelo CcEspecial e interacción con la base de datos.

- Archivo `cc_especial.py` terminado, mergear con rama main, pushear y eliminar rama `cc_especial.py`:

```
git add .
git commit -m 'Archivo `cc_especial.py`, terminado y testeado.'
git checkout main
git merge cc_especial.py
git push origin main
git branch -d cc_especial.py
```

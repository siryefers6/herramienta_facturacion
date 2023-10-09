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
|-- vev/
```
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

- Enlazar repositorio remoto con repositorio local.
```


```
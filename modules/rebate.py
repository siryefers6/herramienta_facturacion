from model.cc_especial import CcEspecial
from model.cliente import Cliente
from model.item import Item
from model.solicitante_facturas import SolicitanteFacturas

def limpiar_archivo_txt() -> str:
    ruta_al_archivo = 'archivo.txt'
    with open(ruta_al_archivo, 'r', encoding='ascii', errors='ignore') as archivo:
        contenido = archivo.read()

    contenido = contenido.replace(',', '').replace('.', '').replace('  ', ' ').replace('  ', ' ').upper()

    return contenido

def lineas_archivo_txt() -> list:

    contenido = limpiar_archivo_txt()
    lineas = contenido.split('\n')
    lineas_contenido = []
    for line in lineas:
        line = line.strip()
        if '$' in line:
            line = line.replace('-', '')
        if line != '':
            lineas_contenido.append(line)

    return lineas_contenido
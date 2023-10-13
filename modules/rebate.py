import pandas as pd
import os
import re
from model.cc_especial import CcEspecial
from model.cliente import Cliente
from model.item import Item
from model.solicitante_facturas import SolicitanteFacturas


def limpiar_archivo_txt() -> str:
    ruta_al_archivo = 'archivo.txt'
    with open(ruta_al_archivo, 'r', encoding='ascii', errors='ignore') as archivo:
        contenido = archivo.read()

    contenido = contenido.replace(',', '').replace(
        '.', '').replace('\t', ' ').replace('  ', ' ').replace('  ', ' ').upper()

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


def quitar_puntos_y_comas(line):
    line = line.lower()
    line = line.replace(',', '').replace('.', '').replace('\t', ' ')
    return line


def detectar_rut(line):
    str_contain = ['RUT', '-K', '92986000', '86132100', '94282000', '76165935']
    rut_contain = re.findall(r"\d{7,8}-", line)
    if any(str in line for str in str_contain) or rut_contain:
        patron_rut = r"\d{7,8}"
        line = re.findall(patron_rut, line)
        if line:
            line = line[0]
        else:
            line = ''
    else:
        line = ''
    return line


def detectar_monto(line):
    str_contain = ['$', 'iva', 'pesos']
    # monto_contain = re.findall(r"\d{2,9}", line)
    if any(str in line for str in str_contain):
        patron_monto = r"\d{2,9}"
        line = re.findall(patron_monto, line)
        line = line[0]
    else:
        line = ''
    return line


def detectar_ccosto(line):
    str_contain = ['cc', 'centro de costo', 'c costo', 'c  costo']
    ccosco_contain = re.findall(r"950\d", line)
    if any(str in line for str in str_contain) or ccosco_contain:
        patron_ccosto = r"950\d"
        line = re.findall(patron_ccosto, line)
        if line:
            line = line[0]
        else:
            line = ''
    else:
        line = ''
    return line


def eliminar_coincidencia_string(row):
    if len(row) == 2:
        columna1 = row[0]
        columna2 = row['Rut']
        columna3 = ''
        columna4 = ''
        columna5 = ''
    elif len(row) == 3:
        columna1 = row[0]
        columna2 = row['Rut']
        columna3 = row['Ccosto']
        columna4 = ''
        columna5 = ''
    elif len(row) == 4:
        columna1 = row[0]
        columna2 = row['Rut']
        columna3 = row['Ccosto']
        columna4 = row['Vendedor']
        columna5 = ''
    elif len(row) == 5:
        columna1 = row[0]
        columna2 = row['Rut']
        columna3 = row['Ccosto']
        columna4 = row['Vendedor']
        columna5 = row['Monto']
    if (columna1 and columna2) and (columna2 in columna1):
        columna1 = columna1.replace(columna2, '')
    if columna3 and (columna3 in columna1):
        columna1 = columna1.replace(columna3, '')
    if columna4 and (columna4 in columna1):
        columna1 = columna1.replace(columna4, '')
    if columna5 and (columna5 in columna1):
        columna1 = columna1.replace(columna5, '')
    return columna1

def detectar_vendedor(line):
    str_contain = ['comprador', 'vend', 'vendedor', ' 901', ' 902', ' 903',
                   ' 904', ' 905', ' 906', ' 907', ' 908', ' 909', ' 910', ' 911', ' 912', '918']
    if any(str in line for str in str_contain):
        patron_vendedor = r"9[0,1][0-9]"
        line = re.findall(patron_vendedor, line)
        if line:
            line = line[0]
        else:
            line = ''
    else:
        line = ''
    return line


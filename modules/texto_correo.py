import pandas as pd
import os
import re
from model.cc_especial import CcEspecial
from model.cliente import Cliente
from model.item import Item
from model.solicitante_facturas import SolicitanteFacturas


class TextoCorreo:
    def __init__(self, ruta_archivo) -> None:
        self.ruta_archivo = ruta_archivo
        
    def limpiar_archivo_txt(self) -> str:
        with open(self.ruta_archivo, 'r', encoding='ascii', errors='ignore') as archivo:
            contenido = archivo.read()
        contenido = contenido.replace(',', '').replace('.', '').replace('\t', ' ').replace('$', ' ').replace('  ', ' ').replace('  ', ' ').upper()
        return contenido

    def lineas_archivo_txt(self) -> list:
        contenido = self.limpiar_archivo_txt()
        lineas = contenido.split('\n')
        return lineas
    
    def extraer_ruts(self) -> list:
        lineas = self.lineas_archivo_txt()
        patron_rut = r"\d{7,8}-"
        ruts_encontrados = []
        ruts_limpios = []
        for linea in lineas:
            ruts = re.findall(patron_rut, linea)
            ruts_encontrados += ruts
        for rut in ruts_encontrados:
            ruts_limpios.append(rut.replace('-', ''))
        return ruts_limpios
    
    def extraer_glosa(self) -> list:
        lineas = self.lineas_archivo_txt()
        for line in lineas:
            pass
    

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
        with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
        texto = texto.replace('.-', ' ').replace('  -', '0').replace(',', '').replace('.', '').replace('\t', ' ').replace('  ', ' ').replace('  ', ' ').upper()
        return texto

    def lineas_archivo_txt(self) -> list:
        texto = self.limpiar_archivo_txt()
        lineas = texto.split('\n')
        return lineas
    
    def eliminar_cadenas_de_texto(self, cadenas: list, texto: str) -> str:
        for cadena in cadenas:
            texto = texto.replace(cadena, '')
        return texto

    def extraer_ruts(self) -> list:
        texto = self.limpiar_archivo_txt()
        patron_rut = r"\d{7,8}(?=-)"
        ruts = re.findall(patron_rut, texto)
        return ruts
    
    def extraer_ccostos(self) -> list:
        texto = self.limpiar_archivo_txt()
        patron_cc = r"950[0-4]"
        ccostos = re.findall(patron_cc, texto)
        return ccostos
    
    def extraer_montos(self) -> list:
        texto = self.limpiar_archivo_txt()
        cadenas = self.extraer_ruts() + self.extraer_ccostos()
        texto_limpio = self.eliminar_cadenas_de_texto(cadenas, texto)
        patron_monto = r"\$\s*(\d{1,9})"
        montos = re.findall(patron_monto, texto_limpio)
        return montos
    
    def extraer_vendedores(self) -> str:
        texto = self.limpiar_archivo_txt()
        cadenas = self.extraer_ruts() + self.extraer_ccostos() + self.extraer_montos()
        texto_limpio = self.eliminar_cadenas_de_texto(cadenas, texto)
        patron_vendedor = r"9[0,1][1-6,8-9]"
        vendedores = re.findall(patron_vendedor, texto)
        return vendedores[0]

    def extraer_glosas(self) -> list:
        texto = self.limpiar_archivo_txt()
        cadenas = self.extraer_ruts() + self.extraer_ccostos() + self.extraer_montos()
        texto_limpio = self.eliminar_cadenas_de_texto(cadenas, texto)
        patron_glosa = r"\*(.{1,})\s*"
        glosas = re.findall(patron_glosa, texto_limpio)
        glosas_sin_espacios = []
        for glosa in glosas:
            glosas_sin_espacios.append(glosa.strip())
        glosas = glosas_sin_espacios
        return glosas
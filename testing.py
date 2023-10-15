# testing class Cliente.py #

from model.cliente import Cliente


# cliente1 = Cliente(24405907, 'yeferson bermudez molina')
# cliente2 = Cliente(24219980, 'ruben dario bermudez gallego')
# cliente3 = Cliente(24803784, 'miriam del socorro molina zapata')

# Cliente.crear_tabla(Cliente)
# Cliente.borrar_tabla(Cliente)
# cliente1.guardar()
# cliente2.guardar()
# cliente3.guardar()
# print(Cliente.listar(Cliente))
# cliente2.editar()
# cliente2.eliminar()

# Cliente.importar_csv(Cliente)
# print(Cliente.listar_ruts(Cliente))

# testing class Cliente.py #


from model.item import Item

# item1 = Item('258040az', 'Lapiz pasta azul bic', 900800)
# item2 = Item('258040ng', 'marcador negro bic', 900801)
# item3 = Item('399765', 'corchetera swinlite', 900802)

# Item.crear_tabla(Item)
# Item.borrar_tabla(Item)
# item1.guardar()
# item2.guardar()
# item3.guardar()
# print(Item.listar(Item))
# item2.editar()
# item2.eliminar()

# Item.importar_csv(Item)
# print(Item.listar_cods(Item))

# testing class SolicitanteFacturas #


from model.solicitante_facturas import SolicitanteFacturas

# comp1 = SolicitanteFacturas(908, 'Patricia Silva', 3130)
# comp2 = SolicitanteFacturas(903, 'Carlos yanez yanez', 3133)
# comp3 = SolicitanteFacturas(907, 'emilio pulecio', 3100)

# SolicitanteFacturas.crear_tabla(SolicitanteFacturas)
# SolicitanteFacturas.borrar_tabla(SolicitanteFacturas)
# comp1.guardar()
# comp2.guardar()
# comp3.guardar()
# print(SolicitanteFacturas.listar(SolicitanteFacturas))
# comp2.editar()
# comp2.eliminar()

# SolicitanteFacturas.importar_csv(SolicitanteFacturas)
# print(SolicitanteFacturas.listar_cods_solicitantes(SolicitanteFacturas))
# print(SolicitanteFacturas.listar_cods_planillas(SolicitanteFacturas))


# testing class CcEspecial.py #


from model.cc_especial import CcEspecial

# cc1 = CcEspecial(9501, 'marketing')
# cc2 = CcEspecial(9503, 'Publicidad especiales')
# cc3 = CcEspecial(9500, 'rebate')

# CcEspecial.crear_tabla(CcEspecial)
# CcEspecial.borrar_tabla(CcEspecial)
# cc1.guardar()
# cc2.guardar()
# cc3.guardar()
# print(CcEspecial.listar(CcEspecial))
# cc2.editar()
# cc2.eliminar()

# CcEspecial.importar_csv(CcEspecial)
# print(CcEspecial.listar_ccostos(CcEspecial))

from modules.texto_correo import *


texto_rebate = TextoCorreo('archivo.txt')

# print(texto_rebate.extraer_ruts())
# print(texto_rebate.extraer_ccostos())

# print(texto_rebate.extraer_montos())
# print(texto_rebate.extraer_vendedores())
# print(texto_rebate.extraer_glosas())

## testing extraer texto rebates

ruts = texto_rebate.extraer_ruts()
ccostos = texto_rebate.extraer_ccostos()
glosas = texto_rebate.extraer_glosas()
montos = texto_rebate.extraer_montos()
vendedor = texto_rebate.extraer_vendedores()

print('ruts', len(ruts))
print('ruts', ruts)
print('ccostos', len(ccostos))
print('ccostos', ccostos)
print('glosas', len(glosas))
print('glosas', glosas)
print('montos', len(montos))
print('montos', montos)

nueva_lista_ruts = []
nueva_lista_ccs = []
nueva_lista_glosas = []
if len(ccostos) == len(glosas) and (len(ruts) != len(montos) or len(ruts) != len(ccostos)):
    for rut in ruts:
        rut_multiplicado = (f'-{rut}' * len(ccostos))[1:].split('-')
        nueva_lista_ruts += rut_multiplicado
    ruts = nueva_lista_ruts

    for n in range(0, len(ruts)):
        nueva_lista_ccs += ccostos
        nueva_lista_glosas += glosas
    ccostos = nueva_lista_ccs
    glosas = nueva_lista_glosas

if len(ccostos) != len(montos):
    for n in range(0, len(montos)):
        nueva_lista_ccs += ccostos
    ccostos = nueva_lista_ccs

for i in range(0, len(ruts)):
    if montos[i] == '0':
        continue
    if len(glosas[i]) <= 40:
        print(f'{ruts[i]},{ccostos[i]},{glosas[i]},,{montos[i]},{vendedor}')
    else:
        palabras = glosas[i].split(' ')
        glosa1 = ''
        glosa2 = ''
        for palabra in palabras:
            if glosa2 == '' and len((glosa1 + ' ' + palabra).strip()) <= 40:
                glosa1 = glosa1 + ' ' + palabra
            else:
                glosa2 = glosa2 + ' ' + palabra
        print(f'{ruts[i]},{ccostos[i]},{glosa1.strip()},{glosa2.strip()},{montos[i]},{vendedor}')


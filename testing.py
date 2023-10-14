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

for rut in ruts:
    print(rut)
for cc in ccostos:
    print(cc)
for glosa in glosas:
    print(glosa)
for monto in montos:
    print(monto)
print(vendedor)
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

from modules.rebate import *

# print(limpiar_archivo_txt())
# print(lineas_archivo_txt())

lines = lineas_archivo_txt()
ruts = []

for line in lines:
    line = detectar_rut(line)
    if line:
        ruts.append(line)

print(ruts)

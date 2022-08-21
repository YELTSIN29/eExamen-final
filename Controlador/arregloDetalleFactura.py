from Controlador.detalleVenta import *
from Controlador.arregloClientes import *
#from Controlador.detalleVenta import *
from Controlador.arregloProductos import *

class ArregloDetalleFactura:

    def __init__(self):
        self.dataDetalleFactura = []

    def adicionaDetalleFactura(self, objDetFact):
        self.dataDetalleFactura.append(objDetFact)

    def devolverDetalleFactura(self, pos):
        return self.dataDetalleFactura[pos]
    
    def tamañoDetalleFactura(self):
        return len(self.dataDetalleFactura)

    def buscarDetalleFactura(self, nDocumentoFactura):
        for i in range(self.tamañoDetalleFactura()):
            if nDocumentoFactura == self.dataDetalleFactura[i].getnroCom():
                return i
        return -1

    def eliminarDetalleFactura(self, indice):
        del(self.dataDetalleFactura[indice])
    
    #def imprimirDetalleFactura(self, nDocumentoFact, aPro):
    #    for objDetFact in self.dataDetalleFactura:
    #        if objDetFact.getnroCom() == nDocumentoFact
    #            pos = aPro.buscarProducto(objDetFact.getCodigoProducto())  
    #            objPro = aPro.devolverProducto(pos)
    #            objDetFact.imprimirLineaDetalleFact(objPro)

                

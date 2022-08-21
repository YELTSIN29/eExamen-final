from Controlador.detalleVenta import *
from Controlador.arregloClientes import *
#from Controlador.detalleVenta import *
from Controlador.arregloProductos import *

class ArregloDetalleVenta:

    def __init__(self):
        self.dataDetalleVenta = []
        

    def adicionaDetalleVenta(self, objDetVent):
        self.dataDetalleVenta.append(objDetVent)

    def devolverDetalleVenta(self, pos):
        return self.dataDetalleVenta[pos]
    
    def tamañoDetalleVenta(self):
        return len(self.dataDetalleVenta)

    def buscarDetalleVenta(self, nDocumentoVenta):
        for i in range(self.tamañoDetalleVenta()):
            if nDocumentoVenta == self.dataDetalleVenta[i].getNDocumentoVenta:
                return i
        return -1

    def eliminarDetalleVenta(self, indice):
        del(self.dataDetalleVenta[indice])
    
    def imprimirDetalleVenta(self, nDocumentoVenta, aPro):
        for objDetVent in self.dataDetalleVenta:
            if objDetVent.getNDocumentoVenta() == nDocumentoVenta:
                pos = aPro.buscarProducto(objDetVent.getCodigoProducto())  
                objPro = aPro.devolverProducto(pos)
                objDetVent.imprimirLineaDetalleVenta(objPro)
    


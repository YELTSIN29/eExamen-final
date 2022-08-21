from Controlador.factura import *

class ArregloFactura:
    
    def __init__(self):
        self.dataFactura = []

    def adicionaFactura(self, objFact):
        self.dataFactura.append(objFact)

    def devolverFactura(self, pos):
        return self.dataFactura[pos]
    
    def tamañoFactura(self):
        return len(self.dataFactura)

    def buscarFactura(self, nDocumentoVenta):
        for i in range(self.tamañoFactura()):
            if nDocumentoVenta == self.dataFactura[i].getnroDoc():
                return i
        return -1

    def eliminarFactura(self, indice):
        del(self.dataFactura[indice])
    
    def nroSerie(self):
        self.series = []
        for i in range(self.tamañoFactura()):
            self.series.append(self.dataFactura[i].getnroDoc())
        return len(self.series)

class DetalleFactura():

    __nroCom = "";  __codProducto = ""; __nomProducto = "";  __precioVenta = 0.0
    __cant = 0

    def __init__(self, nroCom, codProducto, nomProducto, precioVenta, cant):
        self.__nroCom = nroCom
        self.__codProducto = codProducto
        self.__nomProducto = nomProducto
        self.__precioVenta = precioVenta
        self.__cant = cant

    def getnroCom(self):
        return self.__nroCom

    def getcodProducto(self):
        return self.__codProducto

    def getnomProducto(self):
        return self.__nomProducto

    def getprecioVenta(self):
        return self.__precioVenta

    def getcant(self):
        return self.__cant

    
    def setnroCom(self, nroCom):
        self.__nroCom = nroCom

    def setcodProducto(self, codProducto):
        self.__codProducto = codProducto

    def setnomProducto(self, nomProducto):
        self.__nomProducto = nomProducto

    def setprecioVenta(self, precioVenta):
        self.__precioVenta = precioVenta

    def setcant(self, cant):
        self.__cant = cant

        

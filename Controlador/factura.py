class Factura():

    __nroDoc = ""; __dniCliente = ""; __dniEmpleado = ""; __fecha = ""


    def __init__(self, nroDoc, dniCliente, dniEmpleado, fecha):
        self.__nroDoc = nroDoc
        self.__dniCliente = dniCliente
        self.__dniEmpleado = dniEmpleado
        self.__fecha = fecha

    def getnroDoc(self):
        return self.__nroDoc

    def getdniCliente(self):
        return self.__dniCliente
    
    def getdniEmpleado(self):
        return self.__dniEmpleado

    def getfecha(self):
        return self.__fecha


    def setnroDoc(self, nroDoc):
        self.__nroDoc = nroDoc

    def setdniCliente(self, dniCliente):
        self.__dniCliente = dniCliente
    
    def setdniEmpleado(self, dniEmpleado):
        self.__dniEmpleado = dniEmpleado

    def setfecha(self, fecha):
        self.__fecha = fecha


    
    

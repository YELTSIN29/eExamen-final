class Proveedores():

    #1. Atributos
    __DniProveedor = ""; __RazSoc = ""; __Telefono = ""
    __Direccion = ""; __Categoria = ""

    #2. Constructor
    def __init__(self, dni, raz, tel, dir, cat):
        self.__DniProveedor = dni
        self.__RazSoc = raz
        self.__Telefono = tel
        self.__Direccion = dir
        self.__Categoria = cat
    
    #3. Metodos de Acceso publico Set - Get

    def getDniProveedor(self):
        return self.__DniProveedor
    def setDniProveedor(self, dni):
        self.__DniProveedor = dni

    def getRazSoc(self):
        return self.__RazSoc
    def setRazSoc(self, raz):
        self.__RazSoc = raz

    def getTelefono(self):
        return self.__Telefono
    def setTelefono(self, tel):
        self.__Telefono = tel
    
    def getDireccion(self):
        return self.__Direccion
    def setDireccion(self, dir):
        self.__Direccion = dir
    
    def getCategoria(self):
        return self.__Categoria
    def setCategoria(self, cat):
        self.__Categoria = cat
    

    









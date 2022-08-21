from Controlador.proveedor import *

class ArregloProveedor:
    
    def __init__(self):
        self.dataProveedor = []
        self.cargar()
        
    def adicionaProveedor(self, objPro):
        self.dataProveedor.append(objPro)

    def devolverProveedor(self, pos):
        return self.dataProveedor[pos]
    
    def tamañoArregloProveedor(self):
        return len(self.dataProveedor)

    def buscarProveedor(self, codigo):
        for i in range(self.tamañoArregloProveedor()):
            if codigo == self.dataProveedor[i].getDniProveedor():
                return i
        return -1

    def eliminarProveedor(self, indice):
        del(self.dataProveedor[indice])
    
    def modificarProveedor(self, objPro, pos):
        self.dataProveedor[pos]=objPro
    
    def retornarDatos(self):
        return self.dataProveedor       
    
    def cargar(self):
        archivo = open("Modelo/Proveedor.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna[0]
            raz = columna[1]
            tel = columna[2]
            dir = columna[3]
            cat = columna[4].strip()
            objPro = Proveedores(dni, raz, tel, dir, cat)
            self.adicionaProveedor(objPro)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Proveedor.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloProveedor()):
            archivo.write(str(self.devolverProveedor(i).getDniProveedor()) + ","
            + str(self.devolverProveedor(i).getRazSoc()) + "," 
            + str(self.devolverProveedor(i).getTelefono()) + ","
            + str(self.devolverProveedor(i).getDireccion()) + ","
            + str(self.devolverProveedor(i).getCategoria()) + "\n")
        archivo.close()
from Controlador.empleados import *

class ArregloEmpleados:
    
    def __init__(self):
        self.dataEmpleados = []
        self.cargar()

    def adicionaEmpleado(self, objEmp):
        self.dataEmpleados.append(objEmp)

    def devolverEmpleado(self, pos):
        return self.dataEmpleados[pos]
    
    def tamañoArregloEmpleado(self):
        return len(self.dataEmpleados)

    def buscarEmpleado(self, dni):
        for i in range(self.tamañoArregloEmpleado()):
            if dni == self.dataEmpleados[i].getDniEmpleado():
                return i
        return -1

    def eliminarEmpleado(self, indice):
        del(self.dataEmpleados[indice])
        
    def modificarEmpleado(self, objEmp, pos):
        self.dataEmpleados[pos]=objEmp
    
    def retornarDatos(self):
        return self.dataEmpleados
    
    def cargar(self):
        archivo = open("Modelo/Empleados.txt", "r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dni = columna[0]
            nombres = columna[1]
            apellido_paterno = columna[2]
            apellido_materno = columna[3]
            direccion = columna[4]
            telefono = columna[5].strip()
            objEmp = Empleado(dni, nombres, apellido_paterno, apellido_materno, direccion, telefono)
            self.adicionaEmpleado(objEmp)
        archivo.close()

    def grabar(self):
        archivo = open("Modelo/Empleados.txt", "w+", encoding = "utf-8")
        for i in range(self.tamañoArregloEmpleado()):
            archivo.write(str(self.devolverEmpleado(i).getDniEmpleado()) + ","
            + str(self.devolverEmpleado(i).getNombresEmpleado()) + "," 
            + str(self.devolverEmpleado(i).getApellidoPaternoEmpleado()) + ","
            + str(self.devolverEmpleado(i).getApellidoMaternoEmpleado()) + ","
            + str(self.devolverEmpleado(i).getDireccionEmpleado()) + ","
            + str(self.devolverEmpleado(i).getTelefonoEmpleado()) + "\n")
        archivo.close()
from PyQt5 import QtWidgets, uic
#from PyQt5 import QtGui
from Controlador.arregloEmpleados import *

aEmp = ArregloEmpleados()

class VentanaEmpleados(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaEmpleados,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaEmpleados.ui", self)
        self.show()
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        #self.Carga_Empleados()

    def Carga_Empleados(self):
        if aEmp.tamañoArregloEmpleado()==0:
            objEmp = Empleado('08693923', 'Jorge','Saldaña','Campos','JR. QUEZADA 221','4585985')
            aEmp.adicionaEmpleado(objEmp)
            objEmp = Empleado('08793924', 'Gustavo','Paez','Salcedo','JR. HUARAZ 162','3722754')
            aEmp.adicionaEmpleado(objEmp)
            objEmp = Empleado('08893925', 'Luis','Campos','Salas','AV. PERU 862','2752854')
            aEmp.adicionaEmpleado(objEmp)
            objEmp = Empleado('08993926', 'Roberto','Marquez','Alcantara','JR. CUZCO 222','5714764')
            aEmp.adicionaEmpleado(objEmp)
            self.listar()
        else:
            self.listar()
    
    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()
    
    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()
    
    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()
    
    def obtenerDireccion(self):
        return self.txtDireccion.text()
    
    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblEmpleados.clearContents()
        self.tblEmpleados.setRowCount(0)

    def valida(self):
        if self.txtDni.text() == "":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"
        elif self.txtNombres.text() == "":
            self.txtNombres.setFocus()
            return "Nombre del cliente...!!!"
        elif self.txtApellidoPaterno.text() == "":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"
        elif self.txtApellidoMaterno.text() == "":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Materno del cliente...!!!"
        elif self.txtDireccion.text() == "":
            self.txtDireccion.setFocus()
            return "Dirección del cliente...!!!"
        elif self.txtTelefono.text() == "":
            self.txtTelefono.setFocus()
            return "Teléfono del cliente...!!!"
        else:
            return ""

    def listar(self):
        self.tblEmpleados.setRowCount(aEmp.tamañoArregloEmpleado())
        self.tblEmpleados.setColumnCount(6)
        #Cabecera
        self.tblEmpleados.verticalHeader().setVisible(False)
        for i in range(0, aEmp.tamañoArregloEmpleado()):
            self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDniEmpleado()))
            self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getNombresEmpleado()))
            self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoPaternoEmpleado()))
            self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoMaternoEmpleado()))
            self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDireccionEmpleado()))
            self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getTelefonoEmpleado()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

    def registrar(self):
        if self.valida() == "":
            objEmp = Empleado(self.obtenerDni(), self.obtenerNombres(), 
                             self.obtenerApellidoPaterno(), 
                             self.obtenerApellidoMaterno(), 
                             self.obtenerDireccion(), self.obtenerTelefono())
            dni = self.obtenerDni()
            if aEmp.buscarEmpleado(dni) == -1:
                aEmp.adicionaEmpleado(objEmp)
                aEmp.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                        "El DNI ingesado ya existe...!!!",
                                                         QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado", 
                                     "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)


    def consultar(self):
        #self.limpiarTabla()
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado", 
                                    "No existen empleados a consultar...!!!",
                                    QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Empleado",
                                                          "Ingrese el DNI a consultar")
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                        "El DNI ingresado no existe...!!! ", 
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aEmp.devolverEmpleado(pos).getDniEmpleado())
                self.txtNombres.setText(aEmp.devolverEmpleado(pos).getNombresEmpleado())
                self.txtApellidoPaterno.setText(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado())
                self.txtApellidoMaterno.setText(aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado())
                self.txtDireccion.setText(aEmp.devolverEmpleado(pos).getDireccionEmpleado())
                self.txtTelefono.setText(aEmp.devolverEmpleado(pos).getTelefonoEmpleado())

                #self.tblClientes.setRowCount(1)
                #self.tblClientes.setItem(0, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDniCliente()))
                #self.tblClientes.setItem(0, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getNombresCliente()))
                #self.tblClientes.setItem(0, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoPaternoCliente()))
                #self.tblClientes.setItem(0, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoMaternoCliente()))
                #self.tblClientes.setItem(0, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDireccionCliente()))
                #self.tblClientes.setItem(0, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getTelefonoCliente()))

    def eliminar(self):
        dni = self.txtDni.text()
        pos = aEmp.buscarEmpleado(dni)
        if pos != -1:
            aEmp.eliminarEmpleado(pos)
            aEmp.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                    "No existen empleados a eliminar...!!!", 
                                                    QtWidgets.QMessageBox.Ok)
        else:
           fila = self.tblEmpleados.selectedItems()
           if fila:
               indiceFila = fila[0].row()
               dni = self.tblEmpleados.item(indiceFila, 0).text()
               pos = aEmp.buscarEmpleado(dni)
               aEmp.eliminarEmpleado(pos)
               aEmp.grabar()
               self.limpiarTabla()
               self.listar()
           else:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                        "Debe seleccionar una fila...!!!", 
                                                        QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado",
                                                    "No existen empleados a modificar...!!!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            dni = self.obtenerDni()
            pos = aEmp.buscarEmpleado(dni)
            if pos != -1:
                objEmp = Empleado(self.obtenerDni(), self.obtenerNombres(), 
                                     self.obtenerApellidoPaterno(), 
                                     self.obtenerApellidoMaterno(), 
                                     self.obtenerDireccion(), self.obtenerTelefono())
                aEmp.modificarEmpleado(objEmp, pos)
                aEmp.grabar()
                self.limpiarControles()
                self.listar()





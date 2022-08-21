from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Controlador.arregloProveedor import *
from Controlador.arregloProveedor import *

aProv = ArregloProveedor()

class VentanaProveedor(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaProveedor,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaProveedores.ui",self)
        self.show()

        self.btnRegProveedor.clicked.connect(self.registrar)
        self.btnConsultarProveedor.clicked.connect(self.consultar)
        self.btnListarProveedor.clicked.connect(self.listar)
        self.btnEliminarProveedor.clicked.connect(self.eliminar)
        self.btnModificarProveedor.clicked.connect(self.modificar)
        self.btnQuitarProveedor.clicked.connect(self.quitar)
        self.listar()
        #self.Carga_Productos()

    def Carga_Productos(self):
        if aProv.tamañoArregloProveedor()==0:
            objPro = ('001', 'Pantalones Jeans','Color Azul desteñido','5', '100','80.00', '95.50','Samza S.A','A')
            aProv.adicionaProveedor(objPro)
            objPro = Proveedores('002', 'Camisas','Uso de verano','5','100','60.00','70.50','Repl S:A','A')
            aProv.adicionaProveedor(objPro)
            objPro = Proveedores('003', 'Corbatas','Uso Elegante','5','100','50.00','65.55','Samza S.A','B')
            aProv.adicionaProveedor(objPro)
            objPro = Proveedores('004', 'Polos','Uso de verano','5','100','45.00','55.55','Cool S.A','C')
            aProv.adicionaProveedor(objPro)
            self.listar()
        else:
            self.listar()


    def obtenerDNIProveedor(self):
        return self.txtDNIproveedor.text()
    
    def obtenerRazonProveedor(self):
        return self.txtRazonProveedor.text()
    
    def obtenerTelefonoProveedor(self):
        return self.txtTelefonoProveedor.text()
    
    def obtenerDireccionProveedor(self):
        return self.txtDireccionProveedor.text()
    
    def obtenerCategoriaProveedor(self):
        return self.txtCategoriaProveedor.text()
    
    def limpiarTablaProveedor(self):
        self.tblProveedor.clearContents()
        self.tblProveedor.setRowCount(0)

    def validaProveedor(self):
        if self.txtDNIproveedor.text() == "":
            self.txtDNIproveedor.setFocus()
            return "DNI Proveedor...!!!"
        elif self.txtRazonProveedor.text() == "":
            self.txtRazonProveedor.setFocus()
            return "Razon Social del Proveedor...!!!"
        elif self.txtTelefonoProveedor.text() == "":
            self.txtTelefonoProveedor.setFocus()
            return "Telefono del Proveedor...!!!"
        elif self.txtDireccionProveedor.text() == "":
            self.txtDireccionProveedor.setFocus()
            return "Direccion del Proveedor...!!!"
        elif self.txtCategoriaProveedor.text() == "":
            self.txtCategoriaProveedor.setFocus()
            return "Categoria del Proveedor...!!!"
        else:
            return ""

    def listar(self):
        self.tblProveedor.setRowCount(aProv.tamañoArregloProveedor())
        self.tblProveedor.setColumnCount(5)
        self.tblProveedor.verticalHeader().setVisible(False)
        for i in range(0, aProv.tamañoArregloProveedor()):
            self.tblProveedor.setItem(i, 0, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDniProveedor()))
            self.tblProveedor.setItem(i, 1, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getRazSoc()))
            self.tblProveedor.setItem(i, 2, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getTelefono()))
            self.tblProveedor.setItem(i, 3, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getDireccion()))
            self.tblProveedor.setItem(i, 4, QtWidgets.QTableWidgetItem(aProv.devolverProveedor(i).getCategoria()))

    def limpiarControles(self):
        self.txtDNIproveedor.clear()
        self.txtRazonProveedor.clear()
        self.txtTelefonoProveedor.clear()
        self.txtDireccionProveedor.clear()
        self.txtCategoriaProveedor.clear()

    def registrar(self):
        if self.validaProveedor() == "":
            objPro =Proveedores(self.obtenerDNIProveedor(), self.obtenerRazonProveedor(), self.obtenerTelefonoProveedor(), 
                    self.obtenerDireccionProveedor(),self.obtenerCategoriaProveedor())
            codigo = self.obtenerDNIProveedor()
            if aProv.buscarProveedor(codigo) == -1:
                aProv.adicionaProveedor(objPro)
                aProv.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El código ingresado ya existe...!!!",                                                          QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " +                                                self.validaProveedor(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTablaProveedor()
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                    "No existen productos a consultar...!!!", 
                                                    QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto",
                                                            "Ingrese el código a consultar")
            pos = aProv.buscarProveedor(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                        "El código ingresado no existe...!!! ",
                                                        QtWidgets.QMessageBox.Ok)
            else:
                self.txtDNIproveedor.setText(aProv.devolverProveedor(pos).getDniProveedor())
                self.txtRazonProveedor.setText(aProv.devolverProveedor(pos).getRazSoc())
                self.txtTelefonoProveedor.setText(aProv.devolverProveedor(pos).getTelefono())
                self.txtDireccionProveedor.setText(aProv.devolverProveedor(pos).getDireccion())
                self.txtCategoriaProveedor.setText(aProv.devolverProveedor(pos).getCategoria())

                

    def eliminar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                    "No existen productos a eliminar...!!!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            cod = self.txtDNIproveedor.text()
            pos = aProv.buscarProveedor(cod)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                    "No existe el producto...!!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                aProv.eliminarProveedor(pos)
                aProv.grabar()
                self.limpiarControles()
                self.listar()


    def modificar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                    "No existen Productos a modificar...!!!",                                                    QtWidgets.QMessageBox.Ok)
        else:
            cod = self.txtDNIproveedor.text()
            pos = aProv.buscarProveedor(cod)
            if pos != -1:
                objPro = Proveedores(self.obtenerDNIProveedor(), self.obtenerRazonProveedor(), self.obtenerTelefonoProveedor(), 
                        self.obtenerDireccionProveedor(), self.obtenerCategoriaProveedor())
                aProv.modificarProveedor(objPro, pos)
                aProv.grabar()
                self.limpiarControles()
                self.listar()

    def quitar(self):
        if aProv.tamañoArregloProveedor() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                "No existen Productos a eliminar...!!!", 
                                                QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProveedor.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                cod = self.tblProveedor.item(indiceFila, 0).text()
                pos = aProv.buscarProveedor(cod)
                aProv.eliminarProveedor(pos)
                aProv.grabar()
                self.limpiarTablaProveedor()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                            "Debe seleccionar una fila...!!!", 
                                                            QtWidgets.QMessageBox.Ok)  
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from Controlador.arregloProductos import *

aPro = ArregloProductos()

class VentanaProductos(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaProductos,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaProductos.ui",self)
        self.show()

        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnListar.clicked.connect(self.listar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.listar()
        #self.Carga_Productos()

    def Carga_Productos(self):
        if aPro.tamañoArregloProducto()==0:
            objPro = Producto('001', 'Pantalones Jeans','Color Azul desteñido','5', '100','80.00', '95.50','Samza S.A','A')
            aPro.adicionaProducto(objPro)
            objPro = Producto('002', 'Camisas','Uso de verano','5','100','60.00','70.50','Repl S:A','A')
            aPro.adicionaProducto(objPro)
            objPro = Producto('003', 'Corbatas','Uso Elegante','5','100','50.00','65.55','Samza S.A','B')
            aPro.adicionaProducto(objPro)
            objPro = Producto('004', 'Polos','Uso de verano','5','100','45.00','55.55','Cool S.A','C')
            aPro.adicionaProducto(objPro)
            self.listar()
        else:
            self.listar()


    def obtenerCodigo(self):
        return self.txtCodigo.text()
    
    def obtenerNombre(self):
        return self.txtNombre.text()
    
    def obtenerDescripcion(self):
        return self.txtDescripcion.text()
    
    def obtenerMinimo(self):
        return self.txtStockMinimo.text()
    
    def obtenerActual(self):
        return self.txtStockActual.text()
    
    def obtenerCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecio(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()
    
    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text() == "":
            self.txtCodigo.setFocus()
            return "Código del producto...!!!"
        elif self.txtNombre.text() == "":
            self.txtNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text() == "":
            self.txtDescripcion.setFocus()
            return "Descripción del producto...!!!"
        elif self.txtStockMinimo.text() == "":
            self.txtStockMinimo.setFocus()
            return "Stock mínimo del producto...!!!"
        elif self.txtStockActual.text() == "":
            self.txtStockActual.setFocus()
            return "Stock máximo del producto...!!!"
        elif self.txtPrecioCosto.text() == "":
            self.txtPrecioCosto.setFocus()
            return "Costo del producto...!!!"
        elif self.txtPrecioVenta.text() == "":
            self.txtPrecioVenta.setFocus()
            return "Precio del producto...!!!"
        elif self.cboProveedor.currentText() == "Seleccionar Proveedor":
            self.cboProveedor.setCurrentIndex(0)
            return "Proveedor...!!!"
        elif self.cboAlmacen.currentText() == "Seleccionar Almacén":
            self.cboAlmacen.setCurrentIndex(0)
            return "Almacén...!!!"
        else:
            return ""

    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProducto())
        self.tblProductos.setColumnCount(9)
        self.tblProductos.verticalHeader().setVisible(False)
        for i in range(0, aPro.tamañoArregloProducto()):
            self.tblProductos.setItem(i, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigo()))
            self.tblProductos.setItem(i, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombre()))
            self.tblProductos.setItem(i, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcion()))
            self.tblProductos.setItem(i, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimo()))
            self.tblProductos.setItem(i, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActual()))
            self.tblProductos.setItem(i, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCosto()))
            self.tblProductos.setItem(i, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVenta()))
            self.tblProductos.setItem(i, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedor()))
            self.tblProductos.setItem(i, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacen()))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

    def registrar(self):
        if self.valida() == "":
            objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), 
                     self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), 
                     self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen())
            codigo = self.obtenerCodigo()
            if aPro.buscarProducto(codigo) == -1:
                aPro.adicionaProducto(objPro)
                aPro.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto", "El código ingresado ya existe...!!!",                                                          QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto", "Error en " +                                                self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                    "No existen productos a consultar...!!!", 
                                                    QtWidgets.QMessageBox.Ok)
        else:
            codigo, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto",
                                                             "Ingrese el código a consultar")
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                        "El código ingresado no existe...!!! ",
                                                         QtWidgets.QMessageBox.Ok)
            else:
                self.txtCodigo.setText(aPro.devolverProducto(pos).getCodigo())
                self.txtNombre.setText(aPro.devolverProducto(pos).getNombre())
                self.txtDescripcion.setText(aPro.devolverProducto(pos).getDescripcion())
                self.txtStockMinimo.setText(aPro.devolverProducto(pos).getStockMinimo())
                self.txtStockActual.setText(aPro.devolverProducto(pos).getStockActual())
                self.txtPrecioCosto.setText(aPro.devolverProducto(pos).getPrecioCosto())
                self.txtPrecioVenta.setText(aPro.devolverProducto(pos).getPrecioVenta())
                self.cboProveedor.setCurrentText(aPro.devolverProducto(pos).getProveedor())
                self.cboAlmacen.setCurrentText(aPro.devolverProducto(pos).getAlmacen())

                #self.tblProductos.setRowCount(1)
                #self.tblProductos.setItem(0, 0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigo()))
                #self.tblProductos.setItem(0, 1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombre()))
                #self.tblProductos.setItem(0, 2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcion()))
                #self.tblProductos.setItem(0, 3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimo()))
                #self.tblProductos.setItem(0, 4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActual()))
                #self.tblProductos.setItem(0, 5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCosto()))
                #self.tblProductos.setItem(0, 6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVenta()))
                #self.tblProductos.setItem(0, 7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedor()))
                #self.tblProductos.setItem(0, 8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacen()))


    def eliminar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                    "No existen productos a eliminar...!!!",
                                                    QtWidgets.QMessageBox.Ok)
        else:
            cod = self.txtCodigo.text()
            pos = aPro.buscarProducto(cod)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                    "No existe el producto...!!!",
                                                    QtWidgets.QMessageBox.Ok)
            else:
                aPro.eliminarProducto(pos)
                aPro.grabar()
                self.limpiarControles()
                self.listar()


    def modificar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                                    "No existen Productos a modificar...!!!",                                                    QtWidgets.QMessageBox.Ok)
        else:
            cod = self.txtCodigo.text()
            pos = aPro.buscarProducto(cod)
            if pos != -1:
                objPro = Producto(self.obtenerCodigo(), self.obtenerNombre(), self.obtenerDescripcion(), 
                     self.obtenerMinimo(), self.obtenerActual(), self.obtenerCosto(), 
                     self.obtenerPrecio(), self.obtenerProveedor(), self.obtenerAlmacen())
                aPro.modificarProducto(objPro, pos)
                aPro.grabar()
                self.limpiarControles()
                self.listar()

    def quitar(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                              "No existen Productos a eliminar...!!!", 
                                              QtWidgets.QMessageBox.Ok)
        else:
           fila = self.tblProductos.selectedItems()
           if fila:
               indiceFila = fila[0].row()
               cod = self.tblProductos.item(indiceFila, 0).text()
               pos = aPro.buscarProducto(cod)
               aPro.eliminarProducto(pos)
               aPro.grabar()
               self.limpiarTabla()
               self.listar()
           else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                        "Debe seleccionar una fila...!!!", 
                                                         QtWidgets.QMessageBox.Ok)


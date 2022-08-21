from PyQt5 import QtWidgets, uic
#from PyQt5 import QtGui

from Controlador.arregloClientes import *
from Controlador.arregloEmpleados import *
from Controlador.arregloProductos import *

from Controlador.factura import *
from Controlador.arregloFactura import *
from Controlador.detalleFactura import *
from  Controlador.arregloDetalleFactura import *
from datetime import date

# Carga de Objetos
aCli = ArregloClientes()
aEmp = ArregloEmpleados()
aPro = ArregloProductos()
acFactura = ArregloFactura()
adFactura = ArregloDetalleFactura()
Detalle = []


class VentanaComprobante(QtWidgets.QMainWindow):
    Fila = -1 

    def __init__(self,parent = None):
        super(VentanaComprobante,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaComprobante.ui", self)
        aCli.cargar()
        aEmp.cargar()

        self.show()

        
        self.btnBuscarCliente.clicked.connect(self.buscarCli)
        self.btnBuscarEmpleado.clicked.connect(self.buscarEmp)
        self.btnBuscarProducto.clicked.connect(self.buscarProd)
        self.btnAgregar.clicked.connect(self.agregar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnLimpiar.clicked.connect(self.Limpiar_Controles_Productos)
        self.btnSalir.clicked.connect(self.salir)

        self.Carga_Clientes()
        self.Carga_Empleados()
        self.Carga_Productos()

    def Carga_Clientes(self):
        if aCli.tamañoArregloCliente()==0:
            objCli = Cliente('08693923', 'Alberto','Cordero','Zamorano','Jr. Quezada 221','4585985')
            aCli.adicionaCliente(objCli)
            objCli = Cliente('08793924', 'Juan','Perez','Sanchez','Jr. Cusco 123','3722754')
            aCli.adicionaCliente(objCli)
            objCli = Cliente('08893925', 'Cesar','Céspedes','Ramos','Av. Perú 162','2752854')
            aCli.adicionaCliente(objCli)
            objCli = Cliente('08993926', 'Roberto','Chambi','Rojas','Jr. Cusco 222','5714764')
            aCli.adicionaCliente(objCli)
        else:
            pass

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
        else:
            pass

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
        else:
            pass

    def buscarCli(self):
        aCli.cargar()
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Cliente", 
                                    "No existen clientes a consultar...!!!",
                                    QtWidgets.QMessageBox.Ok)
        else:
            #dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente",
            #                                              "Ingrese el DNI a consultar")
            dni = self.txtDniCli.text()
            pos = aCli.buscarCliente(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente",
                                                        "El DNI ingresado no existe...!!! ", 
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.txtApeNomCli.setText(aCli.devolverCliente(pos).getApellidoPaternoCliente() + " " +
                                          aCli.devolverCliente(pos).getApellidoMaternoCliente() + " " +
                                          aCli.devolverCliente(pos).getNombresCliente())
                self.txtDireccionCli.setText(aCli.devolverCliente(pos).getDireccionCliente())

    def buscarEmp(self):
        aEmp.cargar()
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Empleado", 
                                    "No existen empleados a consultar...!!!",
                                    QtWidgets.QMessageBox.Ok)
        else:
            #dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente",
            #                                              "Ingrese el DNI a consultar")
            dni = self.txtDniEmp.text()
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                        "El DNI ingresado no existe...!!! ", 
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.txtApeNomEmp.setText(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado() + " " +
                                          aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado() + " " +
                                          aEmp.devolverEmpleado(pos).getNombresEmpleado())

    def buscarProd(self):
        if aPro.tamañoArregloProducto() == 0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto", 
                                    "No existen productos a consultar...!!!",
                                    QtWidgets.QMessageBox.Ok)
        else:
            #dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente",
            #                                              "Ingrese el DNI a consultar")
            codigo = self.txtCodProd.text()
            pos = aPro.buscarProducto(codigo)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                        "El Código ingresado no existe...!!! ", 
                                                    QtWidgets.QMessageBox.Ok)
            else:
                self.txtNomProd.setText(aPro.devolverProducto(pos).getNombre())
                self.txtStockMin.setText(aPro.devolverProducto(pos).getStockMinimo())
                self.txtStockActual.setText(aPro.devolverProducto(pos).getStockActual())
                self.txtPrecioVenta.setText(aPro.devolverProducto(pos).getPrecioVenta())
    
    def Limpiar_Controles_Productos(self):
        self.txtCodProd.clear()
        self.txtNomProd.clear()
        self.txtStockMin.clear()
        self.txtStockActual.clear()
        self.txtPrecioVenta.clear()
        self.txtCodProd.setFocus()

    def agregar(self): # _ --> True=Aceptar False=Cancelar
        Cantidad, _ = QtWidgets.QInputDialog.getText(self, "Cantidad Solicitada:","Ingrese Cantidad:")
        if _:
            self.Fila = self.Fila + 1
            Detalle.append([])
            Detalle[self.Fila].append(self.txtNumComprobante.text()) #0
            Detalle[self.Fila].append(self.txtCodProd.text())        #1
            Detalle[self.Fila].append(self.txtNomProd.text())        #2
            Detalle[self.Fila].append(self.txtPrecioVenta.text())    #3
            Detalle[self.Fila].append(Cantidad)                      #4
            Detalle[self.Fila].append(float(self.txtPrecioVenta.text()) * float(Cantidad)) #5
            #print(Detalle)
            self.Limpiar_Controles_Productos()
            self.Imprimir()

    def quitar(self):
        Item, _ = QtWidgets.QInputDialog.getText(self, "Fila",
                                                          "Ingrese Fila a Eliminar")
        if _ :
            Detalle.pop(int(Item)-1)
            self.Fila = self.Fila - 1
            #print(Detalle)
            self.Imprimir()

    def Imprimir(self):
        #Cabecera del Comprobante.
        self.txtComprobante.setText("***********************************************************************")
        self.txtComprobante.append("Comprobante de Pago")
        self.txtComprobante.append("***********************************************************************")
        self.txtComprobante.append("Comprobante:\t:\t" + self.txtNumComprobante.text())
        self.txtComprobante.append("Cliente\t:\t\t" + self.txtApeNomCli.text())
        self.txtComprobante.append("Dirección\t:\t\t" + self.txtDireccionCli.text())
        self.txtComprobante.append("Empleado\t:\t\t" + self.txtApeNomEmp.text())
        self.txtComprobante.append("Fecha\t:\t\t" + str(date.today()))
        self.txtComprobante.append("***********************************************************************")
        #Detalle del Conprobante
        self.txtComprobante.append("Item\tCant x Descripción\tImportes")
        self.txtComprobante.append("***********************************************************************")
        Acumulador = 0
        for i in range(len(Detalle)):
            self.txtComprobante.append(str(i+1) +"\t" + Detalle[i][4] + " x " +  Detalle[i][2])
            self.txtComprobante.append("\tPrecio: " + Detalle[i][3] + "\t\t" +  str(Detalle[i][5]))
            Acumulador = Acumulador + Detalle[i][5]
        
        self.txtComprobante.append("***********************************************************************")
        self.txtComprobante.append("Total\t\t: " + str(Acumulador))
        Igv = Acumulador * 0.18
        Tg = Acumulador + Igv
        self.txtComprobante.append("Igv(18%)\t\t: " + str(Igv))
        self.txtComprobante.append("Total Venta\t\t: " + str(Tg))
        #-- igv
        #-- total a pagar

    def registrar(self):
        #Grabar Cabecera Factura
        objFactura = Factura(self.txtNumComprobante.text(),self.txtDniCli.text(), self.txtDniEmp.text(), str(date.today()))
        nroF = self.txtNumComprobante.text()
        if acFactura.buscarFactura(nroF) == -1:
            acFactura.adicionaFactura(objFactura)
            #aCli.grabar()
            #Grabar Detalle de Factura
            for i in range(len(Detalle)):
                nro = Detalle[i][0] # Numero del Comprobante
                cod = Detalle[i][1] # Codigo del Producto
                nom = Detalle[i][2] # Nombre del Producto
                pre = Detalle[i][3] # Precio de Venta
                can = Detalle[i][4] # Cantidad
                #imp = Detalle[i][5] #Importe
                objDFactura = DetalleFactura(nro, cod, nom, pre, can)
                #Reservado para el archivo
            QtWidgets.QMessageBox.information(self, "Registrar Factura",
                                  "Comprobante Registrado Satisfactoriamente...!!!",
                                   QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Factura",
                                  "El Comprobante ingresado ya existe...!!!",
                                   QtWidgets.QMessageBox.Ok)
        

    def salir(self):
        Fila = -1
        Detalle.clear()
        self.close()


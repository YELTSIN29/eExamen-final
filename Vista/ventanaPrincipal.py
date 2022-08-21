from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui


from Vista.ventanaClientes import *
from Vista.ventanaProductos import *
from Vista.ventanaEmpleados import *
from Vista.ventanaComprobante import *
from Vista.ventanaProveedores import *



class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaPrincipal,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/ventanaPrincipal.ui",self)
        
        '''self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnEmpleados.clicked.connect(self.abrirVentanaEmpleados)
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnComprobante.clicked.connect(self.abrirVentanaComprobante)'''

        # Llamada de opciones de menu
        self.actionClientes.triggered.connect(self.Abrir_Ventana_Cliente)
        self.actionEmpleados.triggered.connect(self.Abrir_Ventana_Empleado)
        self.actionProductos.triggered.connect(self.Abrir_Ventana_Producto) 
        self.actionVista_Previa.triggered.connect(self.Abrir_Ventana_Comprobante)
        self.actionProveedor.triggered.connect(self.Abrir_Ventana_Proveedor)

        #self.btnVender.clicked.connect(self.abrirVentanaVentas)
        #self.btnDetalleVentas.clicked.connect(self.abrirVentanaDetalleVentas)
        #self.btnVentas.clicked.connect(self.abrirVentanaFacturas)
        self.btnSalir.clicked.connect(self.cerrar)


    def Abrir_Ventana_Cliente(self):
        vclientes = VentanaClientes(self)
        vclientes.show()
    
    def Abrir_Ventana_Empleado(self):
        vempleados = VentanaEmpleados(self)
        vempleados.show()

    def Abrir_Ventana_Producto(self):
        vproductos = VentanaProductos(self)
        vproductos.show()

    def Abrir_Ventana_Comprobante(self):
        vComprobante = VentanaComprobante(self)
        vComprobante.show()

    def Abrir_Ventana_Proveedor(self):
        vProveedor = VentanaProveedor(self)
        vProveedor.show()
        
    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()

    def abrirVentanaEmpleados(self):
        vempleados = VentanaEmpleados(self)
        vempleados.show()

    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def abrirVentanaComprobante(self):
        vComprobante = VentanaComprobante(self)
        vComprobante.show()


    def abrirVentanaVentas(self):
        #vVentas = VentanaVentas(self)
        #vVentas.show()
        print()
    
    def abrirVentanaDetalleVentas(self):
        #vDetalleVentas = VentanaDetalleVentas(self)
        #vDetalleVentas.show()
        print()
    
    def abrirVentanaFacturas(self):
        #vFacturas = VentanaFacturas(self)
        #vFacturas.show()
        print()

    def cerrar(self):
        self.close()

from PyQt5 import QtWidgets, uic
#from PyQt5 import QtGui

from Vista.ventanaPrincipal import VentanaPrincipal
#from Controlador.arregloProductos import *
#from Controlador.arregloClientes import *
#from Controlador.arregloDetalleVenta import *
#from Controlador.arregloFactura import *

#qtCreatorFile = "UI/LOGIN.ui" # Nombre del archivo aquí!!!
#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Login(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Login,self).__init__(parent)
        #self.setWindowIcon(QtGui.QIcon("UI/imagenes/venta.png"))
        uic.loadUi("UI/login.ui",self)
        self.show()
        
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        

    # Aquí van las nuevas funciones
    def iniciarSesion(self):
        usuario = self.txtUsuario.text().lower()
        contraseña = self.txtPassword.text()
        if usuario == "kenny" and contraseña == "123456":
            self.close()
            vprincipal = VentanaPrincipal(self)
            vprincipal.show()         
        else:
            mensaje = QtWidgets.QMessageBox()
            mensaje.setWindowTitle("Punto de Venta")
            mensaje.setText("Los datos ingresados son incorrectos...!!!")
            mensaje.setIcon(QtWidgets.QMessageBox.Information)

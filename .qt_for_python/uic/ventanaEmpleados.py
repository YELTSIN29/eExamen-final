# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\yelts\OneDrive\Escritorio\Proyecto_A (2)\Proyecto_A\UI\ventanaEmpleados.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 381)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 23, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 56, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 98, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 57, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.txtDni = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDni.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.txtDni.setObjectName("txtDni")
        self.txtNombres = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombres.setGeometry(QtCore.QRect(20, 130, 113, 20))
        self.txtNombres.setObjectName("txtNombres")
        self.txtApellidoPaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoPaterno.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.txtApellidoPaterno.setObjectName("txtApellidoPaterno")
        self.txtApellidoMaterno = QtWidgets.QLineEdit(self.centralwidget)
        self.txtApellidoMaterno.setGeometry(QtCore.QRect(20, 230, 113, 20))
        self.txtApellidoMaterno.setObjectName("txtApellidoMaterno")
        self.txtDireccion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDireccion.setGeometry(QtCore.QRect(20, 280, 113, 20))
        self.txtDireccion.setObjectName("txtDireccion")
        self.txtTelefono = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTelefono.setGeometry(QtCore.QRect(20, 330, 113, 20))
        self.txtTelefono.setObjectName("txtTelefono")
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(160, 110, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegistrar.setFont(font)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(280, 110, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnConsultar.setFont(font)
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(660, 80, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnListar.setFont(font)
        self.btnListar.setObjectName("btnListar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(400, 110, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(520, 110, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModificar.setFont(font)
        self.btnModificar.setObjectName("btnModificar")
        self.btnQuitar = QtWidgets.QPushButton(self.centralwidget)
        self.btnQuitar.setGeometry(QtCore.QRect(660, 110, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnQuitar.setFont(font)
        self.btnQuitar.setObjectName("btnQuitar")
        self.tblEmpleados = QtWidgets.QTableWidget(self.centralwidget)
        self.tblEmpleados.setGeometry(QtCore.QRect(160, 141, 611, 211))
        self.tblEmpleados.setObjectName("tblEmpleados")
        self.tblEmpleados.setColumnCount(0)
        self.tblEmpleados.setRowCount(0)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 40, 751, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Dni:"))
        self.label_2.setText(_translate("MainWindow", "Nombres:"))
        self.label_3.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.label_4.setText(_translate("MainWindow", "Apellido Materno:"))
        self.label_5.setText(_translate("MainWindow", "Dirección:"))
        self.label_6.setText(_translate("MainWindow", "Teléfono:"))
        self.btnRegistrar.setText(_translate("MainWindow", "Registrar"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))
        self.btnListar.setText(_translate("MainWindow", "Listar"))
        self.btnEliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btnModificar.setText(_translate("MainWindow", "Modificar"))
        self.btnQuitar.setText(_translate("MainWindow", "Quitar"))
        self.label_7.setText(_translate("MainWindow", "Registro de Empleados"))

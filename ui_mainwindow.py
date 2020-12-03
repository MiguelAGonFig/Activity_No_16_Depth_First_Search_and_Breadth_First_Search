# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 600)
        self.actionAbrir_Archivo = QAction(MainWindow)
        self.actionAbrir_Archivo.setObjectName(u"actionAbrir_Archivo")
        self.actionGuardar_Archivo = QAction(MainWindow)
        self.actionGuardar_Archivo.setObjectName(u"actionGuardar_Archivo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Agregar_Inicio_pushButton = QPushButton(self.groupBox)
        self.Agregar_Inicio_pushButton.setObjectName(u"Agregar_Inicio_pushButton")

        self.gridLayout.addWidget(self.Agregar_Inicio_pushButton, 9, 0, 1, 3)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")
        self.ID_spinBox.setMaximum(100000000)

        self.gridLayout.addWidget(self.ID_spinBox, 0, 1, 1, 2)

        self.Green_spinBox = QSpinBox(self.groupBox)
        self.Green_spinBox.setObjectName(u"Green_spinBox")
        self.Green_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Green_spinBox, 7, 2, 1, 1)

        self.Blue_spinBox = QSpinBox(self.groupBox)
        self.Blue_spinBox.setObjectName(u"Blue_spinBox")
        self.Blue_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Blue_spinBox, 8, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.Destino_X_spinBox = QSpinBox(self.groupBox)
        self.Destino_X_spinBox.setObjectName(u"Destino_X_spinBox")
        self.Destino_X_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_X_spinBox, 3, 1, 1, 2)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 8, 1, 1, 1)

        self.Mostrar_pushButton = QPushButton(self.groupBox)
        self.Mostrar_pushButton.setObjectName(u"Mostrar_pushButton")

        self.gridLayout.addWidget(self.Mostrar_pushButton, 11, 0, 1, 3)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.Red_spinBox = QSpinBox(self.groupBox)
        self.Red_spinBox.setObjectName(u"Red_spinBox")
        self.Red_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.Red_spinBox, 6, 2, 1, 1)

        self.Agregar_Final_pushButton = QPushButton(self.groupBox)
        self.Agregar_Final_pushButton.setObjectName(u"Agregar_Final_pushButton")

        self.gridLayout.addWidget(self.Agregar_Final_pushButton, 10, 0, 1, 3)

        self.Destino_Y_spinBox = QSpinBox(self.groupBox)
        self.Destino_Y_spinBox.setObjectName(u"Destino_Y_spinBox")
        self.Destino_Y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Destino_Y_spinBox, 4, 1, 1, 2)

        self.Origen_Y_spinBox = QSpinBox(self.groupBox)
        self.Origen_Y_spinBox.setObjectName(u"Origen_Y_spinBox")
        self.Origen_Y_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_Y_spinBox, 2, 1, 1, 2)

        self.Velocidad_spinBox = QSpinBox(self.groupBox)
        self.Velocidad_spinBox.setObjectName(u"Velocidad_spinBox")
        self.Velocidad_spinBox.setMaximum(100000000)

        self.gridLayout.addWidget(self.Velocidad_spinBox, 5, 1, 1, 2)

        self.Origen_X_spinBox = QSpinBox(self.groupBox)
        self.Origen_X_spinBox.setObjectName(u"Origen_X_spinBox")
        self.Origen_X_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.Origen_X_spinBox, 1, 1, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 2, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_9 = QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_5 = QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.Salida = QPlainTextEdit(self.groupBox_5)
        self.Salida.setObjectName(u"Salida")

        self.gridLayout_8.addWidget(self.Salida, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_6 = QGridLayout(self.groupBox_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Pantalla_Diccionarios = QPlainTextEdit(self.groupBox_4)
        self.Pantalla_Diccionarios.setObjectName(u"Pantalla_Diccionarios")

        self.gridLayout_6.addWidget(self.Pantalla_Diccionarios, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Recorrido_Profundidad_pushButton = QPushButton(self.groupBox_3)
        self.Recorrido_Profundidad_pushButton.setObjectName(u"Recorrido_Profundidad_pushButton")

        self.gridLayout_3.addWidget(self.Recorrido_Profundidad_pushButton, 0, 0, 1, 1)

        self.Pantalla_Recorridos = QPlainTextEdit(self.groupBox_3)
        self.Pantalla_Recorridos.setObjectName(u"Pantalla_Recorridos")

        self.gridLayout_3.addWidget(self.Pantalla_Recorridos, 0, 1, 2, 1)

        self.Recorrido_Amplitud_pushButton = QPushButton(self.groupBox_3)
        self.Recorrido_Amplitud_pushButton.setObjectName(u"Recorrido_Amplitud_pushButton")

        self.gridLayout_3.addWidget(self.Recorrido_Amplitud_pushButton, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.Table = QTableWidget(self.tab_4)
        self.Table.setObjectName(u"Table")

        self.gridLayout_7.addWidget(self.Table, 0, 0, 1, 3)

        self.Buscar_lineEdit = QLineEdit(self.tab_4)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")

        self.gridLayout_7.addWidget(self.Buscar_lineEdit, 1, 0, 1, 1)

        self.Buscar_pushButton = QPushButton(self.tab_4)
        self.Buscar_pushButton.setObjectName(u"Buscar_pushButton")

        self.gridLayout_7.addWidget(self.Buscar_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Limpiar_pushButton = QPushButton(self.tab)
        self.Limpiar_pushButton.setObjectName(u"Limpiar_pushButton")

        self.gridLayout_4.addWidget(self.Limpiar_pushButton, 1, 2, 1, 1)

        self.Dibujar_pushButton = QPushButton(self.tab)
        self.Dibujar_pushButton.setObjectName(u"Dibujar_pushButton")

        self.gridLayout_4.addWidget(self.Dibujar_pushButton, 1, 0, 1, 1)

        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_4.addWidget(self.graphicsView, 0, 0, 1, 3)

        self.Dibujar_Grafo_pushButton = QPushButton(self.tab)
        self.Dibujar_Grafo_pushButton.setObjectName(u"Dibujar_Grafo_pushButton")

        self.gridLayout_4.addWidget(self.Dibujar_Grafo_pushButton, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.Ordenar_ID_pushButton = QPushButton(self.groupBox_2)
        self.Ordenar_ID_pushButton.setObjectName(u"Ordenar_ID_pushButton")

        self.gridLayout_5.addWidget(self.Ordenar_ID_pushButton, 0, 0, 1, 1)

        self.Ordenar_Distancia_pushButton = QPushButton(self.groupBox_2)
        self.Ordenar_Distancia_pushButton.setObjectName(u"Ordenar_Distancia_pushButton")

        self.gridLayout_5.addWidget(self.Ordenar_Distancia_pushButton, 0, 1, 1, 1)

        self.Ordenar_Velocidad_pushButton = QPushButton(self.groupBox_2)
        self.Ordenar_Velocidad_pushButton.setObjectName(u"Ordenar_Velocidad_pushButton")

        self.gridLayout_5.addWidget(self.Ordenar_Velocidad_pushButton, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_Archivo)
        self.menuArchivo.addAction(self.actionGuardar_Archivo)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir_Archivo.setText(QCoreApplication.translate("MainWindow", u"Abrir Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar_Archivo.setText(QCoreApplication.translate("MainWindow", u"Guardar Archivo", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar_Archivo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.Agregar_Inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino en X", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.Mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en Y", None))
        self.Agregar_Final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen en Y", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COLOR - RGB", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en X", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Particulas Registradas", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Contenido del Diccionario", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Recorridos del grafo", None))
        self.Recorrido_Profundidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Profundidad", None))
        self.Recorrido_Amplitud_pushButton.setText(QCoreApplication.translate("MainWindow", u"Recorrido en Amplitud", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Contenido", None))
        self.Buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la Part\u00edcula", None))
        self.Buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.Limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar Pantalla", None))
        self.Dibujar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Part\u00edculas", None))
        self.Dibujar_Grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Grafo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar Elementos", None))
        self.Ordenar_ID_pushButton.setText(QCoreApplication.translate("MainWindow", u"ID - Ascendente", None))
        self.Ordenar_Distancia_pushButton.setText(QCoreApplication.translate("MainWindow", u"Distancia - Descendente", None))
        self.Ordenar_Velocidad_pushButton.setText(QCoreApplication.translate("MainWindow", u"Velocidad - Ascendente", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi


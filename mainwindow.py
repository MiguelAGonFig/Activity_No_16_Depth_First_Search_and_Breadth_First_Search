from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from pprint import pprint, pformat
from PySide2.QtGui import QPen, QColor, QTransform
from ui_mainwindow import Ui_MainWindow
from particula import Particula
from admin_particulas import Admin_particulas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Admin_particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Agregar_Inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.Agregar_Final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.Mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.Ordenar_ID_pushButton.clicked.connect(self.ordenar_ID)
        self.ui.Ordenar_Distancia_pushButton.clicked.connect(self.ordenar_Distancia)
        self.ui.Ordenar_Velocidad_pushButton.clicked.connect(self.ordenar_Velocidad)

        self.ui.Dibujar_Grafo_pushButton.clicked.connect(self.dibujar_Grafo)
        self.ui.Recorrido_Profundidad_pushButton.clicked.connect(self.recorrido_profundidad)
        self.ui.Recorrido_Amplitud_pushButton.clicked.connect(self.recorrido_amplitud)

        self.ui.actionAbrir_Archivo.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar_Archivo.triggered.connect(self.action_guardar_archivo)

        self.ui.Buscar_pushButton.clicked.connect(self.buscar_ID)

        self.ui.Dibujar_pushButton.clicked.connect(self.dibujar_particulas)
        self.ui.Limpiar_pushButton.clicked.connect(self.limpiar_pantalla)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def ordenar_ID(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado partículas existentes'
            )
        else:
            self.particulas.sort(1)
            self.click_mostrar()

    @Slot()
    def ordenar_Distancia(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado partículas existentes'
            )
        else:
            self.particulas.sort(2)
            self.click_mostrar()
            

    @Slot()
    def ordenar_Velocidad(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado partículas existentes'
            )
        else:
            self.particulas.sort(3)
            self.click_mostrar()

    @Slot()
    def dibujar_Grafo(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado particulas existentes'
            )
        else:
            grafo = dict()
            for particula in self.particulas:
                origen = (particula.origen_x, particula.origen_y)
                destino = (particula.destino_x, particula.destino_y)
                peso = particula.distancia
                arista_o_d = (destino, peso)
                arista_d_o = (origen, peso)
                if origen in grafo:
                    grafo[origen].append(arista_o_d)
                else:
                    grafo[origen] = [arista_o_d]
                if destino in grafo:
                    grafo[destino].append(arista_d_o)
                else:
                    grafo[destino] = [arista_d_o]
            
            self.dibujar_particulas()
            str = pformat(grafo, width=80, indent=1)
            self.ui.Pantalla_Diccionarios.clear()
            self.ui.Pantalla_Diccionarios.insertPlainText(str)

    @Slot()
    def recorrido_profundidad(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado particulas existentes'
            )
        else:
            grafo = dict()
            for particula in self.particulas:
                origen = (particula.origen_x, particula.origen_y)
                destino = (particula.destino_x, particula.destino_y)
                peso = particula.distancia
                arista_o_d = (destino, peso)
                arista_d_o = (origen, peso)
                if origen in grafo:
                    grafo[origen].append(arista_o_d)
                else:
                    grafo[origen] = [arista_o_d]
                if destino in grafo:
                    grafo[destino].append(arista_d_o)
                else:
                    grafo[destino] = [arista_d_o]
            
            keys = list(grafo.keys())
            elementos = list(grafo.items())
            visitados = [keys[0]]
            pila = [keys[0]]
            recorrido = []
            while pila:
                recorrido.append(pila[len(pila)-1])
                i = 0
                for key in keys:
                    if key == pila[len(pila)-1]:
                        break
                    i += 1
                pila.pop()
                for elemento in elementos[i][1]:
                    if not elemento[0] in visitados:
                        visitados.append(elemento[0])
                        pila.append(elemento[0])
            
            self.ui.Pantalla_Recorridos.clear()
            self.ui.Pantalla_Recorridos.insertPlainText("\n\n    Recorrido Profundidad       ")
            for vertice in recorrido:
                if vertice != recorrido[len(recorrido)-1]:
                    self.ui.Pantalla_Recorridos.insertPlainText(str(vertice)+",  ")
                else:
                    self.ui.Pantalla_Recorridos.insertPlainText(str(vertice))

            self.mostrar_dict()

    @Slot()
    def recorrido_amplitud(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado particulas existentes'
            )
        else:
            grafo = dict()
            for particula in self.particulas:
                origen = (particula.origen_x, particula.origen_y)
                destino = (particula.destino_x, particula.destino_y)
                peso = particula.distancia
                arista_o_d = (destino, peso)
                arista_d_o = (origen, peso)
                if origen in grafo:
                    grafo[origen].append(arista_o_d)
                else:
                    grafo[origen] = [arista_o_d]
                if destino in grafo:
                    grafo[destino].append(arista_d_o)
                else:
                    grafo[destino] = [arista_d_o]
            
            keys = list(grafo.keys())
            elementos = list(grafo.items())
            visitados = [keys[0]]
            cola = [keys[0]]
            recorrido = []
            while cola:
                recorrido.append(cola[0])
                i = 0
                for key in keys:
                    if key == cola[0]:
                        break
                    i += 1
                cola.pop(0)
                for elemento in elementos[i][1]:
                    if not elemento[0] in visitados:
                        visitados.append(elemento[0])
                        cola.append(elemento[0])
            
            self.ui.Pantalla_Recorridos.clear()
            self.ui.Pantalla_Recorridos.insertPlainText("\n\n    Recorrido Amplitud       ")
            for vertice in recorrido:
                if vertice != recorrido[len(recorrido)-1]:
                    self.ui.Pantalla_Recorridos.insertPlainText(str(vertice)+",  ")
                else:
                    self.ui.Pantalla_Recorridos.insertPlainText(str(vertice))

            self.mostrar_dict()

    @Slot()
    def mostrar_dict(self):
        grafo = dict()
        for particula in self.particulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            peso = particula.distancia
            arista_o_d = (destino, peso)
            arista_d_o = (origen, peso)
            if origen in grafo:
                grafo[origen].append(arista_o_d)
            else:
                grafo[origen] = [arista_o_d]
            if destino in grafo:
                grafo[destino].append(arista_d_o)
            else:
                grafo[destino] = [arista_d_o]
        
        str = pformat(grafo, width=80, indent=1)
        self.ui.Pantalla_Diccionarios.clear()
        self.ui.Pantalla_Diccionarios.insertPlainText(str)

    @Slot()
    def dibujar_particulas(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado particulas existentes'
            )
        else:
            for particula in self.particulas:
                pen = QPen()
                color = QColor(particula.red, particula.green, particula.blue)
                pen.setColor(color)
                pen.setWidth(2)

                self.scene.addEllipse(particula.origen_x, particula.origen_y, 3, 3, pen)
                self.scene.addEllipse(particula.destino_x, particula.destino_y, 3, 3, pen)
                self.scene.addLine(particula.origen_x + 3, particula.origen_y, particula.destino_x + 3, particula.destino_y, pen)          

    @Slot()
    def limpiar_pantalla(self):
        self.scene.clear()

    @Slot()
    def buscar_ID(self):
        id = self.ui.Buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == str(particula.id):
                self.ui.Table.clear()
                self.ui.Table.setRowCount(1)

                ID_widget = QTableWidgetItem(str(particula.id))
                Origen_X_widget = QTableWidgetItem(str(particula.origen_x))
                Origen_Y_widget = QTableWidgetItem(str(particula.origen_y))
                Destino_X_widget = QTableWidgetItem(str(particula.destino_x))
                Destino_Y_widget = QTableWidgetItem(str(particula.destino_y))
                Velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                Red_widget = QTableWidgetItem(str(particula.red))
                Green_widget = QTableWidgetItem(str(particula.green))
                Blue_widget = QTableWidgetItem(str(particula.blue))
                Distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.Table.setItem(0, 0, ID_widget)
                self.ui.Table.setItem(0, 1, Origen_X_widget)
                self.ui.Table.setItem(0, 2, Origen_Y_widget)
                self.ui.Table.setItem(0, 3, Destino_X_widget)
                self.ui.Table.setItem(0, 4, Destino_Y_widget)
                self.ui.Table.setItem(0, 5, Velocidad_widget)
                self.ui.Table.setItem(0, 6, Red_widget)
                self.ui.Table.setItem(0, 7, Green_widget)
                self.ui.Table.setItem(0, 8, Blue_widget)
                self.ui.Table.setItem(0, 9, Distancia_widget)  

                encontrado = True
                return 
        
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con el ID "{id}" no fue encontrada'
            )


    @Slot()
    def mostrar_tabla(self):
        self.ui.Table.setColumnCount(10)
        headers = ["ID", "Origen en X", "Origen en Y", "Destino en X", "Destino en Y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.Table.setHorizontalHeaderLabels(headers)
        self.ui.Table.setRowCount(len(self.particulas))

        row = 0
        for particula in self.particulas:
            ID_widget = QTableWidgetItem(str(particula.id))
            Origen_X_widget = QTableWidgetItem(str(particula.origen_x))
            Origen_Y_widget = QTableWidgetItem(str(particula.origen_y))
            Destino_X_widget = QTableWidgetItem(str(particula.destino_x))
            Destino_Y_widget = QTableWidgetItem(str(particula.destino_y))
            Velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            Red_widget = QTableWidgetItem(str(particula.red))
            Green_widget = QTableWidgetItem(str(particula.green))
            Blue_widget = QTableWidgetItem(str(particula.blue))
            Distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.Table.setItem(row, 0, ID_widget)
            self.ui.Table.setItem(row, 1, Origen_X_widget)
            self.ui.Table.setItem(row, 2, Origen_Y_widget)
            self.ui.Table.setItem(row, 3, Destino_X_widget)
            self.ui.Table.setItem(row, 4, Destino_Y_widget)
            self.ui.Table.setItem(row, 5, Velocidad_widget)
            self.ui.Table.setItem(row, 6, Red_widget)
            self.ui.Table.setItem(row, 7, Green_widget)
            self.ui.Table.setItem(row, 8, Blue_widget)
            self.ui.Table.setItem(row, 9, Distancia_widget)

            row +=1

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self, 
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Apertura exitosa del archivo en " + ubicacion
            )
        else:
            QMessageBox.critical(
                self, 
                "Error",
                "Fallo al intentar abir el archivo en " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Archivo creado correctamente en " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo en " + ubicacion
            )

    @Slot()
    def click_agregar_inicio(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_inicio(particula)

    @Slot()
    def click_agregar_final(self):
        Id = self.ui.ID_spinBox.value()
        Origen_X = self.ui.Origen_X_spinBox.value()
        Origen_Y = self.ui.Origen_Y_spinBox.value()
        Destino_X = self.ui.Destino_X_spinBox.value()
        Destino_Y = self.ui.Destino_Y_spinBox.value()
        Velocidad = self.ui.Velocidad_spinBox.value()
        Red = self.ui.Red_spinBox.value()
        Green = self.ui.Green_spinBox.value()
        Blue = self.ui.Blue_spinBox.value()

        particula = Particula(Id, Origen_X, Origen_Y, Destino_X, Destino_Y, Velocidad, Red, Green, Blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_mostrar(self):
        if len(self.particulas) == 0:
            QMessageBox.warning(
                self,
                "Atención",
                'No se han detectado partículas existentes'
            )
        else:
            self.ui.Salida.clear()
            self.ui.Salida.insertPlainText(str(self.particulas))
            self.mostrar_tabla()
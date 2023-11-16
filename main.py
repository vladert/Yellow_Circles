import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from random import randint


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.diameter = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.yellow)
        painter.drawEllipse(self.rect().center(), self.diameter, self.diameter)

    def setDiameter(self, diameter):
        self.diameter = diameter
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Генерация рандомного жёлтого круга')
        self.setGeometry(100, 100, 400, 400)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.circleWidget = CircleWidget()
        self.layout.addWidget(self.circleWidget)

        self.button = QPushButton('Create Circle')
        self.button.clicked.connect(self.createCircle)
        self.layout.addWidget(self.button)

    def createCircle(self):
        diameter = randint(10, 100)
        self.circleWidget.setDiameter(diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from random import randint

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.yellow)
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

    def setCircles(self, circles):
        self.circles = circles
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Генерация рандомного круга')
        self.setGeometry(100, 100, 400, 400)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.circleWidget = CircleWidget()
        self.layout.addWidget(self.circleWidget)

        self.button = QPushButton('Create Circles')
        self.button.clicked.connect(self.createCircles)
        self.layout.addWidget(self.button)

    def createCircles(self):
        circles = []
        for _ in range(randint(1, 10)):
            diameter = randint(10, 100)
            x = randint(0, self.width() - diameter)
            y = randint(0, self.height() - diameter)
            circles.append((x, y, diameter))
        self.circleWidget.setCircles(circles)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
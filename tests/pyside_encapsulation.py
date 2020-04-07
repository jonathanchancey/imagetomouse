import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("this is a label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("GO")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        print("clicked")
        self.label.setText("you pressed GO")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QSlider, QLineEdit
# from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize 
import sys

## EXAMPLES
# https://doc.qt.io/qtforpython/PySide2/QtCore/Qt.html


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(484, 180))
        self.setWindowTitle("Matriks Printer")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)

        b1 = QtWidgets.QPushButton(self)
        b1.setText("click")
        gridLayout.addWidget(b1,1,0)

        b2 = QtWidgets.QPushButton(self)
        b2.setText("click")
        gridLayout.addWidget(b2,1,1)


        # self.s1 = QSlider(Qt.Horizontal)
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        slider.setRange(0,255)
        slider.setValue(200)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.valueChanged.connect(self.changedValue)
        # slider.setAlignment()
        gridLayout.addWidget(slider,2,0)


        valueOfSlider = slider.tickPosition()
        print(type(valueOfSlider))
        print(valueOfSlider)
        filterCutOffLabel = QLabel("Hello World from PyQt", self)
        filterCutOffLabel.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(filterCutOffLabel, 2, 1)
        # filterCutOffLabel.ItemIsEditable(true)


    def changedValue(self):
        size = str(self.slider.value())
        self.lineEdit.setText(size)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Window()
    mainWin.show()
    sys.exit(app.exec_())
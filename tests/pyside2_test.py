import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle("Mouse Matrix Printer")
        self.setMinimumSize(QtCore.QSize(484, 180))
        central_widget = QtWidgets.QWidget(self) # create the central widget

        # self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
        #               "Hola Mundo", "Привет мир"]
        # set central widget to grid_layout
        grid_layout = QtWidgets.QGridLayout(self)
        central_widget.setLayout(grid_layout)

        # add title
        title = QtWidgets.QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(title, 0, 0)

        # add buttons
        b1 = QtWidgets.QPushButton(self)
        b1.setText("click 0")
        grid_layout.addWidget(b1, 1, 0)

        b2 = QtWidgets.QPushButton(self)
        b2.setText("click 1")
        grid_layout.addWidget(b2, 1, 1)

        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        slider.setRange(0,255)
        slider.setValue(200)
        slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        slider.valueChanged.connect(self.changed_value)
        grid_layout.addWidget(slider, 2, 0)

        value_of_slider = slider.tickPosition()
        print(type(value_of_slider))
        print(value_of_slider)
        filterCutOffLabel = QtWidgets.QLabel("Hello World from PyQt", self)
        filterCutOffLabel.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(filterCutOffLabel, 2, 1)
        # filterCutOffLabel.ItemIsEditable(true)

    def changed_value(self):
        print("in changedValue")
        # size = str(self.slider.value())
        # self.lineEdit.setText(size)

        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World")
        # self.text.setAlignment(QtCore.Qt.AlignCenter)
        #
        # self.layout = QtWidgets.QVBoxLayout()
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
        # self.setLayout(self.layout)
        #
        # self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


def main():
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

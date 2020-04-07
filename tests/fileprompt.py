
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QObject

class Ui_MainWindow( QObject ):
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect( self.browseSlot)
        self.pushButton_2.clicked.connect( self.writeDocSlot)
        self.lineEdit.returnPressed.connect( self.returnPressedSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "My Python Application"))
        self.label_2.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Write Doc"))


    @pyqtSlot( )
    def returnPressedSlot( self ):
        pass

    @pyqtSlot( )
    def writeDocSlot( self ):
        pass

    @pyqtSlot( )
    def browseSlot( self ):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(714, 458)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 661, 361))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 641, 335))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_input = QLabel(self.widget)
        self.label_input.setObjectName(u"label_input")
        self.label_input.setMinimumSize(QSize(40, 0))

        self.horizontalLayout.addWidget(self.label_input)

        self.lineEdit_input = QLineEdit(self.widget)
        self.lineEdit_input.setObjectName(u"lineEdit_input")

        self.horizontalLayout.addWidget(self.lineEdit_input)

        self.pushButton_input = QPushButton(self.widget)
        self.pushButton_input.setObjectName(u"pushButton_input")
        self.pushButton_input.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_input)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_input_3 = QLabel(self.widget)
        self.label_input_3.setObjectName(u"label_input_3")
        self.label_input_3.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_4.addWidget(self.label_input_3)

        self.lineEdit_input_2 = QLineEdit(self.widget)
        self.lineEdit_input_2.setObjectName(u"lineEdit_input_2")

        self.horizontalLayout_4.addWidget(self.lineEdit_input_2)

        self.pushButton_input_2 = QPushButton(self.widget)
        self.pushButton_input_2.setObjectName(u"pushButton_input_2")
        self.pushButton_input_2.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_input_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton_go = QPushButton(self.widget)
        self.pushButton_go.setObjectName(u"pushButton_go")

        self.horizontalLayout_3.addWidget(self.pushButton_go)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label_image0 = QLabel(self.widget)
        self.label_image0.setObjectName(u"label_image0")
        self.label_image0.setMinimumSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.label_image0)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 714, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_input.clicked.connect(MainWindow.browseSlot)
        self.pushButton_go.clicked.connect(MainWindow.displaySlot)
        self.lineEdit_input_2.returnPressed.connect(MainWindow.returnPressedSlot)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.pushButton_input.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_input_3.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.pushButton_input_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_go.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.label_image0.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


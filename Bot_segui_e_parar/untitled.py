# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        MainWindow.resize(320, 240)
        icon = QIcon()
        icon.addFile(u"../../MiddleMist/Perfil/MiddleMist.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(208, 255, 253);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 80, 171, 47))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label)

        self.botaoa = QPushButton(self.centralwidget)
        self.botaoa.setObjectName(u"botaoa")
        self.botaoa.setGeometry(QRect(120, 140, 75, 23))
        self.botaogo = QPushButton(self.centralwidget)
        self.botaogo.setObjectName(u"botaogo")
        self.botaogo.setGeometry(QRect(120, 210, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Insta bot", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"   Adicionar nomes de pesquisa", None))
        self.botaoa.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.botaogo.setText(QCoreApplication.translate("MainWindow", u"Come\u00e7ar", None))
    # retranslateUi


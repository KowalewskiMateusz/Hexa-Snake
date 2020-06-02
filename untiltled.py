# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
import resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(796, 463)
        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 562, 202))

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(650, 10, 93, 28))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(650, 60, 93, 28))

        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(650, 110, 93, 28))

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(650, 260, 93, 28))

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton")
        self.pushButton_4.setGeometry(QRect(75, 380, 120, 26))

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(650, 160, 93, 28))

        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(650, 210, 93, 28))

        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(75, 420, 120, 26))



        self.QRadioButton = QRadioButton(Dialog)
        self.QRadioButton.setObjectName(u"QRadioButton")
        self.QRadioButton.setGeometry(QRect(650, 340, 81, 20))

        self.QRadioButton2 = QRadioButton(Dialog)
        self.QRadioButton2.setObjectName(u"QRadioButton2")
        self.QRadioButton2.setGeometry(QRect(650, 370, 81, 20))

        self.QRadioButton3 = QRadioButton(Dialog)
        self.QRadioButton3.setObjectName(u"QRadioButton3")
        self.QRadioButton3.setGeometry(QRect(650, 310, 81, 20))
        self.QRadioButton3.setChecked(True)

        self.QRadioButton4 = QRadioButton(Dialog)
        self.QRadioButton4.setObjectName(u"QRadioButton2")
        self.QRadioButton4.setGeometry(QRect(650, 400, 81, 20))

        self.QLineEdit1 = QLineEdit(Dialog)
        self.QLineEdit1.setObjectName(u"QLineEdit1")
        self.QLineEdit1.setGeometry(QRect(80, 220, 105, 26))

        self.QTextEdit1 = QLabel(Dialog)
        self.QTextEdit1.setObjectName(u"QTextEdit1")
        self.QTextEdit1.setGeometry(QRect(20, 220, 105, 26))
        self.QTextEdit1.setText("Host IP")

        self.QLineEdit2 = QLineEdit(Dialog)
        self.QLineEdit2.setObjectName(u"QLineEdit2")
        self.QLineEdit2.setGeometry(QRect(80, 260, 105, 26))

        self.QTextEdit2 = QLabel(Dialog)
        self.QTextEdit2.setObjectName(u"QTextEdit2")
        self.QTextEdit2.setGeometry(QRect(20, 260, 105, 26))
        self.QTextEdit2.setText("Port")

        self.QLineEdit3 = QLineEdit(Dialog)
        self.QLineEdit3.setObjectName(u"QLineEdit3")
        self.QLineEdit3.setGeometry(QRect(80, 300, 105, 26))

        self.QTextEdit3 = QLabel(Dialog)
        self.QTextEdit3.setObjectName(u"QTextEdit3")
        self.QTextEdit3.setGeometry(QRect(20, 300, 105, 26))
        self.QTextEdit3.setText("Nick 1")

        self.QLineEdit4 = QLineEdit(Dialog)
        self.QLineEdit4.setObjectName(u"QLineEdit3")
        self.QLineEdit4.setGeometry(QRect(80, 340, 105, 26))

        self.QTextEdit4 = QLabel(Dialog)
        self.QTextEdit4.setObjectName(u"QTextEdit3")
        self.QTextEdit4.setGeometry(QRect(20, 340, 105, 26))
        self.QTextEdit4.setText("Nick 2")
        newfont = QFont("Times", 12, QFont.Bold)
        self.QTextEdit5 = QLabel(Dialog)
        self.QTextEdit5.setObjectName(u"QTextEdit5")
        self.QTextEdit5.setGeometry(QRect(400, 200, 105, 26))
        self.QTextEdit5.setFont(newfont)
        self.QTextEdit5.setStyleSheet('color: red')
        self.QTextEdit5.setText("User 1")

        self.QTextEdit6 = QLabel(Dialog)
        self.QTextEdit6.setStyleSheet('color: red')
        self.QTextEdit6.setObjectName(u"QTextEdit6")
        self.QTextEdit6.setGeometry(QRect(400, 250, 105, 26))
        self.QTextEdit6.setFont(newfont)
        self.QTextEdit6.setText("User 2")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Nowa gra", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Wyj\u015bcie", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Zapisz ustawienia", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Wczytaj gre", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Replay", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"Wczytaj ustawienia", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Zapisuj gre", None))
        self.QRadioButton.setText(QCoreApplication.translate("Dialog", u"Hot sit", None))
        self.QRadioButton2.setText(QCoreApplication.translate("Dialog", u"Online", None))
        self.QRadioButton3.setText(QCoreApplication.translate("Dialog", u"Solo", None))
        self.QRadioButton4.setText(QCoreApplication.translate("Dialog", u"AI", None))

    # retranslateUi


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(450, 347)
        self.groupBox = QtWidgets.QGroupBox(widget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 431, 251))
        self.groupBox.setObjectName("groupBox")
        self.weatherComboBox = QtWidgets.QComboBox(self.groupBox)
        self.weatherComboBox.setGeometry(QtCore.QRect(80, 30, 221, 21))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.resultText = QtWidgets.QTextEdit(self.groupBox)
        self.resultText.setGeometry(QtCore.QRect(10, 60, 411, 181))
        self.resultText.setObjectName("resultText")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 21))
        self.label.setObjectName("label")
        self.queryBtn = QtWidgets.QPushButton(widget)
        self.queryBtn.setGeometry(QtCore.QRect(90, 300, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.clearBtn = QtWidgets.QPushButton(widget)
        self.clearBtn.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(widget)
        self.clearBtn.clicked.connect(widget.clearResult)
        self.queryBtn.clicked.connect(widget.queryWeather)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "GitPython"))
        self.groupBox.setTitle(_translate("widget", "查询城市天气"))
        self.weatherComboBox.setItemText(0, _translate("widget", "天津"))
        self.weatherComboBox.setItemText(1, _translate("widget", "长春"))
        self.weatherComboBox.setItemText(2, _translate("widget", "北京"))
        self.weatherComboBox.setItemText(3, _translate("widget", "廊坊"))
        self.weatherComboBox.setItemText(4, _translate("widget", "沈阳"))
        self.label.setText(_translate("widget", "城市"))
        self.queryBtn.setText(_translate("widget", "查询"))
        self.clearBtn.setText(_translate("widget", "清空"))



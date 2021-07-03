import json

import requests
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 104)
        MainWindow.setStyleSheet("background-color: rgb(84, 84, 84);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(211, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(125, 125, 125);\n"
                                    "border-radius:10px;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 63 10pt \"Yu Gothic UI\";")
        self.numvalidator = QtGui.QDoubleValidator()
        self.lineEdit.setValidator(self.numvalidator)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 211, 31))
        self.label.setMinimumSize(QtCore.QSize(211, 31))
        self.label.setStyleSheet("border-radius:10px;"
                                 "background-color:rgb(100,100,100)")
        self.label.setText("")
        self.label.setObjectName("label")
        response = requests.get("https://free.currconv.com/api/v7/currencies?apiKey=Your API key")
        data = json.loads(response.text)
        currencies = list(data['results'].keys())
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 20, 73, 31))
        self.comboBox.setMinimumSize(QtCore.QSize(0, 31))
        self.comboBox.setStyleSheet("background-color: rgb(67, 67, 67);\n"
                                    "color: rgb(255, 170, 0);\n"
                                    "border-radius:10px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 60, 73, 31))
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(67, 67, 67);\n"
                                      "color: rgb(255, 170, 0);\n"
                                      "border-radius:10px;")
        self.comboBox_3.setObjectName("comboBox_3")
        for currency in sorted(currencies):
            self.comboBox.addItem(currency)
            self.comboBox_3.addItem(currency)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 51, 51))
        self.pushButton.setStyleSheet("QPushButton{border-radius:25px;}"
                                      "QPushButton::hover"
                                      "{"
                                      "background-color:rgb(50,50,50)"
                                      "}"
                                      "QPushButton::pressed"
                                      "{"
                                      "background-color:rgb(255,170,0)"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(QtGui.QIcon('convert-01.png'))
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.clicked.connect(self.onclick)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyConverter"))

    def onclick(self):
        cfrom = str(self.comboBox.currentText())
        cto = str(self.comboBox_3.currentText())
        cval = float(self.lineEdit.text())

        response = requests.get(
            f"https://free.currconv.com/api/v7/convert?q={cfrom}_{cto}&compact=ultra&apiKey=Your API key")
        data = json.loads(response.text)
        self.label.setText(f"{data[f'{cfrom}_{cto}'] * cval:.2f}")

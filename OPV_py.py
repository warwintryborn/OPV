# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OPV_Designer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1366, 738)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1366, 738))
        Form.setMaximumSize(QtCore.QSize(1366, 738))
        Form.setStyleSheet("background-color:rgb(212, 208, 200)")
        self.label_CAG = QtWidgets.QLabel(Form)
        self.label_CAG.setGeometry(QtCore.QRect(210, 200, 1001, 541))
        self.label_CAG.setAutoFillBackground(False)
        self.label_CAG.setText("")
        self.label_CAG.setPixmap(QtGui.QPixmap("CAG - Python.PNG"))
        self.label_CAG.setObjectName("label_CAG")
        self.label_BAG01 = QtWidgets.QLabel(Form)
        self.label_BAG01.setGeometry(QtCore.QRect(450, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_BAG01.setFont(font)
        self.label_BAG01.setObjectName("label_BAG01")
        self.label_BAG02 = QtWidgets.QLabel(Form)
        self.label_BAG02.setGeometry(QtCore.QRect(440, 370, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_BAG02.setFont(font)
        self.label_BAG02.setObjectName("label_BAG02")
        self.label_BAR = QtWidgets.QLabel(Form)
        self.label_BAR.setGeometry(QtCore.QRect(450, 550, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_BAR.setFont(font)
        self.label_BAR.setObjectName("label_BAR")
        self.label_Chiller01 = QtWidgets.QLabel(Form)
        self.label_Chiller01.setGeometry(QtCore.QRect(790, 250, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Chiller01.setFont(font)
        self.label_Chiller01.setObjectName("label_Chiller01")
        self.label_Chiller02 = QtWidgets.QLabel(Form)
        self.label_Chiller02.setGeometry(QtCore.QRect(800, 470, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Chiller02.setFont(font)
        self.label_Chiller02.setObjectName("label_Chiller02")
        self.label_VAG01 = QtWidgets.QLabel(Form)
        self.label_VAG01.setGeometry(QtCore.QRect(960, 250, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_VAG01.setFont(font)
        self.label_VAG01.setObjectName("label_VAG01")
        self.label_VAG02 = QtWidgets.QLabel(Form)
        self.label_VAG02.setGeometry(QtCore.QRect(950, 470, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_VAG02.setFont(font)
        self.label_VAG02.setObjectName("label_VAG02")
        self.label_TempIns = QtWidgets.QLabel(Form)
        self.label_TempIns.setGeometry(QtCore.QRect(1110, 320, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_TempIns.setFont(font)
        self.label_TempIns.setObjectName("label_TempIns")
        self.label_TempRet = QtWidgets.QLabel(Form)
        self.label_TempRet.setGeometry(QtCore.QRect(280, 330, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_TempRet.setFont(font)
        self.label_TempRet.setObjectName("label_TempRet")
        self.label_TanqueRecalque = QtWidgets.QLabel(Form)
        self.label_TanqueRecalque.setGeometry(QtCore.QRect(190, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_TanqueRecalque.setFont(font)
        self.label_TanqueRecalque.setObjectName("label_TanqueRecalque")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 290, 61, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.text_BAG01 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.text_BAG01.setContentsMargins(0, 0, 0, 0)
        self.text_BAG01.setObjectName("text_BAG01")
        self.label_Comando = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Comando.setFont(font)
        self.label_Comando.setObjectName("label_Comando")
        self.text_BAG01.addWidget(self.label_Comando)
        self.label_Estado = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Estado.setFont(font)
        self.label_Estado.setObjectName("label_Estado")
        self.text_BAG01.addWidget(self.label_Estado)
        self.label_Falha = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Falha.setFont(font)
        self.label_Falha.setObjectName("label_Falha")
        self.text_BAG01.addWidget(self.label_Falha)
        self.label_LR = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_LR.setFont(font)
        self.label_LR.setObjectName("label_LR")
        self.text_BAG01.addWidget(self.label_LR)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 460, 61, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.text_BAG02 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.text_BAG02.setContentsMargins(0, 0, 0, 0)
        self.text_BAG02.setObjectName("text_BAG02")
        self.label_Comando_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Comando_2.setFont(font)
        self.label_Comando_2.setObjectName("label_Comando_2")
        self.text_BAG02.addWidget(self.label_Comando_2)
        self.label_Estado_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Estado_2.setFont(font)
        self.label_Estado_2.setObjectName("label_Estado_2")
        self.text_BAG02.addWidget(self.label_Estado_2)
        self.label_Falha_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Falha_2.setFont(font)
        self.label_Falha_2.setObjectName("label_Falha_2")
        self.text_BAG02.addWidget(self.label_Falha_2)
        self.label_LR_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_LR_2.setFont(font)
        self.label_LR_2.setObjectName("label_LR_2")
        self.text_BAG02.addWidget(self.label_LR_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 630, 61, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.text_BAGR = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.text_BAGR.setContentsMargins(0, 0, 0, 0)
        self.text_BAGR.setObjectName("text_BAGR")
        self.label_Comando_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Comando_3.setFont(font)
        self.label_Comando_3.setObjectName("label_Comando_3")
        self.text_BAGR.addWidget(self.label_Comando_3)
        self.label_Estado_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Estado_3.setFont(font)
        self.label_Estado_3.setObjectName("label_Estado_3")
        self.text_BAGR.addWidget(self.label_Estado_3)
        self.label_Falha_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Falha_3.setFont(font)
        self.label_Falha_3.setObjectName("label_Falha_3")
        self.text_BAGR.addWidget(self.label_Falha_3)
        self.label_LR_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_LR_3.setFont(font)
        self.label_LR_3.setObjectName("label_LR_3")
        self.text_BAGR.addWidget(self.label_LR_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 440, 81, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.text_tempRet = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.text_tempRet.setContentsMargins(0, 0, 0, 0)
        self.text_tempRet.setObjectName("text_tempRet")
        self.label_textTemp = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_textTemp.setFont(font)
        self.label_textTemp.setObjectName("label_textTemp")
        self.text_tempRet.addWidget(self.label_textTemp)
        self.label_tempValor = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_tempValor.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_tempValor.setFont(font)
        self.label_tempValor.setObjectName("label_tempValor")
        self.text_tempRet.addWidget(self.label_tempValor)
        self.label_textC = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_textC.setFont(font)
        self.label_textC.setObjectName("label_textC")
        self.text_tempRet.addWidget(self.label_textC)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1110, 430, 81, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.text_tempIns = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.text_tempIns.setContentsMargins(0, 0, 0, 0)
        self.text_tempIns.setObjectName("text_tempIns")
        self.label_textTemp_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_textTemp_2.setFont(font)
        self.label_textTemp_2.setObjectName("label_textTemp_2")
        self.text_tempIns.addWidget(self.label_textTemp_2)
        self.label_tempValor_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_tempValor_2.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_tempValor_2.setFont(font)
        self.label_tempValor_2.setObjectName("label_tempValor_2")
        self.text_tempIns.addWidget(self.label_tempValor_2)
        self.label_textC_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_textC_2.setFont(font)
        self.label_textC_2.setObjectName("label_textC_2")
        self.text_tempIns.addWidget(self.label_textC_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(770, 360, 61, 71))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.text_Chiller01 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.text_Chiller01.setContentsMargins(0, 0, 0, 0)
        self.text_Chiller01.setObjectName("text_Chiller01")
        self.label_Comando_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Comando_4.setFont(font)
        self.label_Comando_4.setObjectName("label_Comando_4")
        self.text_Chiller01.addWidget(self.label_Comando_4)
        self.label_Estado_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Estado_4.setFont(font)
        self.label_Estado_4.setObjectName("label_Estado_4")
        self.text_Chiller01.addWidget(self.label_Estado_4)
        self.label_Falha_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Falha_4.setFont(font)
        self.label_Falha_4.setObjectName("label_Falha_4")
        self.text_Chiller01.addWidget(self.label_Falha_4)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(770, 590, 61, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.text_Chiller02 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.text_Chiller02.setContentsMargins(0, 0, 0, 0)
        self.text_Chiller02.setObjectName("text_Chiller02")
        self.label_Comando_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Comando_6.setFont(font)
        self.label_Comando_6.setObjectName("label_Comando_6")
        self.text_Chiller02.addWidget(self.label_Comando_6)
        self.label_Estado_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Estado_6.setFont(font)
        self.label_Estado_6.setObjectName("label_Estado_6")
        self.text_Chiller02.addWidget(self.label_Estado_6)
        self.label_Falha_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_Falha_6.setFont(font)
        self.label_Falha_6.setObjectName("label_Falha_6")
        self.text_Chiller02.addWidget(self.label_Falha_6)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(470, 290, 21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("green_led.PNG"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(470, 290, 21, 21))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("red_led.PNG"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "OPV - Operador Virtual"))
        self.label_BAG01.setText(_translate("Form", "BAG01"))
        self.label_BAG02.setText(_translate("Form", "BAG02"))
        self.label_BAR.setText(_translate("Form", "BAGR"))
        self.label_Chiller01.setText(_translate("Form", "Chiller 01"))
        self.label_Chiller02.setText(_translate("Form", "Chiller 02"))
        self.label_VAG01.setText(_translate("Form", "VAG01"))
        self.label_VAG02.setText(_translate("Form", "VAG02"))
        self.label_TempIns.setText(_translate("Form", "Temp Ins"))
        self.label_TempRet.setText(_translate("Form", "Temp Ret"))
        self.label_TanqueRecalque.setText(_translate("Form", "Tanque de Recalque"))
        self.label_Comando.setText(_translate("Form", "Comando"))
        self.label_Estado.setText(_translate("Form", "Estado"))
        self.label_Falha.setText(_translate("Form", "Falha"))
        self.label_LR.setText(_translate("Form", "L/R"))
        self.label_Comando_2.setText(_translate("Form", "Comando"))
        self.label_Estado_2.setText(_translate("Form", "Estado"))
        self.label_Falha_2.setText(_translate("Form", "Falha"))
        self.label_LR_2.setText(_translate("Form", "L/R"))
        self.label_Comando_3.setText(_translate("Form", "Comando"))
        self.label_Estado_3.setText(_translate("Form", "Estado"))
        self.label_Falha_3.setText(_translate("Form", "Falha"))
        self.label_LR_3.setText(_translate("Form", "L/R"))
        self.label_textTemp.setText(_translate("Form", "Temp:"))
        self.label_tempValor.setText(_translate("Form", "00"))
        self.label_textC.setText(_translate("Form", "°C"))
        self.label_textTemp_2.setText(_translate("Form", "Temp:"))
        self.label_tempValor_2.setText(_translate("Form", "00"))
        self.label_textC_2.setText(_translate("Form", "°C"))
        self.label_Comando_4.setText(_translate("Form", "Comando"))
        self.label_Estado_4.setText(_translate("Form", "Estado"))
        self.label_Falha_4.setText(_translate("Form", "Falha"))
        self.label_Comando_6.setText(_translate("Form", "Comando"))
        self.label_Estado_6.setText(_translate("Form", "Estado"))
        self.label_Falha_6.setText(_translate("Form", "Falha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


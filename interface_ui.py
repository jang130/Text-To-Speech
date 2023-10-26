# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(890, 585)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(window)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(window)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.text_label = QtWidgets.QLabel(window)
        self.text_label.setObjectName("text_label")
        self.horizontalLayout_2.addWidget(self.text_label)
        self.text_box = QtWidgets.QLineEdit(window)
        self.text_box.setObjectName("text_box")
        self.horizontalLayout_2.addWidget(self.text_box)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.open_file_tick = QtWidgets.QCheckBox(window)
        self.open_file_tick.setObjectName("open_file_tick")
        self.verticalLayout_3.addWidget(self.open_file_tick)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.language_label = QtWidgets.QLabel(window)
        self.language_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.language_label.setObjectName("language_label")
        self.verticalLayout_2.addWidget(self.language_label)
        self.German_tick = QtWidgets.QRadioButton(window)
        self.German_tick.setObjectName("German_tick")
        self.verticalLayout_2.addWidget(self.German_tick)
        self.Turkish_tick = QtWidgets.QRadioButton(window)
        self.Turkish_tick.setObjectName("Turkish_tick")
        self.verticalLayout_2.addWidget(self.Turkish_tick)
        self.Polish_tick = QtWidgets.QRadioButton(window)
        self.Polish_tick.setObjectName("Polish_tick")
        self.verticalLayout_2.addWidget(self.Polish_tick)
        self.Spanish_tick = QtWidgets.QRadioButton(window)
        self.Spanish_tick.setObjectName("Spanish_tick")
        self.verticalLayout_2.addWidget(self.Spanish_tick)
        self.English_tick = QtWidgets.QRadioButton(window)
        self.English_tick.setObjectName("English_tick")
        self.verticalLayout_2.addWidget(self.English_tick)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.enter_button = QtWidgets.QPushButton(window)
        self.enter_button.setObjectName("enter_button")
        self.verticalLayout_3.addWidget(self.enter_button)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Text To Speech v1.0"))
        self.text_label.setText(_translate("window", "Enter text to convert to speech:"))
        self.open_file_tick.setText(_translate("window", "Do you want to open file after conversion?"))
        self.language_label.setText(_translate("window", "Choose Language:"))
        self.German_tick.setText(_translate("window", "German"))
        self.Turkish_tick.setText(_translate("window", "Turkish"))
        self.Polish_tick.setText(_translate("window", "Polish"))
        self.Spanish_tick.setText(_translate("window", "Spanish"))
        self.English_tick.setText(_translate("window", "English"))
        self.enter_button.setText(_translate("window", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


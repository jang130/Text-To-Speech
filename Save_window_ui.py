# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Save_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_save_window(object):
    def setupUi(self, save_window):
        save_window.setObjectName("save_window")
        save_window.resize(447, 339)
        self.verticalLayout = QtWidgets.QVBoxLayout(save_window)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_label = QtWidgets.QLabel(save_window)
        self.name_label.setObjectName("name_label")
        self.horizontalLayout.addWidget(self.name_label)
        self.name_textbox = QtWidgets.QLineEdit(save_window)
        self.name_textbox.setObjectName("name_textbox")
        self.horizontalLayout.addWidget(self.name_textbox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.save_button = QtWidgets.QPushButton(save_window)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(save_window)
        QtCore.QMetaObject.connectSlotsByName(save_window)

    def retranslateUi(self, save_window):
        _translate = QtCore.QCoreApplication.translate
        save_window.setWindowTitle(_translate("save_window", "Save as"))
        self.name_label.setText(_translate("save_window", "File name:"))
        self.save_button.setText(_translate("save_window", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    save_window = QtWidgets.QDialog()
    ui = Ui_save_window()
    ui.setupUi(save_window)
    save_window.show()
    sys.exit(app.exec_())


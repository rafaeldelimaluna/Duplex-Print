# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cups-dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    is_continue = False

    def setupUi(self, Dialog):
        Dialog.setObjectName("Proxima Etapa")
        Dialog.resize(400, 224)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.MessageContainer = QtWidgets.QFrame(Dialog)
        self.MessageContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MessageContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MessageContainer.setObjectName("MessageContainer")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.MessageContainer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Message_3Label = QtWidgets.QLabel(self.MessageContainer)
        self.Message_3Label.setObjectName("Message_3Label")
        self.verticalLayout_3.addWidget(self.Message_3Label)
        self.Message_1Label = QtWidgets.QLabel(self.MessageContainer)
        self.Message_1Label.setObjectName("Message_1Label")
        self.verticalLayout_3.addWidget(self.Message_1Label)
        self.verticalLayout.addWidget(self.MessageContainer)
        spacerItem = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ContinueBtn = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.Continue())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.ContinueBtn.setStyleSheet(
            "background-color: #004bb5;font: 87 11pt 'Lato Black';")
        self.ContinueBtn.setDefault(False)
        self.ContinueBtn.setSizePolicy(sizePolicy)
        self.ContinueBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.ContinueBtn.setFlat(False)
        self.ContinueBtn.setObjectName("ContinueBtn")
        self.verticalLayout.addWidget(self.ContinueBtn)
        self.AbortBtn = QtWidgets.QPushButton(
            Dialog, clicked=lambda: self.Abort())
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.AbortBtn.sizePolicy().hasHeightForWidth())
        self.AbortBtn.setSizePolicy(sizePolicy)
        self.AbortBtn.setWhatsThis("")
        self.AbortBtn.setStyleSheet(
            "selection-background-color: rgb(255, 98, 46);")
        self.AbortBtn.setObjectName("AbortBtn")
        self.verticalLayout.addWidget(self.AbortBtn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Message_3Label.setText(_translate("Dialog", "Deseja Continuar?"))
        self.Message_1Label.setText(_translate(
            "Dialog", "Primeira parte concluída!"))
        self.ContinueBtn.setText(_translate("Dialog", "Continuar"))
        self.AbortBtn.setText(_translate("Dialog", "Abortar"))

    def Continue(self):
        Ui_Dialog.is_continue = True
        QtCore.QCoreApplication.quit()

    def Abort(self):
        Ui_Dialog.is_continue = False
        QtCore.QCoreApplication.quit()


def Question() -> bool:
    from sys import argv
    app = QtWidgets.QApplication(argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
    return Ui_Dialog.is_continue
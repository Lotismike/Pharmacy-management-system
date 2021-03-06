
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_SaleOnCredit(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(321, 300)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 270, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.billNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.billNumberLabel.setObjectName("billNumberLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.billNumberLabel)
        self.billNumberLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.billNumberLineEdit.setObjectName("billNumberLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.billNumberLineEdit)
        self.billLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.billLabel.setObjectName("billLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.billLabel)
        self.billLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.billLineEdit.setObjectName("billLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.billLineEdit)
        self.cashDownLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cashDownLabel.setObjectName("cashDownLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cashDownLabel)
        self.cashDownLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cashDownLineEdit.setObjectName("cashDownLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cashDownLineEdit)
        self.paymentDateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.paymentDateLabel.setObjectName("paymentDateLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.paymentDateLabel)
        self.paymentDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.paymentDateDateEdit.setObjectName("paymentDateDateEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.paymentDateDateEdit)
        self.clientNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.clientNameLabel.setObjectName("clientNameLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.clientNameLabel)
        self.clientNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.clientNameLineEdit.setObjectName("clientNameLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.clientNameLineEdit)
        self.clientContactLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.clientContactLabel.setObjectName("clientContactLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.clientContactLabel)
        self.clientContactLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.clientContactLineEdit.setObjectName("clientContactLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.clientContactLineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 131, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.billNumberLabel.setText(_translate("Dialog", "Bill Number"))
        self.billLabel.setText(_translate("Dialog", "Bill"))
        self.cashDownLabel.setText(_translate("Dialog", "Cash Down"))
        self.paymentDateLabel.setText(_translate("Dialog", "Payment Date"))
        self.clientNameLabel.setText(_translate("Dialog", "Client Name"))
        self.clientContactLabel.setText(_translate("Dialog", "Client Contact"))
        self.pushButton.setText(_translate("Dialog", "Add Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SaleOnCredit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


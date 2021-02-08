
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_addOrder(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(405, 398)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(19, 10, 401, 80))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(120, 30, 181, 20))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 110, 361, 201))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.medicineIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.medicineIDLabel.setObjectName("medicineIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.medicineIDLabel)
        self.medicineIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.medicineIDLineEdit.setObjectName("medicineIDLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.medicineIDLineEdit)
        self.medicineNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.medicineNameLabel.setObjectName("medicineNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.medicineNameLabel)
        self.medicineNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.medicineNameLineEdit.setObjectName("medicineNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.medicineNameLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.categoryLineEdit)
        self.batchNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.batchNumberLabel.setObjectName("batchNumberLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.batchNumberLabel)
        self.batchNumberLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.batchNumberLineEdit.setObjectName("batchNumberLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.batchNumberLineEdit)
        self.sellingPriceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sellingPriceLabel.setObjectName("sellingPriceLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sellingPriceLabel)
        self.sellingPriceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sellingPriceLineEdit.setObjectName("sellingPriceLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sellingPriceLineEdit)
        self.quantityLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.quantityLabel.setObjectName("quantityLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.quantityLabel)
        self.quantityLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.quantityLineEdit.setObjectName("quantityLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.quantityLineEdit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 330, 211, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Product Details"))
        self.medicineIDLabel.setText(_translate("Dialog", "Medicine ID :"))
        self.medicineNameLabel.setText(_translate("Dialog", "Medicine Name :"))
        self.categoryLabel.setText(_translate("Dialog", "Category :"))
        self.batchNumberLabel.setText(_translate("Dialog", "Batch Number : "))
        self.sellingPriceLabel.setText(_translate("Dialog", "Selling Price :"))
        self.quantityLabel.setText(_translate("Dialog", "Quantity"))
        self.pushButton.setText(_translate("Dialog", "Add Order"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_addOrder()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

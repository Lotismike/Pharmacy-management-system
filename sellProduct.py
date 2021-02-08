from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
class Ui_sellProduct(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(396, 407)
        self.setWindowFlags(QtCore.Qt.Window)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 31))
        self.label.setObjectName("sellTitle")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 50, 361, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.drugIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.drugIDLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.drugIDLabel)
        self.drugIDLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.drugIDLineEdit.setObjectName("drugIDLineEdit")
        self.drugIDLineEdit.setReadOnly(1)

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.drugIDLineEdit)
        self.drugNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.drugNameLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.drugNameLabel)
        self.drugNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.drugNameLineEdit.setObjectName("drugNameLineEdit")
        self.drugNameLineEdit.setReadOnly(1)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.drugNameLineEdit)
        self.batchNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.batchNumberLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.batchNumberLabel)
        self.batchNumberLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.batchNumberLineEdit.setObjectName("batchNumberLineEdit")
        self.batchNumberLineEdit.setReadOnly(1)

        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.batchNumberLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.categoryLineEdit.setObjectName("categoryLineEdit")
        self.categoryLineEdit.setReadOnly(1)

        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.categoryLineEdit)
        self.sellingPriceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sellingPriceLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sellingPriceLabel)
        self.sellingPriceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sellingPriceLineEdit.setObjectName("sellingPriceLineEdit")
        self.sellingPriceLineEdit.setReadOnly(1)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sellingPriceLineEdit)
        self.quantityLeftLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.quantityLeftLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.quantityLeftLabel)
        self.quantityLeftLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.quantityLeftLineEdit.setObjectName("quantityLeftLineEdit")
        self.quantityLeftLineEdit.setReadOnly(1)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.quantityLeftLineEdit)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 250, 361, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(36, 12, 301, 31))
        self.label_2.setObjectName("qtnLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(32, 60, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 151, 41))
        self.pushButton.setObjectName("sellBTN")
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Item "))
        Dialog.setWindowIcon(QIcon('data/images/logoicon.ICO'))
        self.label.setText(_translate("Dialog", "Add  item to the list of items to be billed "))
        self.drugIDLabel.setText(_translate("Dialog", "Drug ID"))
        self.drugNameLabel.setText(_translate("Dialog", "Drug Name"))
        self.batchNumberLabel.setText(_translate("Dialog", "Batch Number"))
        self.categoryLabel.setText(_translate("Dialog", "Category"))
        self.sellingPriceLabel.setText(_translate("Dialog", "Selling Price"))
        self.quantityLeftLabel.setText(_translate("Dialog", "Quantity In Stock :"))
        self.label_2.setText(_translate("Dialog", "Enter Quantity"))
        self.pushButton.setText(_translate("Dialog", "ADD ITEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_sellProduct()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

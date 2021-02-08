
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
class Ui_UpdateListRow(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(396, 384)
        self.setWindowFlags(QtCore.Qt.Window)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 31))
        self.label.setObjectName("sellTitle")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.drugNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.drugNameLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.drugNameLabel)
        self.drugNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.drugNameLineEdit.setObjectName("drugNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.drugNameLineEdit)
        self.sellingPriceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sellingPriceLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sellingPriceLabel)
        self.sellingPriceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sellingPriceLineEdit.setObjectName("sellingPriceLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sellingPriceLineEdit)
        self.quantityLeftLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.quantityLeftLabel.setObjectName("sellLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.quantityLeftLabel)
        self.quantityLeftLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.quantityLeftLineEdit.setObjectName("quantityLeftLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.quantityLeftLineEdit)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 190, 361, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(86, 12, 201, 31))
        self.label_2.setObjectName("qtnLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(32, 60, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(180, 110, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 131, 51))
        self.pushButton.setObjectName("sellBTN")
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 110, 131, 51))
        self.pushButton_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("profitBTN")

        self.retranslateUi(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Update / Delete Item"))
        Dialog.setWindowIcon(QIcon('data/images/logoicon.ICO'))
        self.label.setText(_translate("Dialog", "Update / Delete From The List"))
        self.drugNameLabel.setText(_translate("Dialog", "Drug Name"))
        self.sellingPriceLabel.setText(_translate("Dialog", "Selling Price"))
        self.quantityLeftLabel.setText(_translate("Dialog", "Quantity In Stock :"))
        self.label_2.setText(_translate("Dialog", "Update Quantity"))
        self.pushButton.setText(_translate("Dialog", "UPDATE"))
        self.pushButton_2.setText(_translate("Dialog", "DELETE  ROW"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_UpdateListRow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


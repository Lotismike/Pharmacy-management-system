
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_DeleteRow(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(279, 129)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 80, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel| QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("delBTNS")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 241, 41))
        self.label.setObjectName("sellLabel")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.buttonBox.accepted.connect(lambda:self.deleteMe(1))
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delete Row"))
        Dialog.setWindowIcon(QIcon('data/images/logoicon.ICO'))
        self.label.setText(_translate("Dialog", "Do you want to delete this record?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_DeleteRow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


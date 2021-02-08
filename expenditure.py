
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
import pharmacyLoginController as PLC
class Ui_Expenditure(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(942, 594)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 950, 64))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("header")
        self.backImg = QtWidgets.QLabel(self.frame)
        self.backImg.setGeometry(QtCore.QRect(30, 12, 40, 41))
        self.backImg.setObjectName("backImg")
        self.backImg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        pixmap = QPixmap('data/images/back2.png')
        self.backImg.setPixmap(pixmap)
        self.backImg.setScaledContents(True)
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(300, 9, 351, 50))
        self.title.setObjectName("pagesTitle")
        self.username = QtWidgets.QLabel(self.frame)
        self.username.setGeometry(QtCore.QRect(830, 12, 120, 40))
        self.username.setObjectName("usernameLabel")

        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(300, 130, 351, 451))
        self.widget_2.setObjectName("widget_2")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.label_10.setObjectName("userLabel")
        self.nationalID = QtWidgets.QLineEdit(self.widget_2)
        self.nationalID.setGeometry(QtCore.QRect(0, 30, 321, 31))
        self.nationalID.setObjectName("nationalID")
        self.homeDist = QtWidgets.QLineEdit(self.widget_2)
        self.homeDist.setGeometry(QtCore.QRect(0, 100, 321, 31))
        self.homeDist.setObjectName("homeDist")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(0, 70, 271, 31))
        self.label_11.setObjectName("userLabel")
        self.currentDist = QtWidgets.QLineEdit(self.widget_2)
        self.currentDist.setGeometry(QtCore.QRect(0, 170, 321, 31))
        self.currentDist.setObjectName("currentDist")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(0, 140, 271, 31))
        self.label_12.setObjectName("userLabel")
        self.currentAddress = QtWidgets.QLineEdit(self.widget_2)
        self.currentAddress.setGeometry(QtCore.QRect(0, 240, 321, 31))
        self.currentAddress.setObjectName("currentAddress")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(0, 210, 271, 31))
        self.label_13.setObjectName("userLabel")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(0, 280, 271, 31))
        self.label_14.setObjectName("userLabel")
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 310, 321, 71))
        self.textEdit.setObjectName("textEdit")
        self.addExpenseBTN = QtWidgets.QPushButton(self.widget_2)
        self.addExpenseBTN.setGeometry(QtCore.QRect(50, 400, 211, 51))
        self.addExpenseBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.addExpenseBTN.setObjectName("pagesBTN")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 85, 411, 20))
        self.label.setObjectName("pagesLabel")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(200, 105, 451, 2))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(270, 106, 2, 470))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Staff\'s Exependiture | UG- Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Staff\'s Exependiture"))
        self.username.setText(_translate("Dialog", "Username"))
        self.label_10.setText(_translate("Dialog", "Item Name*"))
        self.label_11.setText(_translate("Dialog", "Cost Per Item*"))
        self.label_12.setText(_translate("Dialog", "Quantity*"))
        self.label_13.setText(_translate("Dialog", "Total Amount*"))
        self.label_14.setText(_translate("Dialog", "Brief Description"))
        self.addExpenseBTN.setText(_translate("Dialog", "Add Expense"))
        self.label.setText(_translate("Dialog", "Use the form below for expenditure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Expenditure()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


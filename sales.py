
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
import pharmacyLoginController as PLC
class Ui_sales(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(927, 591)
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
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(630, 63, 2, 520))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 303, 631, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line")
        self.medName = QtWidgets.QLineEdit(Dialog)
        self.medName.setGeometry(QtCore.QRect(20, 90, 191, 22))
        self.medName.setObjectName("medName")
        self.medID = QtWidgets.QLineEdit(Dialog)
        self.medID.setGeometry(QtCore.QRect(450, 90, 171, 21))
        self.medID.setObjectName("medID")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 120, 601, 171))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        colHeaders = ['Drug ID', 'Drug Name', 'Batch No.', 'Category', 'Selling Price', 'Manufacturer']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        self.tableWidget.cellClicked.connect(self.rowData)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 320, 261, 20))
        self.label_4.setObjectName("searchLabel")
        self.billOrderBTN = QtWidgets.QPushButton(Dialog)
        self.billOrderBTN.setGeometry(QtCore.QRect(470, 312, 151, 31))
        self.billOrderBTN.setObjectName("billBTN")
        self.billOrderBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.billOrderBTN.clicked.connect(self.billOrder)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 350, 601, 231))
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        colHeaders2 = ['Drug ID', 'Drug Name', 'Selling Price', 'Quantity', 'Total', 'Batch No.', 'Category']
        self.tableWidget_2.setHorizontalHeaderLabels(colHeaders2)
        self.medName_2 = QtWidgets.QComboBox(Dialog)
        self.medName_2.setGeometry(QtCore.QRect(240, 90, 181, 22))
        self.medName_2.setObjectName("medName_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(640, 88, 271, 31))
        self.widget.setObjectName("calSection")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 5, 81, 21))
        self.label_5.setObjectName("searchLabel")
        self.billDate = QtWidgets.QLineEdit(self.widget)
        self.billDate.setGeometry(QtCore.QRect(90, 5, 171, 21))
        self.billDate.setObjectName("billDate")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(640, 128, 271, 451))
        self.widget_2.setObjectName("calSection")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(0, -1, 271, 16))
        self.label_6.setObjectName("innerSec2")
        self.formLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.totalAmountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.totalAmountLabel.setObjectName("saleLevel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totalAmountLabel)
        self.totalAmount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.totalAmount.setObjectName("totalAmount")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalAmount)
        self.discountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.discountLabel.setObjectName("saleLevel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.discountLabel)
        self.discount = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.discount.setObjectName("discount")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.discount)
        self.calBTN = QtWidgets.QPushButton(self.widget_2)
        self.calBTN.setGeometry(QtCore.QRect(80, 83, 131, 31))
        self.calBTN.setObjectName("calBTN")
        self.calBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.calBTN.clicked.connect(self.calculateBill)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 251, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.totalAmountLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.totalAmountLabel_2.setObjectName("saleLevel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totalAmountLabel_2)
        self.bill = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.bill.setObjectName("bill")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.bill)
        self.discountLabel_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.discountLabel_2.setObjectName("saleLevel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.discountLabel_2)
        self.payMethod = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.payMethod.setObjectName("payMethod")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.payMethod)
        self.paidByLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.paidByLabel.setObjectName("saleLevel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.paidByLabel)
        self.cleintName = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.cleintName.setObjectName("cleintName")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cleintName)
        self.workedOnByLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.workedOnByLabel.setObjectName("saleLevel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.workedOnByLabel)
        self.userName = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.userName.setObjectName("userName")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.userName)
        self.subOrderBTN = QtWidgets.QPushButton(self.widget_2)
        self.subOrderBTN.setGeometry(QtCore.QRect(10, 390, 250, 51))
        self.subOrderBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.subOrderBTN.setObjectName("subOrderBTN")
        self.subOrderBTN.clicked.connect(self.addBill)

        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(0, 120, 271, 16))
        self.label_8.setObjectName("innerSec")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(0, 269, 271, 16))
        self.label_9.setObjectName("innerSec")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.widget_2)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 290, 251, 91))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.cashDownLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.cashDownLabel.setObjectName("saleLevel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.cashDownLabel)
        self.cashDownLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.cashDownLineEdit.setObjectName("cashDownLineEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cashDownLineEdit)
        self.paymentDateLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.paymentDateLabel.setObjectName("saleLevel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.paymentDateLabel)
        self.paymentDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_3)
        self.paymentDateDateEdit.setObjectName("paymentDateDateEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.paymentDateDateEdit)
        self.clientContactLabel = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.clientContactLabel.setObjectName("saleLevel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.clientContactLabel)
        self.clientContactLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.clientContactLineEdit.setObjectName("clientContactLineEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.clientContactLineEdit)

        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 611, 20))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("searchLabel")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("searchLabel")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("searchLabel")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(700, 68, 131, 21))
        self.label_7.setObjectName("searchLabel")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Point Of Sale | ug - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Point Of Sale"))
        self.username.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "LIST OF ITEMS TO BE BILLED"))
        self.billOrderBTN.setText(_translate("Dialog", "BILL ORDER"))
        self.label_5.setText(_translate("Dialog", "Bill Number "))
        self.label_6.setText(_translate("Dialog", "Discount"))
        self.totalAmountLabel.setText(_translate("Dialog", "Total Amount  "))
        self.discountLabel.setText(_translate("Dialog", "Discount (%)  "))
        self.calBTN.setText(_translate("Dialog", "CALCULATE BILL"))
        self.totalAmountLabel_2.setText(_translate("Dialog", "Bill  "))
        self.discountLabel_2.setText(_translate("Dialog", "Payment Method  "))
        self.paidByLabel.setText(_translate("Dialog", "Paid By :"))
        self.workedOnByLabel.setText(_translate("Dialog", "Worked on By "))
        self.subOrderBTN.setText(_translate("Dialog", "SUBMIT ORDER"))

        self.label_8.setText(_translate("Dialog", "Final Bill"))
        self.label_9.setText(_translate("Dialog", "Taken On Credit"))
        self.cashDownLabel.setText(_translate("Dialog", "Cash Down"))
        self.paymentDateLabel.setText(_translate("Dialog", "Payment Date"))
        self.clientContactLabel.setText(_translate("Dialog", "Client Contact"))
        self.label.setText(_translate("Dialog", "Search By drug Name"))
        self.label_2.setText(_translate("Dialog", " Search By Category"))
        self.label_3.setText(_translate("Dialog", " Search By Batch Number"))
        self.label_7.setText(_translate("Dialog", "BILLING SECTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_sales()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


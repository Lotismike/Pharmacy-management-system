
from PyQt5 import QtCore, QtGui, QtWidgets
import errors as E
from PyQt5.QtGui import QCursor
import categoryController as CC
import addDrugController as ADC
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_expiry(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(927, 594)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 950, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("header")
        self.backImg = QtWidgets.QLabel(self.frame)
        self.backImg.setGeometry(QtCore.QRect(30, 16, 40, 41))
        self.backImg.setObjectName("backImg")
        self.backImg.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        pixmap = QPixmap('data/images/back2.png')
        self.backImg.setPixmap(pixmap)
        self.backImg.setScaledContents(True)
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setGeometry(QtCore.QRect(300, 20, 351, 50))
        self.title.setObjectName("pagesTitle")
        self.username = QtWidgets.QLabel(self.frame)
        self.username.setGeometry(QtCore.QRect(830, 20, 120, 50))
        self.username.setObjectName("usernameLabel")
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

        self.refreshBTN = QtWidgets.QPushButton(Dialog)
        self.refreshBTN.setGeometry(QtCore.QRect(370, 542, 191, 40))
        self.refreshBTN.setObjectName("pagesBTN")
        self.refreshBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBTN.setDefault(False)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 811, 381))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setObjectName("tableWidget")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(620, 110, 251, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(60, 110, 231,25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(620, 88, 251, 20))
        self.label_2.setObjectName("searchLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 88, 231, 20))
        self.label.setObjectName("searchLabel")
        self.medName_2 = QtWidgets.QComboBox(Dialog)
        self.medName_2.setGeometry(QtCore.QRect(330, 110, 251, 25))
        self.medName_2.setObjectName("medName_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(330, 88, 251, 20))
        self.label_5.setObjectName("searchLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #setting intails
        colHeaders = ['Entry Date', 'Drug ID', 'Drug Name','Days To Expire','Reorder Level', 'Expiry Date', 'Batch No.', 'Category', 'Quantity', 'Buying Price',
                      'Selling Price', 'Supplier']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        self.medName_2.addItem("Select Category")
        # loading usernames
        catList = CC.categoryController.getCatData()
        for x in catList:
            self.medName_2.addItem(x.getCatName())

        self.refreshBTN.clicked.connect(self.loadExpire)
        self.lineEdit.returnPressed.connect(lambda: self.searchExpire("drugName"))
        self.lineEdit_2.returnPressed.connect(lambda: self.searchExpire("batch"))
        self.medName_2.currentIndexChanged.connect(lambda: self.searchExpire("category"))
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

        self.loadExpire()
    # loadOutStock
    def loadExpire(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(ADC.addDrugController.loadExpire()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # search OutStock
    def searchExpire(self, searchType):
        eObj = E.errors()
        self.tableWidget.setRowCount(0)
        if searchType == "category":
            sword = self.medName_2.currentText()
            if self.medName_2.currentIndex() != 0:
                if len(ADC.addDrugController.searchExpire(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchExpire(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drugs in the selected category')
            else:
                eObj.errorBox('Error', 'Please select a category')

        if searchType == "drugName":
            sword = self.lineEdit.text()
            if sword == "":
                eObj.errorBox('Error', 'Please enter a drug name')
            else:
                self.tableWidget.setRowCount(0)
                if len(ADC.addDrugController.searchExpire(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchExpire(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drug found with the entered drug name')

        if searchType == "batch":
            sword = self.lineEdit_2.text()
            if sword == "":
                eObj.errorBox('Error', 'Please enter a Batch Number')
            else:
                self.tableWidget.setRowCount(0)
                if len(ADC.addDrugController.searchExpire(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchExpire(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drug with such Batch Number')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Soon To Expire | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Soon To Expire"))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label_2.setText(_translate("Dialog", "Search By Batch Number"))
        self.label.setText(_translate("Dialog", "Search By Medicine"))
        self.label_5.setText(_translate("Dialog", "Search By Category"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_expiry()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


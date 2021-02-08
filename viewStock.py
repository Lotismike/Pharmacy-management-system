from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import addDrugController as ADC
import categoryController as CC
import errors as E
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_viewStock(object):
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

        self.medName_2 = QtWidgets.QComboBox(Dialog)
        self.medName_2.setGeometry(QtCore.QRect(330, 110, 261, 25))
        self.medName_2.setObjectName("searchField")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 110, 241, 25))
        self.lineEdit.setObjectName("searchField")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 110, 241, 25))
        self.lineEdit_2.setObjectName("searchField")

        self.refreshBTN = QtWidgets.QPushButton(Dialog)
        self.refreshBTN.setGeometry(QtCore.QRect(370, 542, 191, 40))
        self.refreshBTN.setObjectName("pagesBTN")
        self.refreshBTN.setDefault(False)
        self.refreshBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBTN.clicked.connect(self.loadStock)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 150, 821, 381))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(15)
        self.tableWidget.setObjectName("tableWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 88, 241, 20))
        self.label.setObjectName("searchLabel")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(340, 88, 231, 20))
        self.label_5.setObjectName("searchLabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(630, 88, 231, 20))
        self.label_2.setObjectName("searchLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # loading categories
        self.medName_2.addItem("Select Category")
        catList = CC.categoryController.getCatData()
        for x in catList:
            self.medName_2.addItem(x.getCatName())

        # call loadStock
        self.loadStock()
        #intial
        colHeaders = ['Entry Date', 'Drug ID', 'Drug Name', 'Batch No.', 'Category', 'Quantity', 'Cost Price','Total Cost Price',
                      'Selling Price','Total Selling Price', 'Supplier', 'Reorder Level', 'Expiry Date', 'Added By', 'Created AT']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(9, QtWidgets.QHeaderView.ResizeToContents)

        self.medName_2.currentIndexChanged.connect(lambda: self.searchStock("category"))
        self.lineEdit.returnPressed.connect(lambda: self.searchStock("drugName"))
        self.lineEdit_2.returnPressed.connect(lambda: self.searchStock("batch"))
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

    # load stock
    def loadStock(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(ADC.addDrugController.loadStock()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # search stock
    def searchStock(self, searchType):
        eObj = E.errors()
        if searchType == "category":
            self.tableWidget.setRowCount(0)
            sword = self.medName_2.currentText()
            if self.medName_2.currentIndex() !=0:
                self.tableWidget.setRowCount(0)
                if len(ADC.addDrugController.searchDrug(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchDrug(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drugs in the selected category')
            else:
                eObj.errorBox('Error', 'Please Select Category')

        if searchType == "drugName":
            self.tableWidget.setRowCount(0)
            sword = self.lineEdit.text()
            if sword == "":
                eObj.errorBox('Error', 'Please enter a drug name')
            else:
                self.tableWidget.setRowCount(0)
                if len(ADC.addDrugController.searchDrug(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchDrug(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drug found with the entered drug name')

        if searchType == "batch":
            self.tableWidget.setRowCount(0)
            sword = self.lineEdit_2.text()
            if sword == "":
                eObj.errorBox('Error', 'Please enter a Batch Number')
            else:
                self.tableWidget.setRowCount(0)
                if len(ADC.addDrugController.searchDrug(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(ADC.addDrugController.searchDrug(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drug with such Batch Number')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Stock | UG - Pharmacy Management System"))
        Dialog.setWindowIcon(QIcon('data/images/logoicon.ICO'))
        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "View Stock"))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label.setText(_translate("Dialog", "Search By Drug Name"))
        self.label_5.setText(_translate("Dialog", "Search By Category"))
        self.label_2.setText(_translate("Dialog", "Search By Batch"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_viewStock()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


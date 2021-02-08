from datetime import datetime
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import mainController as MC
import categoryController as CC
import errors as E
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_viewSalesAdmin(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(942, 594)
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
        self.tableWidget.setGeometry(QtCore.QRect(40, 150, 861, 381))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(13)
        colHeaders2 = ['Date of Sale', 'Bill Number', 'Category', 'Medicine Name', 'Batch No.', 'Selling Price',
                       'Quantity','Total', 'Discount', 'Discounted', 'Payment Mode', 'Client', 'Sold By']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders2)
        self.tableWidget.setObjectName("tableWidget")
        self.medName_2 = QtWidgets.QComboBox(Dialog)
        self.medName_2.setGeometry(QtCore.QRect(420, 110, 151, 25))
        self.medName_2.setObjectName("medName_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(250, 110, 161, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 88, 181, 21))
        self.label.setObjectName("searchLabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 88, 181, 21))
        self.label_2.setObjectName("searchLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(730, 88, 151, 21))
        self.label_3.setObjectName("searchLabel")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(730, 110, 171, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(40, 110, 91, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(140, 110, 91, 25))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 88, 121, 20))
        self.label_4.setObjectName("searchLabel")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 88, 71, 20))
        self.label_5.setObjectName("searchLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(580, 110, 141, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(586, 88, 131, 20))
        self.label_6.setObjectName("searchLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # intails
        self.medName_2.addItem("Select Category")
        self.comboBox.addItem("Select Username")
        self.medName_2.currentIndexChanged.connect(lambda: self.searchSales("category"))
        self.comboBox.currentIndexChanged.connect(lambda: self.searchSales("username"))
        self.lineEdit.returnPressed.connect(lambda: self.searchSales("drugName"))
        self.lineEdit_2.returnPressed.connect(lambda: self.searchSales("batch"))
        self.refreshBTN.clicked.connect(self.loadSales)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

        # loading categories
        catList = CC.categoryController.getCatData()
        for x in catList:
            self.medName_2.addItem(x.getCatName())

        #loading usernames
        catList = MC.mainController.getUserData()
        for x in catList:
            self.comboBox.addItem(x.getUsername())

        self.loadSales()
    # load sales
    def loadSales(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(MC.mainController.loadSales()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # search sales
    def searchSales(self, searchType):
        startDate = self.dateEdit.text()
        endDate = self.dateEdit_2.text()
        # sub dates
        start_date = datetime.strptime(startDate, "%d/%m/%Y")
        end_date = datetime.strptime(endDate, "%d/%m/%Y")
        diff = end_date - start_date
        eObj = E.errors()
        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            self.tableWidget.setRowCount(0)
            if searchType == "category":
                sword = self.medName_2.currentText()
                if self.medName_2.currentIndex() != 0:
                    self.tableWidget.setRowCount(0)
                    if len(MC.mainController.searchSales(sword, searchType,startDate,endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(MC.mainController.searchSales(sword, searchType,startDate,endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drugs in the selected category')
                else:
                    eObj.errorBox('Error', 'Please select category')

            if searchType == "drugName":
                sword = self.lineEdit.text()
                self.tableWidget.setRowCount(0)
                if sword == "":
                    eObj.errorBox('Error', 'Please enter a drug name')
                else:

                    if len(MC.mainController.searchSales(sword, searchType,startDate,endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(MC.mainController.searchSales(sword, searchType,startDate,endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drug found with the entered drug name')

            if searchType == "username":
                sword = self.comboBox.currentText()
                if self.comboBox.currentIndex() != 0:
                    self.tableWidget.setRowCount(0)
                    if len(MC.mainController.searchSales(sword, searchType,startDate,endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(MC.mainController.searchSales(sword, searchType,startDate,endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'Selected user has no sale yet')
                else:
                    eObj.errorBox('Error', 'Please select username')

            if searchType == "batch":
                sword = self.lineEdit_2.text()
                self.tableWidget.setRowCount(0)
                if sword == "":
                    eObj.errorBox('Error', 'Please enter a batch number')
                else:

                    if len(MC.mainController.searchSales(sword, searchType,startDate,endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(MC.mainController.searchSales(sword, searchType,startDate,endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drug found with the entered batch number')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "View Sales | UG - Pharmacy Management System"))
        Dialog.setWindowIcon(QIcon('data/images/logoicon.ICO'))
        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "View Sales"))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Category"))
        self.label_3.setText(_translate("Dialog", "Drug Name"))
        self.label_4.setText(_translate("Dialog", "Start From"))
        self.label_5.setText(_translate("Dialog", "End At"))
        self.label_6.setText(_translate("Dialog", "Batch No."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_viewSalesAdmin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

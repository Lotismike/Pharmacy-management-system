from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
import mainController as MC
from PyQt5.QtGui import QCursor
import errors as E
import time
import pharmacyLoginController as PLC
class Ui_viewSoldOnCredit(object):
    def __init__(self):
        global createDate
        unix = time.time()
        createDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

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
        self.refreshBTN.setAutoDefault(False)

        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 150, 861, 381))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(364, 88, 171, 20))
        self.label_2.setObjectName("searchLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(720, 88, 161, 20))
        self.label_3.setObjectName("searchLabel")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(720, 110, 181, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(40, 110, 141, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(200, 110, 141, 25))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 88, 141, 20))
        self.label_4.setObjectName("searchLabel")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 88, 141, 20))
        self.label_5.setObjectName("searchLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(544, 110, 161, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(550, 88, 141, 20))
        self.label_6.setObjectName("searchLabel")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 110, 171, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #intials
        self.loadSaleCredit()

        colHeaders = ['Bill Number','Payment Date', 'Client Name', 'Client Phone', 'Bill', 'Amount Paid',
                      'Balance','Worked On By','Created At']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)

        self.lineEdit_3.returnPressed.connect(lambda :self.searchSalesCredit("billNumber"))
        self.lineEdit_2.returnPressed.connect(lambda: self.searchSalesCredit("clientName"))
        self.lineEdit.returnPressed.connect(lambda: self.searchSalesCredit("user"))
        self.refreshBTN.clicked.connect(self.loadSaleCredit)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

    def loadSaleCredit(self):
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(MC.mainController.loadSalesCredit()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def searchSalesCredit(self,searchType):
        startDate = self.dateEdit.text()
        endDate = self.dateEdit_2.text()
        #sub dates
        start_date = datetime.strptime(startDate, "%d/%m/%Y")
        end_date = datetime.strptime(endDate, "%d/%m/%Y")
        diff = end_date - start_date
        eObj = E.errors()
        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:

            if searchType == "billNumber":
                self.tableWidget.setRowCount(0)
                sword = self.lineEdit_3.text()
                if sword == "":
                    eObj.errorBox('Error', 'Please enter Bill Number')
                else:
                    self.tableWidget.setRowCount(0)
                    if len(MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(
                                MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drugs sold on credit with that bill number in the specified period')

            if searchType == "clientName":
                self.tableWidget.setRowCount(0)
                sword = self.lineEdit_2.text()
                if sword == "":
                    eObj.errorBox('Error', 'Please enter client name')
                else:
                    if len(MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drugs sold on credit to that client in the specified period')

            if searchType == "user":
                self.tableWidget.setRowCount(0)
                sword = self.lineEdit.text()
                if sword == "":
                    eObj.errorBox('Error', 'Please enter Username /staff name')
                else:
                    self.tableWidget.setRowCount(0)
                    if len(MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate).fetchall()) > 0:
                        for row_number, row_data in enumerate(
                                MC.mainController.searchSalesCredit(sword, searchType, startDate, endDate)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))
                    else:
                        eObj.errorBox('Error', 'No drugs sold on credit by that user in the specified period')


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sales Sold On Credit | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Drugs Sold On credit"))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label_2.setText(_translate("Dialog", "Search By Bill No."))
        self.label_3.setText(_translate("Dialog", "Search By Staff"))
        self.label_4.setText(_translate("Dialog", "Start From"))
        self.label_5.setText(_translate("Dialog", "End At"))
        self.label_6.setText(_translate("Dialog", "Search By Client Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_viewSoldOnCredit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


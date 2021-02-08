from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import errors as E
import expenseController as EC
import pharmacyLoginController as PLC
class Ui_viewUserExpenditure(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(927, 594)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
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
        self.refreshBTN.setGeometry(QtCore.QRect(380, 550, 191, 41))
        self.refreshBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBTN.setObjectName("pagesBTN")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(140, 110, 201, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 88, 201, 20))
        self.label.setObjectName("pagesLabel")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(710, 110, 161, 31))
        self.pushButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pagesBTN")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 811, 391))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")

        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(380, 110, 201, 25))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(380, 88, 201, 20))
        self.label_3.setObjectName("pagesLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #intails
        self.tableWidget.setColumnCount(8)
        colHeaders = ['ID', 'Entry Date', 'Username', 'Item', 'Cost Per Item', 'Quantity', 'Amount',
                      'Description']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

        # loading usernames
        self.refreshBTN.clicked.connect(self.loadExpense)
        self.pushButton.clicked.connect(self.searchExpense)

        self.loadExpense()

    #load sexpenses
    def loadExpense(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(EC.expenseController.loadUserExpenses()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def searchExpense(self):
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
            if len(EC.expenseController.searchUserExpenses(startDate, endDate).fetchall()) > 0:
                for row_number, row_data in enumerate(EC.expenseController.searchUserExpenses(startDate, endDate)):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                eObj.errorBox('Error', 'No expenses made by the selected user')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Staff\'s Expenditure | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Staff\'s Expenditure"))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label.setText(_translate("Dialog", "Start Date"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.label_3.setText(_translate("Dialog", "End Date"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_viewUserExpenditure()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


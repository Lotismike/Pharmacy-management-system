
from PyQt5 import QtCore, QtGui, QtWidgets
import errors as E
from PyQt5.QtGui import QCursor
from datetime import datetime
import profitController as PC
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_profit(object):
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

        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(310, 88, 91, 20))
        self.label_12.setObjectName("searchLabel")
        self.dateEdit_9 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_9.setGeometry(QtCore.QRect(110, 88, 171, 25))
        self.dateEdit_9.setObjectName("dateEdit_9")
        self.dateEdit_10 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_10.setGeometry(QtCore.QRect(400, 88, 171, 25))
        self.dateEdit_10.setObjectName("dateEdit_10")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(630, 85, 281, 30))
        self.pushButton_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("profitBTN")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(20, 88, 91, 20))
        self.label_13.setObjectName("searchLabel")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 110, 671, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(5, 11, 661, 451))
        self.tableWidget.setRowCount(15)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(720, 110, 181, 471))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.label.setObjectName("searchLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 161, 31))
        self.label_2.setObjectName("searchLabel")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 171, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 161, 31))
        self.label_3.setObjectName("searchLabel")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 200, 171, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 250, 171, 31))
        self.label_4.setObjectName("searchLabel")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 280, 171, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(0, 330, 200, 31))
        self.label_5.setObjectName("searchLabel")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 360, 171, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(0, 400, 200, 31))
        self.label_6.setObjectName("searchLabel")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 430, 171, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(700, 120, 16, 471))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #my intail
        colHeaders = ['Drug Name', 'Cost Price', 'Quantity', 'Total Costs', 'Total Sales', 'Profit / Loss','Entry Date']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.pushButton_6.clicked.connect(self.calculatProfit)
        self.lineEdit.setReadOnly(1)
        self.lineEdit_2.setReadOnly(1)
        self.lineEdit_3.setReadOnly(1)
        self.lineEdit_4.setReadOnly(1)
        self.lineEdit_5.setReadOnly(1)
        self.lineEdit_6.setReadOnly(1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))

    #calculatProfit
    def calculatProfit(self):
        eObj = E.errors()
        sDate = self.dateEdit_9.text()
        eDate = self.dateEdit_10.text()

        # sub dates
        start_date = datetime.strptime(sDate, "%d/%m/%Y")
        end_date = datetime.strptime(eDate, "%d/%m/%Y")
        diff = end_date - start_date

        if diff.days == 0:
            eObj.errorBox("Error", "Please enter date interval")
        elif diff.days < 0:
            eObj.errorBox("Error", "End date should be greater than start date")
        else:
            self.tableWidget.setRowCount(0)
            if len(PC.profitController.searchProfit(sDate, eDate).fetchall())>0:
                for row_number, row_data in enumerate(
                        PC.profitController.searchProfit(sDate, eDate)):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number,
                                                 QtWidgets.QTableWidgetItem(str(data)))
                #table totals
                totalRows = self.tableWidget.rowCount()

                #totalCost
                totalCosts = 0
                for row in range(0, totalRows):
                    totalCosts = totalCosts + int(self.tableWidget.item(row, 3).text())
                self.lineEdit_2.setText(str(totalCosts))

                # totalSales
                totalSales = 0
                for row in range(0, totalRows):
                    totalSales = totalSales + float(self.tableWidget.item(row, 4).text())
                self.lineEdit.setText(str(totalSales))

                #total credit
                totalCredit = 0
                for row in PC.profitController.getTotalCredit(sDate, eDate).fetchall():
                    if row[0] is not None:
                        totalCredit = row[0]


                self.lineEdit_3.setText(str(totalCredit))

                # total expenses
                totalExpense = 0
                for row in PC.profitController.getTotalExpenses(sDate, eDate).fetchall():
                    if row[0] is not None:
                        totalExpense = row[0]

                self.lineEdit_4.setText(str(totalExpense))

                #totalProfitWithCredit
                totalProfitWithCredit = totalSales - (totalCosts + totalExpense)
                self.lineEdit_5.setText(str(totalProfitWithCredit))

                # totalProfitWithoutCredit
                totalProfitWithoutCredit = totalSales - (totalCosts + totalExpense + totalCredit)
                self.lineEdit_6.setText(str(totalProfitWithoutCredit))

            else:
                eObj.errorBox('Error', 'No data found')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Profit And Loss | UG - Pharmacy Management System"))
        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Profit And Loss"))
        self.username.setText(_translate("Dialog", "Username"))
        self.label_12.setText(_translate("Dialog", "End At"))
        self.pushButton_6.setText(_translate("Dialog", "Calculate Profit / Loss"))
        self.label_13.setText(_translate("Dialog", "Start From"))
        self.label.setText(_translate("Dialog", "Total Sales "))
        self.label_2.setText(_translate("Dialog", "Total Cost Price"))
        self.label_3.setText(_translate("Dialog", "Total Credit"))
        self.label_4.setText(_translate("Dialog", "Total Expenses"))
        self.label_5.setText(_translate("Dialog", "Profit/Loss (With credit)"))
        self.label_6.setText(_translate("Dialog", "Profit/Loss (Without credit)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_profit()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


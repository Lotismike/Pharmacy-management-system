import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time
import random
from pharmacyLogin import Ui_Login
from adminMenu import Ui_adminMenu
from userMenu import Ui_userMenu
import salesController as SC
import categoryController as CC
import expenseController as EC
import addDrugController as ADC
import addUserController as AUC
import os
from errors import errors
from addDrug import Ui_addDrug
from addUser import Ui_addUser
from expiry import Ui_expiry
from graphAdmin import Ui_graphAdmin
from outOfStock import Ui_outStock
from viewExpenditureAdmin import Ui_viewExpAdmin
from viewSalesAdmin import Ui_viewSalesAdmin
from viewStock import Ui_viewStock
from viewUsers import Ui_viewUsers
from profit import Ui_profit
from creditSalesCleared import Ui_creditSalesCleared
from viewSoldOnCredit import Ui_viewSoldOnCredit
from clearCredit import Ui_clearCredit
from sales import Ui_sales
from viewUserExpenditure import Ui_viewUserExpenditure
from yourAccount import Ui_yoAccount
from addDrugUser import Ui_addDrugUser
from expenditure import Ui_Expenditure
from sellProduct import Ui_sellProduct
from updateListRow import Ui_UpdateListRow
from deleteRow import Ui_DeleteRow
from updateStock import Ui_updateStock
from updateUser import Ui_updateUser
import pharmacyLoginController as PLC


#login
class Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)

        self.loginBTN.clicked.connect(self.login)
        self.username.returnPressed.connect(self.login)
        self.pass1.returnPressed.connect(self.login)

    def login(self):
        eObj = errors()
        uname = str(self.username.text())
        pass2 = str(self.pass1.text())

        if (uname == "" or pass2 == ""):
            eObj.errorBox('Error', 'Please fill all')
        else:

            if (PLC.pharmacyLoginController.login(uname, pass2) == 1):
                # getting accountType
                accountType = PLC.pharmacyLoginController.getAccountType()

                if str(accountType) == "USER":
                    # opening a admin window
                    self.userObj = UserMenu()
                    self.userObj.show()
                    self.hide()
                else:
                    # opening a admin window
                    self.adminObj = AdminMenu()
                    self.adminObj.show()
                    self.hide()

            else:
                eObj.errorBox('Error', 'Invalid Password')

# adminMenu class
class AdminMenu(QtWidgets.QMainWindow, Ui_adminMenu):
    def __init__(self, parent=None):
        super(AdminMenu, self).__init__(parent)

        self.setupUi(self)
        self.logoutBTN.clicked.connect(self.logOut)

    def logOut(self):
        self.hide()
        self.loginObj = Login()
        self.loginObj.show()
    # label1
    def labelClick1(self, eve):
        self.obj = AddDrug()
        self.obj.show()
        self.hide()

    # label2
    def labelClick2(self, eve):
        self.obj = ViewStock()
        self.obj.show()
        self.hide()

    # label3
    def labelClick3(self, eve):
        self.obj = ViewSalesAdmin()
        self.obj.show()
        self.hide()


    # label5
    def labelClick5(self, eve):
        self.obj = ViewExpAdmin()
        self.obj.show()
        self.hide()

    # label6
    def labelClick6(self, eve):
        self.obj = OutStock()
        self.obj.show()
        self.hide()

    # label7
    def labelClick7(self, eve):
        self.obj = Expiry()
        self.obj.show()
        self.hide()



    # label9
    def labelClick9(self, eve):
        self.obj = Profit()
        self.obj.show()
        self.hide()

    # label10
    def labelClick10(self, eve):
        self.obj = AddUser()
        self.obj.show()
        self.hide()

    # label11
    def labelClick11(self, eve):
        self.obj = ViewUsers()
        self.obj.show()
        self.hide()



    # label13
    def labelClick13(self, eve):
        self.obj = ViewSoldOnCredit()
        self.obj.show()
        self.hide()

    # label4
    def labelClick14(self, eve):
        self.obj = CreditSalesCleared()
        self.obj.show()
        self.hide()

    # label15
    def labelClick15(self, eve):
        self.obj = GraphAdmin()
        self.obj.show()
        self.hide()

# usermenu class
class UserMenu(QtWidgets.QMainWindow, Ui_userMenu):
    def __init__(self, parent=None):
        super(UserMenu, self).__init__(parent)
        self.setupUi(self)
        self.logoutBTN.clicked.connect(self.logOut)

    def logOut(self):
        self.loginObj = Login()
        self.loginObj.show()
        self.hide()

    # label1
    def labelClick1(self, eve):
        self.obj = Sales()
        self.obj.show()
        self.hide()

    # label2
    def labelClick2(self, eve):

        self.obj = Expenditure()
        self.obj.show()
        self.hide()

    # label3
    def labelClick3(self, eve):

        pass

    # label4
    def labelClick4(self, eve):

        self.obj = ViewSoldOnCredit()
        self.obj.show()
        self.hide()

    # label5
    def labelClick5(self, eve):

        self.obj = ViewUserExpenditure()
        self.obj.show()
        self.hide()

    # label6
    def labelClick6(self, eve):

        self.obj = YoAccount()
        self.obj.show()
        self.hide()

# Ui_sales
class Sales(QtWidgets.QDialog, Ui_sales):
    def __init__(self, parent=None):
        super(Sales, self).__init__(parent)
        global userID, username
        userID = PLC.pharmacyLoginController.getUserID()
        username = PLC.pharmacyLoginController.getUsername()

        self.salesIntials()
        self.setupUi(self)

        # set intals
        self.backImg.mousePressEvent = self.backMenu
        self.billDate.setReadOnly(1)
        self.billDate.setText(str(billNumber))
        self.totalAmount.setReadOnly(1)
        self.totalAmount.setText(str("0"))
        self.discount.setText(str("0"))
        self.bill.setReadOnly(1)
        self.bill.setText(str("0"))
        self.userName.setReadOnly(1)
        self.userName.setText(str(username))
        self.medName_2.addItem("Select Category")
        self.payMethod.addItem("Select Payment Method")
        self.payMethod.addItem("Cash")
        self.payMethod.addItem("Credit")
        self.cashDownLineEdit.setText(str("0"))
        self.cashDownLineEdit.setValidator(numberValidator)
        self.discount.setValidator(numberValidator)
        self.clientContactLineEdit.setValidator(numberValidator)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))
        # loading categories
        catList = CC.categoryController.getCatData()

        for x in catList:
            self.medName_2.addItem(x.getCatName())

        self.medName.returnPressed.connect(lambda: self.searchStock("drugname"))
        self.medName_2.currentIndexChanged.connect(lambda: self.searchStock("category"))
        self.medID.returnPressed.connect(lambda: self.searchStock("batch"))

        # edit cells
        self.tableWidget_2.cellClicked.connect(self.editCell)

    def salesIntials(self):
        global billNumber, createDate, entryDate, numberValidator
        unix = time.time()
        code = str(datetime.fromtimestamp(unix).strftime('%S')) + str(random.randrange(100, 999))
        billNumber = "B" + code
        createDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        entryDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))

        # reseting temp column to zero
        CC.categoryController.restTemp()
        numberValidator = QtGui.QIntValidator()

    def backMenu(self, eve):
        self.userMObj = UserMenu()
        self.userMObj.show()
        self.hide()

    def searchStock(self, searchType):
        eObj = errors()
        if searchType == "category":
            sword = self.medName_2.currentText()
            if sword != "Select Category":
                self.tableWidget.setRowCount(0)
                if len(SC.salesController.searchDrug(sword, searchType).fetchall()) > 0:
                    catTotal = SC.salesController.checkCat(sword).fetchall()
                    catSum = None
                    for row in catTotal:
                        catSum = row[0]
                    # checking if category is empty
                    if catSum == 0:
                        eObj.errorBox('Error', 'No drugs in the selected category')
                    else:
                        for row_number, row_data in enumerate(SC.salesController.searchDrug(sword, searchType)):
                            self.tableWidget.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                self.tableWidget.setItem(row_number, column_number,
                                                         QtWidgets.QTableWidgetItem(str(data)))

                else:
                    eObj.errorBox('Error', 'No drugs in the selected category')
            else:
                eObj.errorBox('Error', 'Please select a category')

        if searchType == "drugname":
            sword = self.medName.text().lower()
            self.tableWidget.setRowCount(0)
            if sword == "":
                eObj.errorBox('Error', 'Please enter a drug name')
            else:

                if len(SC.salesController.searchDrug(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(SC.salesController.searchDrug(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                else:
                    eObj.errorBox('Error', 'No drug found with the entered drug name')

        if searchType == "batch":
            sword = self.medID.text()
            self.tableWidget.setRowCount(0)
            if sword == "":
                eObj.errorBox('Error', 'Please enter a batch number')
            else:

                if len(SC.salesController.searchDrug(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(SC.salesController.searchDrug(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

                else:
                    eObj.errorBox('Error', 'No drug found with the entered batch number')

    def rowData(self, row, column):
        value = self.tableWidget.item(row, 0)
        id = value.text()
        value2 = self.tableWidget.item(row, 1)
        drugName = value2.text()
        value3 = self.tableWidget.item(row, 2)
        batchNo = value3.text()
        value4 = self.tableWidget.item(row, 3)
        category = value4.text()
        value5 = self.tableWidget.item(row, 4)
        sellingPrice = value5.text()

        # opening a new window
        self.sellProdObj = SellProduct(id, drugName, batchNo, category, sellingPrice)
        self.sellProdObj.exec_()

        billList = self.sellProdObj.getbillList()

        if len(billList) > 0:
            for row_number, row_data in enumerate([billList]):
                self.tableWidget_2.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        # bill order

    def billOrder(self):
        totalRows = self.tableWidget_2.rowCount()
        totals = 0
        if totalRows == 0:
            eObj = errors()
            eObj.errorBox('Error', 'No item to be billed')
        else:
            for row in range(0, totalRows):
                totals = totals + int(self.tableWidget_2.item(row, 4).text())

        self.totalAmount.setText(str(totals))

        # calculateBill

    def calculateBill(self):
        totalAmount = float(self.totalAmount.text())
        discount = float(self.discount.text())

        if discount == "":
            discount = 0
        discount = (discount / 100)

        if totalAmount == 0:
            eObj = errors()
            eObj.errorBox('Error', 'Click Bill Order Button to get the total')
        else:
            if discount == 0:
                newBill = totalAmount
            else:
                newBill = round(totalAmount - (discount * totalAmount), 2)
            self.bill.setText(str(newBill))

    def addBill(self):

        eObj = errors()
        bill = self.bill.text()
        paidBy = self.cleintName.text()
        discount = self.discount.text()
        totalRows = self.tableWidget_2.rowCount()
        payMethod = self.payMethod.currentText()
        payMethodIndex = self.payMethod.currentIndex()
        cashDown = self.cashDownLineEdit.text()
        payDate = self.paymentDateDateEdit.text()
        clientPhone = self.clientContactLineEdit.text()

        if totalRows == 0:
            eObj.errorBox('Error', 'No item to be billed')
        elif (bill == ""):
            eObj.errorBox('Error', 'Click Calculate Bill button to generate the bill')
        elif payMethodIndex == 0:
            eObj.errorBox('Error', 'Please select Payment Method')
        elif payMethodIndex == 2 and (cashDown == "" or clientPhone == ""):
            eObj.errorBox('Error',
                          'Since credit is the payment method , you have to fill in all fields in "Taken On Credit" section ')
        elif float(cashDown) > float(bill):
            eObj.errorBox('Error', 'Cash down can not exceed the Bill')
        else:

            for row in range(0, totalRows):
                dID = self.tableWidget_2.item(row, 0).text()
                drugName = self.tableWidget_2.item(row, 1).text()
                sellingPrice = self.tableWidget_2.item(row, 2).text()
                qty = self.tableWidget_2.item(row, 3).text()
                total = self.tableWidget_2.item(row, 4).text()
                batchNo = self.tableWidget_2.item(row, 5).text()
                cat = self.tableWidget_2.item(row, 6).text()

                # calculating discout per item
                disAmount = round((((100 - int(discount)) / 100) * int(total)), 2)

                SC.salesController.addSales(billNumber, dID, drugName, batchNo, cat, sellingPrice, qty, total, discount,
                                            disAmount, payMethod, paidBy, username, createDate, entryDate)

            SC.salesController.addCredit(billNumber, paidBy, clientPhone, bill, cashDown, payDate, username, createDate,
                                         payMethod)
            eObj.success("Congz", "Order has been submitted")
            # call intials
            self.salesIntials()
            self.clearData()

    def clearData(self):
        # self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        self.billDate.setText(str(billNumber))
        self.totalAmount.setText(str("0"))
        self.discount.setText(str("0"))
        self.bill.setText(str("0"))
        self.payMethod.setCurrentIndex(0)
        self.cleintName.setText(str(""))
        self.cashDownLineEdit.setText(str("0"))
        self.paymentDateDateEdit.clear()
        self.clientContactLineEdit.setText(str(""))

        # editing cells

    def editCell(self, row, column):
        value = self.tableWidget_2.item(row, 0)
        myid = value.text()

        value2 = self.tableWidget_2.item(row, 1)
        drugName = value2.text()

        value5 = self.tableWidget_2.item(row, 2)
        sellingPrice = value5.text()

        value6 = self.tableWidget_2.item(row, 3)
        qty = value6.text()

        # opening a new window
        self.upListRowObj = UpdateListRow(myid, drugName, sellingPrice, qty)
        self.upListRowObj.exec_()

        updateList = self.upListRowObj.getupdateList()

        # list for updating the row
        if len(updateList) > 0:
            newQty = updateList[0]
            newTotal = updateList[1]

            self.tableWidget_2.setItem(row, 4, QtWidgets.QTableWidgetItem(newTotal))
            self.tableWidget_2.setItem(row, 3, QtWidgets.QTableWidgetItem(newQty))

        # checking if delete is set true
        self.delRowObj = DeleteRow()
        if self.delRowObj.getDeleteValue() == 1:
            # setting temp to zero
            CC.categoryController.subUpdateTemp(myid, int(qty))

            self.tableWidget_2.removeRow(row)


# Ui_sellProduct
class SellProduct(QtWidgets.QDialog, Ui_sellProduct):
    def __init__(self, id, drugName, batchNo, category, sellingPrice):
        super(SellProduct, self).__init__()
        global drugID, drugName1, batchNo1, cat, sellingPrice1, totalQtn, numberValidator
        numberValidator = QtGui.QIntValidator()
        drugID = id
        drugName1 = drugName
        batchNo1 = batchNo
        cat = category
        sellingPrice1 = sellingPrice
        totalQtn = CC.categoryController.getItemQtn(drugID)

        # bill list
        global billList
        billList = []
        billList.clear()

        self.setupUi(self)
        # intails
        self.drugIDLineEdit.setText(str(drugID))
        self.drugNameLineEdit.setText(str(drugName1))
        self.batchNumberLineEdit.setText(str(batchNo1))
        self.categoryLineEdit.setText(str(cat))
        self.sellingPriceLineEdit.setText(str(sellingPrice1))
        self.quantityLeftLineEdit.setText(str(totalQtn))
        self.lineEdit.setValidator(numberValidator)
        self.pushButton.clicked.connect(self.addProduct)
        self.lineEdit.returnPressed.connect(self.addProduct)

    def addProduct(self):
        qtn = self.lineEdit.text()
        eObj = errors()
        if qtn == "":
            eObj.errorBox("Error", "Pleases enter quantity")
        elif int(qtn) > CC.categoryController.getItemQtn(drugID):
            eObj.errorBox("Error", "Quantity has exceeded the one in stock")
        else:

            amount = int(qtn) * int(sellingPrice1)
            billList.append(drugID)
            billList.append(drugName1)
            billList.append(sellingPrice1)
            billList.append(qtn)
            billList.append(amount)
            billList.append(batchNo1)
            billList.append(cat)

            # update temp in stock
            CC.categoryController.addUpdateTemp(drugID, int(qtn))

            # close window
            self.hide()
            eObj.success("Congz", "Item has been added too the list")

    @staticmethod
    def getbillList():
        return billList


# Ui_UpdateListRow
class UpdateListRow(QtWidgets.QDialog, Ui_UpdateListRow):
    def __init__(self, id, drugName, sellingPrice, qty):
        super(UpdateListRow, self).__init__()

        global drugID, drugName1, sellingPrice1, totalQtn, numberValidator, qty1
        numberValidator = QtGui.QIntValidator()
        drugID = id
        drugName1 = drugName
        sellingPrice1 = sellingPrice
        qty1 = qty
        totalQtn = CC.categoryController.getItemQtn(drugID)

        # update list
        global updateList
        updateList = []
        updateList.clear()

        # seting delete to zero
        self.delRowObj = DeleteRow()
        self.delRowObj.deleteMe(0)

        self.setupUi(self)
        # setting intails
        self.drugNameLineEdit.setReadOnly(1)
        self.drugNameLineEdit.setText(str(drugName1))
        self.sellingPriceLineEdit.setReadOnly(1)
        self.sellingPriceLineEdit.setText(str(sellingPrice1))
        self.quantityLeftLineEdit.setReadOnly(1)
        self.quantityLeftLineEdit.setText(str(totalQtn))
        self.lineEdit.setValidator(numberValidator)
        self.lineEdit.setText(str(qty1))
        self.pushButton.clicked.connect(self.editCell)
        self.pushButton_2.clicked.connect(self.deleteRow)

    # edit cell
    def editCell(self):
        qtn = self.lineEdit.text()
        eObj = errors()
        if qtn == "":
            eObj.errorBox("Error", "Pleases enter quantity")
        elif int(qtn) > CC.categoryController.getItemQtn(drugID):
            eObj.errorBox("Error", "Quantity has exceeded the one in stock")
        else:
            amount = int(qtn) * int(sellingPrice1)

            updateList.append(qtn)
            updateList.append(str(amount))

            # update temp in stock
            CC.categoryController.updateTemp(drugID, int(qtn))

            # closing the window
            self.hide()
            eObj.success("Congz", "List has been updated")

    @staticmethod
    def getupdateList():
        return updateList

    # delete row
    def deleteRow(self):
        # opening a delete alert
        self.delRowObj = DeleteRow()
        self.delRowObj.exec_()
        eObj = errors()
        # if the user has deleted
        if self.delRowObj.getDeleteValue() == 1:
            self.hide()
            eObj.success("Congz", "The record has been deleted from the list")


# Ui_DeleteRow
class DeleteRow(QtWidgets.QDialog, Ui_DeleteRow):
    def __init__(self, parent=None):
        super(DeleteRow, self).__init__(parent)
        self.setupUi(self)

    def deleteMe(self, delValue):

        global deleteValue
        eObj = errors()
        if delValue == 1:
            deleteValue = 1
        else:
            deleteValue = 0

    @staticmethod
    def getDeleteValue():
        return deleteValue


# Ui_Expenditure
class Expenditure(QtWidgets.QDialog, Ui_Expenditure):
    def __init__(self, parent=None):
        super(Expenditure, self).__init__(parent)
        global userID, username
        userID = PLC.pharmacyLoginController.getUserID()
        username = PLC.pharmacyLoginController.getUsername()
        self.salesIntials()

        self.setupUi(self)
        # set intails
        self.homeDist.setValidator(numberValidator)
        self.currentDist.setValidator(numberValidator)
        self.currentAddress.setValidator(numberValidator)
        self.addExpenseBTN.clicked.connect(self.addExpense)
        self.backImg.mousePressEvent = self.backMenu

    def salesIntials(self):
        global billNumber, createDate, entryDate, numberValidator
        unix = time.time()
        createDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        entryDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
        numberValidator = QtGui.QIntValidator()

    def backMenu(self, eve):
        self.userMObj = UserMenu()
        self.userMObj.show()
        self.hide()

    # add expense
    def addExpense(self):
        item = self.nationalID.text()
        cost = self.homeDist.text()
        qtn = self.currentDist.text()
        total = self.currentAddress.text()
        detail = self.textEdit.toPlainText()

        eObj = errors()
        if item == "" or cost == "" or qtn == "" or total == "":
            eObj.errorBox("Error", "Fill in all fields with a *")
        else:
            if (EC.expenseController.addExpense(item, cost, qtn, total, detail, username, userID, entryDate,
                                                createDate)) == 1:
                eObj.errorBox("Success", "New expense has been added")
                self.addExpenseClear()
            else:
                eObj.errorBox("Error", "Some thing went wrong! no expense added")

    # clear expenses
    def addExpenseClear(self):
        self.nationalID.setText("")
        self.homeDist.setText("")
        self.currentDist.setText("")
        self.currentAddress.setText("")
        self.textEdit.setText("")


# Ui_addDrugUser
class AddDrugUser(QtWidgets.QDialog, Ui_addDrugUser):
    def __init__(self, parent=None):
        super(AddDrugUser, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.userMObj = UserMenu()
        self.userMObj.show()
        self.hide()


# Ui_Ui_graphAdmin
class GraphAdmin(QtWidgets.QDialog, Ui_graphAdmin):
    def __init__(self, parent=None):
        super(GraphAdmin, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_viewUserExpenditure
class ViewUserExpenditure(QtWidgets.QDialog, Ui_viewUserExpenditure):
    def __init__(self, parent=None):
        super(ViewUserExpenditure, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.userMObj = UserMenu()
        self.userMObj.show()
        self.hide()


# Ui_yoAccount
class YoAccount(QtWidgets.QDialog, Ui_yoAccount):
    def __init__(self, parent=None):
        super(YoAccount, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.userMObj = UserMenu()
        self.userMObj.show()
        self.hide()


# addDrug class
class AddDrug(QtWidgets.QDialog, Ui_addDrug):
    def __init__(self, parent=None):
        super(AddDrug, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# view stock
class ViewStock(QtWidgets.QDialog, Ui_viewStock):
    def __init__(self, parent=None):
        super(ViewStock, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu
        self.tableWidget.cellClicked.connect(self.update)

    def update(self, row, column):
        try:
            # first refresh table
            self.loadStock()
            mid = self.tableWidget.item(row, 1).text()
            drugN = self.tableWidget.item(row, 2).text()
            bNo = self.tableWidget.item(row, 3).text()
            cat = self.tableWidget.item(row, 4).text()
            qtn = self.tableWidget.item(row, 5).text()
            bPrice = self.tableWidget.item(row, 6).text()
            sPrice = self.tableWidget.item(row, 8).text()
            supplier = self.tableWidget.item(row, 10).text()
            reorder = self.tableWidget.item(row, 11).text()
            expDate = self.tableWidget.item(row, 12).text()

            # opening a new window
            self.upStockObj = UpdateStock(mid, drugN, bNo, cat, qtn, bPrice, sPrice, supplier, reorder, expDate)
            self.upStockObj.exec_()
        except Exception as e:
            print("something went wrong")

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# UpdateStock
class UpdateStock(QtWidgets.QDialog, Ui_updateStock):

    def __init__(self, drugID, drugName, bNo, cat, qtn, bPrice, sPrice, suppplier, reorderLevel, expDate):
        super(UpdateStock, self).__init__()
        self.setupUi(self)

        # my intails
        global numberValidator, createDate, ddCat
        ddCat = cat
        unix = time.time()
        createDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        numberValidator = QtGui.QIntValidator()

        self.quantityLineEdit.setValidator(numberValidator)
        self.buyingPriceLineEdit.setValidator(numberValidator)
        self.sellingPriceLineEdit.setValidator(numberValidator)
        self.productionDateDateEdit.setValidator(numberValidator)

        self.drugNameLineEdit.setText(str(drugName))
        self.batchNumberLineEdit.setText(str(bNo))
        self.quantityLineEdit.setText(str(qtn))
        self.buyingPriceLineEdit.setText(str(bPrice))
        self.sellingPriceLineEdit.setText(str(sPrice))
        self.supplierLineEdit.setText(str(suppplier))
        self.productionDateDateEdit.setText(str(reorderLevel))
        self.expireDateLineEdit.setReadOnly(1)
        self.categoryLineEdit.setReadOnly(1)
        self.expireDateLineEdit.setPlaceholderText(str(expDate))
        self.categoryLineEdit.setPlaceholderText(str(cat))

        self.pushButton.clicked.connect(lambda: self.updateStock(drugID))
        self.pushButton_2.clicked.connect(lambda: self.deleteStock(drugID))

    # updateStock
    def updateStock(self, drugID):
        eObj = errors()
        ddName = self.drugNameLineEdit.text()
        ddBatch = self.batchNumberLineEdit.text()
        ddQtn = self.quantityLineEdit.text()
        ddBuy = self.buyingPriceLineEdit.text()
        ddSell = self.sellingPriceLineEdit.text()
        ddSup = self.supplierLineEdit.text()
        ddReorder = self.productionDateDateEdit.text()

        if ddName == "" or ddBatch == "" or ddQtn == "" or ddBuy == "" or ddSell == "" or ddSup == "" or ddReorder == "":
            eObj.errorBox("Error", "Please fill in all fields")
        else:
            if (ADC.addDrugController.updateStock(drugID, ddName, ddBatch, ddQtn, ddBuy, ddSell, ddSup, ddReorder,
                                                  ddCat)) == True:
                self.hide()
                eObj.success("Success", "Stock has been updated.Click Refresh button to see changes")
            else:
                eObj.errorBox("Error", "Something went wrong,try again")

    # deleteStock
    def deleteStock(self, drugID):
        eObj = errors()
        ddName = self.drugNameLineEdit.text()
        ddQtn = self.quantityLineEdit.text()
        ddBuy = self.buyingPriceLineEdit.text()

        # checkSales
        if len(SC.salesController.checkDrug(drugID).fetchall()) > 0:
            eObj.errorBox("Error", "A drug can only be deleted when there is no any sale made")
        else:

            # deleteStock
            if (ADC.addDrugController.deleteDrug(drugID, ddName, ddQtn, ddBuy, ddCat)) == True:
                # refresh table
                viewStockObj = ViewStock()
                viewStockObj.loadStock()
                self.hide()
                eObj.success("Success", "Drug has been deleted from stock.Click Refresh button to see changes")

            else:
                eObj.errorBox("Error", "Something went wrong,try again")


# Ui_viewSalesAdmin
class ViewSalesAdmin(QtWidgets.QDialog, Ui_viewSalesAdmin):
    def __init__(self, parent=None):
        super(ViewSalesAdmin, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_viewExpAdmin
class ViewExpAdmin(QtWidgets.QDialog, Ui_viewExpAdmin):
    def __init__(self, parent=None):
        super(ViewExpAdmin, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_outStock
class OutStock(QtWidgets.QDialog, Ui_outStock):
    def __init__(self, parent=None):
        super(OutStock, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_expiry
class Expiry(QtWidgets.QDialog, Ui_expiry):
    def __init__(self, parent=None):
        super(Expiry, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()

# Ui_profit
class Profit(QtWidgets.QDialog, Ui_profit):
    def __init__(self, parent=None):
        super(Profit, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_addUser
class AddUser(QtWidgets.QDialog, Ui_addUser):
    def __init__(self, parent=None):
        super(AddUser, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


# Ui_viewUsers
class ViewUsers(QtWidgets.QDialog, Ui_viewUsers):
    def __init__(self, parent=None):
        super(ViewUsers, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu
        self.tableWidget.cellClicked.connect(self.Uupdate)

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()

    def Uupdate(self, row, column):
        # first refresh table
        self.loadUser()
        uID = self.tableWidget.item(row, 0).text()
        uName = self.tableWidget.item(row, 1).text()
        fName = self.tableWidget.item(row, 2).text()
        lName = self.tableWidget.item(row, 3).text()
        DOB = self.tableWidget.item(row, 4).text()
        sex = self.tableWidget.item(row, 5).text()
        status = self.tableWidget.item(row, 6).text()
        natID = self.tableWidget.item(row, 7).text()
        hDist = self.tableWidget.item(row, 8).text()
        cDist = self.tableWidget.item(row, 9).text()
        add = self.tableWidget.item(row, 10).text()
        phone = self.tableWidget.item(row, 11).text()
        email = self.tableWidget.item(row, 12).text()
        salary = self.tableWidget.item(row, 13).text()
        joinDate = self.tableWidget.item(row, 14).text()
        password = self.tableWidget.item(row, 15).text()
        kinName = self.tableWidget.item(row, 16).text()
        kinPhone = self.tableWidget.item(row, 17).text()

        # opening a new window
        self.upUserObj = UpdateUser(uID, uName, fName, lName, DOB, sex, status, natID, hDist,
                                    cDist, add, phone, email, salary, joinDate, password, kinName, kinPhone)
        self.upUserObj.exec_()


# Ui_updateUser
class UpdateUser(QtWidgets.QDialog, Ui_updateUser):
    def __init__(self, uID, uName, fName, lName, DOB, sex, status, natID, hDist,
                 cDist, add, phone, email, salary, joinDate, password, kinName, kinPhone):
        super(UpdateUser, self).__init__()
        self.setupUi(self)

        # myintals
        self.dob.setReadOnly(1)
        self.joinDate.setReadOnly(1)
        self.dob.setPlaceholderText(str(DOB))
        self.joinDate.setPlaceholderText(str(joinDate))

        self.uname.setText(str(uName))
        self.fName.setText(str(fName))
        self.lName.setText(str(lName))
        self.sex.addItem(str(sex))
        self.sex.addItem("Male")
        self.sex.addItem("Female")
        self.status.addItem(str(status))
        self.status.addItem("Single")
        self.status.addItem("Divorced")
        self.status.addItem("Married")
        self.kinName.setText(str(kinName))
        self.nationalID.setText(str(natID))
        self.homeDist.setText(str(hDist))
        self.currentDist.setText(str(cDist))
        self.currentAddress.setText(str(add))
        self.phone.setText(str(phone))
        self.yoEmail.setText(str(email))
        self.kinPhone.setText(str(kinPhone))
        self.salary.setText(str(salary))
        self.pass1.setText(str(password))
        self.pass2.setText(str(password))

        self.updateAccBTN2.clicked.connect(lambda: self.updateUser(uID))

    # self.updateUser(uID)
    def updateUser(self, userID):
        uname = self.uname.text()
        fname = self.fName.text()
        lname = self.lName.text()
        sex = self.sex.currentText()
        status = self.status.currentText()
        natID = self.nationalID.text()
        homeD = self.homeDist.text()
        currentD = self.currentDist.text()
        currentAdd = self.currentAddress.text()
        phone = self.phone.text()
        email = self.yoEmail.text()
        kinName = self.kinName.text()
        kinPhone = self.kinPhone.text()
        salary = self.salary.text()
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()

        uname = uname.lower()

        eObj = errors()

        if uname == "" or fname == "" or lname == "" or kinName == "" or kinPhone == "" or phone == "" or currentD == "" or homeD == "" or \
                currentAdd == "" or natID == "" or pass1 == "" or pass2 == "":
            eObj.errorBox('Error', 'Please fill all fields with *')
        elif pass2 != pass1:
            eObj.errorBox('Error', 'Passwords do not match')
        elif (AUC.addUserController.checkOtherUsername(uname, userID) == 1):
            eObj.errorBox('Error', 'Username already taken,please change it')
        else:
            if (AUC.addUserController.updateUser(self, uname, fname, lname, sex, status, natID, homeD, currentD,
                                                 currentAdd, phone, email, kinName, kinPhone, salary, pass1,
                                                 userID) == 1):
                self.hide()
                eObj.success('Congratulations',
                             'User information has been updated.Click Refresh button to see changes in the table')
            else:
                eObj.errorBox('Error', 'Some thing went wrong and data has not been saved')



# Ui_viewSoldOnCredit
class ViewSoldOnCredit(QtWidgets.QDialog, Ui_viewSoldOnCredit):
    def __init__(self, parent=None):
        super(ViewSoldOnCredit, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu
        self.tableWidget.cellClicked.connect(self.clearDebt)

    def backMenu(self, eve):
        accType = PLC.pharmacyLoginController.getAccountType()
        if accType == "USER":
            self.userMObj = UserMenu()
            self.userMObj.show()
            self.hide()
        else:
            self.adminMObj = AdminMenu()
            self.adminMObj.show()
            self.hide()

    # clear debt
    def clearDebt(self, row, column):
        value = self.tableWidget.item(row, 0)
        billNo = value.text()

        value2 = self.tableWidget.item(row, 2)
        clientName = value2.text()

        value5 = self.tableWidget.item(row, 4)
        bill = value5.text()

        value6 = self.tableWidget.item(row, 5)
        amountPaid = value6.text()

        value7 = self.tableWidget.item(row, 6)
        bal = value7.text()

        value8 = self.tableWidget.item(row, 3)
        clientPhone = value8.text()

        unix = time.time()
        createDate = str(datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

        # call update dialog
        self.objCC = ClearCredit(billNo, clientName, clientPhone, bill, amountPaid, bal, createDate)
        self.objCC.exec_()

        if (self.objCC.getClearStatus() == 1):
            self.loadSaleCredit()


# Ui_clearCredit
class ClearCredit(QtWidgets.QDialog, Ui_clearCredit):
    def __init__(self, billNo, clientName, clientPhone, bill, amount, balance, createDate):
        super(ClearCredit, self).__init__()
        global billNo1, clientName1, clientPhone1, bill1, amount1, balance1, createDate1, numberValidator, uname
        global clearStatus
        clearStatus = 0
        billNo1 = billNo
        clientName1 = clientName
        clientPhone1 = clientPhone
        bill1 = bill
        amount1 = amount
        balance1 = balance
        createDate1 = createDate
        numberValidator = QtGui.QIntValidator()
        uname = PLC.pharmacyLoginController.getUsername()

        self.setupUi(self)

        # intials
        self.billNumberLineEdit.setReadOnly(1)
        self.billNumberLineEdit.setPlaceholderText(str(billNo1))
        self.clientNameLineEdit.setReadOnly(1)
        self.clientNameLineEdit.setPlaceholderText(str(clientName1))
        self.billLineEdit.setReadOnly(1)
        self.billLineEdit.setPlaceholderText(str(bill1))
        self.amountPaidLineEdit.setReadOnly(1)
        self.amountPaidLineEdit.setPlaceholderText(str(amount1))
        self.balanceLineEdit.setReadOnly(1)
        self.balanceLineEdit.setPlaceholderText(str(balance1))
        self.lineEdit.setValidator(numberValidator)

        self.lineEdit.returnPressed.connect(self.payDebt)
        self.pushButton.clicked.connect(self.payDebt)

    # pay debt
    def payDebt(self):
        eObj = errors()
        pay = self.lineEdit.text()
        bal = balance1

        if pay == "":
            eObj.errorBox("Error", "Please enter amount to pay debt")
        elif int(pay) > int(bal):
            eObj.errorBox("Error", "Entered amount has exceeded the required balance")
        else:
            clearD = SC.salesController.clearDebt(pay, billNo1, clientName1, clientPhone1, bill1, amount1, balance1,
                                                  uname, createDate1)
            if clearD == "cleared":
                self.hide()
                eObj.success("Congz", "The debt has been fully settled")
                clearStatus = 1
            elif clearD == "clearedPartially":
                self.hide()
                eObj.success("Congz", "The debt has been partially settled")
                clearStatus = 1
            else:
                eObj.errorBox("Error", "Something went wrong")
                clearStatus = 0

    # return clearStatus
    @staticmethod
    def getClearStatus():
        return clearStatus


# Ui_creditSalesCleared
class CreditSalesCleared(QtWidgets.QDialog, Ui_creditSalesCleared):
    def __init__(self, parent=None):
        super(CreditSalesCleared, self).__init__(parent)
        self.setupUi(self)

        self.backImg.mousePressEvent = self.backMenu

    def backMenu(self, eve):
        self.adminMObj = AdminMenu()
        self.adminMObj.show()
        self.hide()


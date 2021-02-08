
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QCursor
import time
import datetime
import categoryController as CC
import errors as E
import addDrugController as ADC
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_addDrug(object):

    def __init__(self):
        global numberValidator,createDate
        unix = time.time()
        createDate = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

        numberValidator = QtGui.QIntValidator()

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

        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(9, 80, 911, 100))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 850, 40))
        self.label.setObjectName("subTitle")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(10, 170, 911, 391))
        self.widget_2.setObjectName("widget_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 391, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.medicineNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.medicineNameLabel.setObjectName("pagesLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.medicineNameLabel)
        self.medicineNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.medicineNameLineEdit.setObjectName("addDrugFields")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.medicineNameLineEdit)
        self.quantityLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.quantityLabel.setObjectName("pagesLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.quantityLabel)
        self.quantityLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.quantityLineEdit.setObjectName("addDrugFields")
        self.quantityLineEdit.setValidator(numberValidator)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.quantityLineEdit)
        self.batchNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.batchNumberLabel.setObjectName("pagesLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.batchNumberLabel)
        self.batchNumberLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.batchNumberLineEdit.setObjectName("addDrugFields")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.batchNumberLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.categoryLabel.setObjectName("pagesLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.categoryComboBox.setObjectName("addDrugFields")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.manufucturerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.manufucturerLabel.setObjectName("pagesLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.manufucturerLabel)
        self.manufucturerLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.manufucturerLineEdit.setObjectName("addDrugFields")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.manufucturerLineEdit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(460, 10, 421, 271))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.productionDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.productionDateLabel.setObjectName("pagesLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.productionDateLabel)
        self.productionDateDateEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.productionDateDateEdit.setObjectName("addDrugFields")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productionDateDateEdit)
        self.expiryDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.expiryDateLabel.setObjectName("pagesLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.expiryDateLabel)
        self.expiryDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.expiryDateDateEdit.setObjectName("addDrugFields")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.expiryDateDateEdit)
        self.entryDateLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.entryDateLabel.setObjectName("pagesLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.entryDateLabel)
        self.entryDateDateEdit = QtWidgets.QDateEdit(self.formLayoutWidget_2)
        self.entryDateDateEdit.setObjectName("addDrugFields")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entryDateDateEdit)
        self.buyingPriceLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.buyingPriceLabel.setObjectName("pagesLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.buyingPriceLabel)
        self.buyingPriceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.buyingPriceLineEdit.setObjectName("addDrugFields")
        self.buyingPriceLineEdit.setValidator(numberValidator)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buyingPriceLineEdit)
        self.sellingPriceLabel = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.sellingPriceLabel.setObjectName("pagesLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.sellingPriceLabel)
        self.sellingPriceLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.sellingPriceLineEdit.setObjectName("addDrugFields")
        self.sellingPriceLineEdit.setValidator(numberValidator)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sellingPriceLineEdit)
        self.drugBTN = QtWidgets.QPushButton(self.widget_2)
        self.drugBTN.clicked.connect(self.addDrug)
        self.drugBTN.setGeometry(QtCore.QRect(370, 310, 230, 41))
        self.drugBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.drugBTN.setObjectName("pagesBTN")

        #intials
        self.productionDateDateEdit.setValidator(numberValidator)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #loading categories
        catList = CC.categoryController.getCatData()
        for x in catList:
            self.categoryComboBox.addItem(x.getCatName())

    #addDrug
    def addDrug(self):
        drugName = self.medicineNameLineEdit.text()
        qtn = self.quantityLineEdit.text()
        batchNo = self.batchNumberLineEdit.text()
        cat = self.categoryComboBox.currentText()
        supplier = self.manufucturerLineEdit.text()
        reorder = self.productionDateDateEdit.text()
        expDate = self.expiryDateDateEdit.text()
        entryDate = self.entryDateDateEdit.text()
        buyPrice = self.buyingPriceLineEdit.text()
        sellPrice = self.sellingPriceLineEdit.text()

        drugName = drugName.title()
        expDate1 = datetime.datetime.strptime(expDate, "%d/%m/%Y")
        entryDate1 = datetime.datetime.strptime(entryDate, "%d/%m/%Y")
        expDate = datetime.datetime.strftime(expDate1, '%Y-%m-%d')
        entryDate = datetime.datetime.strftime(entryDate1, '%Y-%m-%d')

        eObj = E.errors()

        if drugName =="" or qtn =="" or reorder=="" or batchNo=="" or supplier=="" or buyPrice =="" or sellPrice=="":
            eObj.errorBox('Error', 'Please fill all fields')
        else:
            addDrug = ADC.addDrugController.storeDrug(self, drugName, qtn, batchNo, cat, supplier, reorder, expDate, entryDate,
                                            buyPrice, sellPrice, createDate,"Admin")
            if addDrug == "failed":
                eObj.errorBox('Error', 'Drug already existing in the same category and its not yet out of stock.Change drug name and try again')
            elif addDrug == "updated":
                eObj.success('Congratulations','This drug was out of stock but its now updated')
                self.addDrugClear()
            elif addDrug == "inserted":
                eObj.success('Congratulations', 'New drug has been added')
                self.addDrugClear()
            else:
                print(drugName)
                eObj.errorBox('Error', 'Some thing went wrong and not data has been saved')

    def addDrugClear(self):
        self.medicineNameLineEdit.setText("")
        self.quantityLineEdit.clear()
        self.batchNumberLineEdit.setText("")
        self.categoryComboBox.setCurrentIndex(0)
        self.manufucturerLineEdit.setText("")
        self.productionDateDateEdit.clear()
        self.buyingPriceLineEdit.clear()
        self.sellingPriceLineEdit.clear()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Drug | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "New Drug Entry"))
        self.username.setText(_translate("Dialog", str(PLC.pharmacyLoginController.getUsername())))
        self.label.setText(_translate("Dialog", "Drug Information "))
        self.medicineNameLabel.setText(_translate("Dialog", "Drug Name "))
        self.quantityLabel.setText(_translate("Dialog", "Quantity"))
        self.batchNumberLabel.setText(_translate("Dialog", "Batch Number"))
        self.categoryLabel.setText(_translate("Dialog", "Category"))
        self.manufucturerLabel.setText(_translate("Dialog", "Supplier"))
        self.productionDateLabel.setText(_translate("Dialog", "Reorder Level"))
        self.expiryDateLabel.setText(_translate("Dialog", "Expiry Date"))
        self.entryDateLabel.setText(_translate("Dialog", "Entry Date"))
        self.buyingPriceLabel.setText(_translate("Dialog", "Buying Price"))
        self.sellingPriceLabel.setText(_translate("Dialog", "Selling Price"))
        self.drugBTN.setText(_translate("Dialog", "ADD A DRUG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_addDrug()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


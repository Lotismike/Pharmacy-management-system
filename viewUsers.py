
from PyQt5 import QtCore, QtGui, QtWidgets
import mainController as MC
import  errors as E
import addUserController as AUC
from PyQt5.QtGui import QCursor
import update as UP
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_viewUsers(object):
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
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 821, 381))
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(19)
        colHeaders = ['userID', 'Username', 'First Name', 'Last Name', 'DOB', 'Gender',
                      'Status','National ID','Home District','Current District','Address','Phone',
                      'Email','Salary','Joining Date','Password','Next of Kin','Phone(Kin)','Created At']
        self.tableWidget.setHorizontalHeaderLabels(colHeaders)
        self.tableWidget.setObjectName("tableWidget")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 60, 721, 20))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.medName_2 = QtWidgets.QComboBox(Dialog)
        self.medName_2.setGeometry(QtCore.QRect(330, 110, 311, 25))
        self.medName_2.setObjectName("medName_2")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(330, 88, 311, 20))
        self.label.setObjectName("searchLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.medName_2.addItem("Select Username")

        # loading usernames
        catList = MC.mainController.getUserData()
        for x in catList:
            self.medName_2.addItem(x.getUsername())

        self.medName_2.currentIndexChanged.connect(lambda: self.searchUser("username"))
        self.refreshBTN.clicked.connect(self.loadUser)
        #call load users
        self.loadUser()
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))
        self.tableWidget.cellClicked.connect(self.update)

    def update(self):
        # opening a new window
        self.window = QtWidgets.QDialog()
        self.ui = UP.Ui_Update()
        self.ui.setupUi(self.window)
        self.window.exec_()

    # search users
    def searchUser(self, searchType):
        eObj = E.errors()
        self.tableWidget.setRowCount(0)
        if searchType == "username":
            sword = self.medName_2.currentText()
            if self.medName_2.currentIndex() != 0:
                if len(AUC.addUserController.searchUsers(sword, searchType).fetchall()) > 0:
                    for row_number, row_data in enumerate(AUC.addUserController.searchUsers(sword, searchType)):
                        self.tableWidget.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            self.tableWidget.setItem(row_number, column_number,
                                                     QtWidgets.QTableWidgetItem(str(data)))
                else:
                    eObj.errorBox('Error', 'No drugs details for the  selected user')
            else:
                eObj.errorBox('Error', 'Please select a username')
    #load users
    def loadUser(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(AUC.addUserController.loadUsers()):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,
                                         QtWidgets.QTableWidgetItem(str(data)))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Staff Members | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Staff Members "))
        self.username.setText(_translate("Dialog", "Username"))
        self.refreshBTN.setText(_translate("Dialog", "Refresh"))
        self.label.setText(_translate("Dialog", "Search By Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_viewUsers()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


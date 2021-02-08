from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
import errors
import accountController as AC
import pharmacyLoginController as PLC
from PyQt5.QtGui import QIcon, QPixmap
class Ui_yoAccount(object):
    def __init__(self):
        self.myIntials()

    def myIntials(self):
        userData = AC.accountController.userData()
        userData = userData.fetchall()

        global username, fname, lname, dob, sex, status, kinName, sex, natID, homeDist, currentDist,\
        currentAddress,phone,email,kinPhone,password,numberValidator

        numberValidator = QtGui.QIntValidator()

        for row in userData:
            username = row[0]
            fname= row[1]
            lname= row[2]
            dob= row[3]
            sex= row[4]
            status= row[5]
            kinName= row[6]
            sex= row[7]
            natID= row[8]
            homeDist= row[9]
            currentDist= row[10]
            currentAddress= row[11]
            phone= row[12]
            email= row[13]
            kinPhone= row[14]
            password = row[15]

    def setupUi(self, Dialog):
        Dialog.setObjectName("adminPages")
        Dialog.setFixedSize(942, 594)
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

        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(300, 100, 2, 481))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(610, 100, 2, 291))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 271, 20))
        self.label.setObjectName("pagesLabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(340, 70, 271, 20))
        self.label_2.setObjectName("pagesLabel")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 70, 271, 20))
        self.label_3.setObjectName("pagesLabel")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(19, 99, 281, 491))
        self.widget.setObjectName("widget")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.label_4.setObjectName("userLabel")
        self.uname = QtWidgets.QLineEdit(self.widget)
        self.uname.setGeometry(QtCore.QRect(0, 30, 271, 31))
        self.uname.setObjectName("uname")
        self.fName = QtWidgets.QLineEdit(self.widget)
        self.fName.setGeometry(QtCore.QRect(0, 100, 271, 31))
        self.fName.setObjectName("fName")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(0, 70, 271, 31))
        self.label_5.setObjectName("userLabel")
        self.lName = QtWidgets.QLineEdit(self.widget)
        self.lName.setGeometry(QtCore.QRect(0, 170, 271, 31))
        self.lName.setObjectName("lName")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(0, 140, 271, 31))
        self.label_6.setObjectName("userLabel")
        self.dob = QtWidgets.QLineEdit(self.widget)
        self.dob.setGeometry(QtCore.QRect(0, 240, 271, 31))
        self.dob.setObjectName("dob")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 210, 271, 31))
        self.label_7.setObjectName("userLabel")
        self.sex = QtWidgets.QLineEdit(self.widget)
        self.sex.setGeometry(QtCore.QRect(0, 310, 271, 31))
        self.sex.setObjectName("sex")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(0, 280, 271, 31))
        self.label_8.setObjectName("userLabel")
        self.status = QtWidgets.QLineEdit(self.widget)
        self.status.setGeometry(QtCore.QRect(0, 380, 271, 31))
        self.status.setObjectName("status")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(0, 350, 271, 31))
        self.label_9.setObjectName("userLabel")
        self.kinName = QtWidgets.QLineEdit(self.widget)
        self.kinName.setGeometry(QtCore.QRect(0, 450, 271, 31))
        self.kinName.setObjectName("kinName")
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setGeometry(QtCore.QRect(0, 420, 271, 31))
        self.label_22.setObjectName("userLabel")
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setGeometry(QtCore.QRect(320, 100, 281, 491))
        self.widget_2.setObjectName("widget_2")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.label_10.setObjectName("userLabel")
        self.nationalID = QtWidgets.QLineEdit(self.widget_2)
        self.nationalID.setGeometry(QtCore.QRect(0, 30, 271, 31))
        self.nationalID.setObjectName("nationalID")
        self.homeDist = QtWidgets.QLineEdit(self.widget_2)
        self.homeDist.setGeometry(QtCore.QRect(0, 100, 271, 31))
        self.homeDist.setObjectName("homeDist")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setGeometry(QtCore.QRect(0, 70, 271, 31))
        self.label_11.setObjectName("userLabel")
        self.currentDist = QtWidgets.QLineEdit(self.widget_2)
        self.currentDist.setGeometry(QtCore.QRect(0, 170, 271, 31))
        self.currentDist.setObjectName("currentDist")
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setGeometry(QtCore.QRect(0, 140, 271, 31))
        self.label_12.setObjectName("userLabel")
        self.currentAddress = QtWidgets.QLineEdit(self.widget_2)
        self.currentAddress.setGeometry(QtCore.QRect(0, 240, 271, 31))
        self.currentAddress.setObjectName("currentAddress")
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(0, 210, 271, 31))
        self.label_13.setObjectName("userLabel")
        self.phone = QtWidgets.QLineEdit(self.widget_2)
        self.phone.setGeometry(QtCore.QRect(0, 310, 271, 31))
        self.phone.setObjectName("phone")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(0, 280, 271, 31))
        self.label_14.setObjectName("userLabel")
        self.yoEmail = QtWidgets.QLineEdit(self.widget_2)
        self.yoEmail.setGeometry(QtCore.QRect(0, 380, 271, 31))
        self.yoEmail.setObjectName("yoEmail")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(0, 350, 271, 31))
        self.label_15.setObjectName("userLabel")
        self.kinPhone = QtWidgets.QLineEdit(self.widget_2)
        self.kinPhone.setGeometry(QtCore.QRect(0, 450, 271, 31))
        self.kinPhone.setObjectName("kinPhone")
        self.label_23 = QtWidgets.QLabel(self.widget_2)
        self.label_23.setGeometry(QtCore.QRect(0, 420, 271, 31))
        self.label_23.setObjectName("userLabel")
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setGeometry(QtCore.QRect(620, 100, 281, 281))
        self.widget_3.setObjectName("widget_3")
        self.label_16 = QtWidgets.QLabel(self.widget_3)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.label_16.setObjectName("userLabel")
        self.currentPass = QtWidgets.QLineEdit(self.widget_3)
        self.currentPass.setGeometry(QtCore.QRect(0, 30, 271, 31))
        self.currentPass.setObjectName("currentPass")
        self.pass1 = QtWidgets.QLineEdit(self.widget_3)
        self.pass1.setGeometry(QtCore.QRect(0, 100, 271, 31))
        self.pass1.setObjectName("pass1")
        self.label_17 = QtWidgets.QLabel(self.widget_3)
        self.label_17.setGeometry(QtCore.QRect(0, 70, 271, 31))
        self.label_17.setObjectName("userLabel")
        self.pass2 = QtWidgets.QLineEdit(self.widget_3)
        self.pass2.setGeometry(QtCore.QRect(0, 170, 271, 31))
        self.pass2.setObjectName("pass2")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(0, 140, 271, 31))
        self.label_18.setObjectName("userLabel")
        self.changePassBTN = QtWidgets.QPushButton(Dialog)
        self.changePassBTN.setGeometry(QtCore.QRect(670, 320, 171, 41))
        self.changePassBTN.setObjectName("changePassBTN")
        self.changePassBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.changePassBTN.clicked.connect(self.passChange)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(610, 390, 301, 2))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line")
        self.updateAccBTN = QtWidgets.QPushButton(Dialog)
        self.updateAccBTN.setGeometry(QtCore.QRect(650, 450, 221, 71))
        self.updateAccBTN.setObjectName("userBTN")
        self.updateAccBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.updateAccBTN.clicked.connect(self.yoAccount2)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #set intials
        self.uname.setText(str(username))
        self.uname.setReadOnly(1)
        self.fName.setText(str(fname))
        self.fName.setReadOnly(1)
        self.lName.setText(str(lname))
        self.lName.setReadOnly(1)
        self.dob.setText(str(dob))
        self.dob.setReadOnly(1)
        self.sex.setText(str(sex))
        self.sex.setReadOnly(1)
        self.status.setText(str(status))
        self.kinName.setText(str(kinName))
        self.nationalID.setText(str(natID))
        self.nationalID.setReadOnly(1)
        self.homeDist.setText(str(homeDist))
        self.homeDist.setReadOnly(1)
        self.currentDist.setText(str(currentDist))
        self.currentAddress.setText(str(currentAddress))
        self.phone.setText(str(phone))
        self.phone.setValidator(numberValidator)
        self.yoEmail.setText(str(email))
        self.kinPhone.setText(str(kinPhone))
        self.kinPhone.setValidator(numberValidator)
        self.currentPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username.setText(str(PLC.pharmacyLoginController.getUsername()))


    #update your account
    def yoAccount2(self):
        status = self.status.text()
        phone = self.phone.text()
        kinName = self.kinName.text()
        cDist = self.currentDist.text()
        cAddr = self.currentAddress.text()
        email = self.yoEmail.text()
        kinPhone = self.kinPhone.text()

        eObj = errors.errors()

        if status =="" or phone =="" or kinName =="" or cDist =="" or cAddr =="" or kinPhone=="":
            eObj.errorBox("Error","Fill in all fields with a *")
        else:
            if AC.accountController.updateUser(status,phone,kinName,cDist,cAddr,email,kinPhone)==1:
                eObj.success("Congz", "Your account has been updated")
            else:
                eObj.errorBox("Error", "Some thing went wrong and no your account has not been updated")

    #change pass
    def passChange(self):
        cPass = self.currentPass.text()
        pass1 = self.pass1.text()
        pass2 = self.pass2.text()

        eObj = errors.errors()

        if cPass =="" or pass1=="" or pass2=="":
            eObj.errorBox("Error", "Fill in all fields in this section")
        else:
            if AC.accountController.checkUserPass2(cPass) ==1:
                if pass1 == pass2:
                    if AC.accountController.upadateUserPass(pass1) == 1:
                        eObj.success('Congz', 'Password has been updated')
                        self.passChangeClear()
                    else:
                        eObj.errorBox('Error', 'Some thing went wrong and no your account has not been updated')
                else:
                    eObj.errorBox('Error', 'Passwords do not match')
            else:
                eObj.errorBox('Error', 'Invalid Password')

    def passChangeClear(self):
        self.currentPass.setText(str(""))
        self.pass1.setText(str(""))
        self.pass2.setText(str(""))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Your Account | UG - Pharmacy Management System"))

        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "Your Account "))
        self.username.setText(_translate("Dialog", "Username"))
        self.label.setText(_translate("Dialog", "Bio Data"))
        self.label_2.setText(_translate("Dialog", "Address And Contacts"))
        self.label_3.setText(_translate("Dialog", "Password Section"))
        self.label_4.setText(_translate("Dialog", "Username"))
        self.label_5.setText(_translate("Dialog", "First Name"))
        self.label_6.setText(_translate("Dialog", "Last Name"))
        self.label_7.setText(_translate("Dialog", "Date Of Birth"))
        self.label_8.setText(_translate("Dialog", "Sex"))
        self.label_9.setText(_translate("Dialog", "Status*"))
        self.label_22.setText(_translate("Dialog", "Next Of Kin*"))
        self.label_10.setText(_translate("Dialog", "National ID"))
        self.label_11.setText(_translate("Dialog", "Home District"))
        self.label_12.setText(_translate("Dialog", "Current District*"))
        self.label_13.setText(_translate("Dialog", "Current Address*"))
        self.label_14.setText(_translate("Dialog", "Phone Number*"))
        self.label_15.setText(_translate("Dialog", "Email Address"))
        self.label_23.setText(_translate("Dialog", "Next Of Kin Contact*"))
        self.label_16.setText(_translate("Dialog", "Enter Current Password"))
        self.label_17.setText(_translate("Dialog", "Enter New Password"))
        self.label_18.setText(_translate("Dialog", "Confirm Password"))
        self.changePassBTN.setText(_translate("Dialog", "Change Password"))
        self.updateAccBTN.setText(_translate("Dialog", "UPDATE YOUR ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_yoAccount()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtGui import QCursor
class Ui_Login(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("loginBody")
        MainWindow.setFixedSize(674, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 31, 611, 41))
        self.label.setObjectName("label")
        self.label.setStyleSheet("font-size:24px")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(270, 109, 351, 221))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("font-size:18px")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font-size:14px;")
        self.horizontalLayout.addWidget(self.label_2)
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setObjectName("username")
        self.username.setStyleSheet("height:28px;border-radius:4px;")
        self.horizontalLayout.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("font-size:14px;")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pass1 = QtWidgets.QLineEdit(self.groupBox)
        self.pass1.setObjectName("pass")
        self.pass1.setStyleSheet("height:28px;border-radius:4px;")
        self.pass1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.horizontalLayout_2.addWidget(self.pass1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.loginBTN = QtWidgets.QPushButton(self.groupBox)
        self.loginBTN.setObjectName("loginBTN")
        self.loginBTN.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBTN.setFont(QtGui.QFont("Times", 10, QtGui.QFont.Bold))
        #self.loginBTN.clicked.connect(self.login)
        self.verticalLayout.addWidget(self.loginBTN)
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(60, 120, 191, 211))
        self.img.setText("")
        self.img.setObjectName("img")
        pixmap = QPixmap('data/images/logoInner.png')
        #pixmap = pixmap.scaledToWidth(200)
        self.img.setScaledContents(True)
        self.img.setPixmap(pixmap)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 400, 580, 41))
        self.label_4.setObjectName("loginFooter")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login |  Pharmacy Management System"))

        self.label.setText(_translate("MainWindow", "UG- PHARMACY MS"))
        self.groupBox.setTitle(_translate("MainWindow", "LogIn"))
        self.label_2.setText(_translate("MainWindow", "Username : "))
        self.label_3.setText(_translate("MainWindow", "Password : "))
        self.loginBTN.setText(_translate("MainWindow", "Login"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

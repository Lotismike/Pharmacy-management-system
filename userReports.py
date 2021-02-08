from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_userReports(object):
    def __init__(self):
        pass

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(942, 594)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.backImg = QtWidgets.QLabel(Dialog)
        self.backImg.setGeometry(QtCore.QRect(30, 8, 40, 41))
        self.backImg.setObjectName("backImg")
        pixmap = QPixmap('data/images/back2.png')
        # pixmap = pixmap.scaledToWidth(40)
        self.backImg.setPixmap(pixmap)
        self.backImg.setScaledContents(True)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(300, 20, 351, 21))
        self.title.setObjectName("title")
        self.username = QtWidgets.QLabel(Dialog)
        self.username.setGeometry(QtCore.QRect(800, 20, 47, 13))
        self.username.setObjectName("username")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 45, 942, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.backImg.setText(_translate("Dialog", ""))
        self.title.setText(_translate("Dialog", "User\'s Reports"))
        self.username.setText(_translate("Dialog", "Username"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    userReportDialog = QtWidgets.QDialog()
    ui = Ui_userReports()
    ui.setupUi(userReportDialog)
    userReportDialog.show()
    sys.exit(app.exec_())


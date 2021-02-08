from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
class errors():
    def errorBox(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setObjectName("error")
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setWindowIcon(QIcon('data/images/erroricon.ICO'))
        mess.exec_()

    def warning(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setObjectName("warning")
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.setWindowIcon(QIcon('data/images/warnicon.ICO'))
        mess.exec_()

    def success(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setObjectName("success")
        mess.setText(message)
        mess.setWindowIcon(QIcon('data/images/successicon.ICO'))
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
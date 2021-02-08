import shutil
import threading

from PyQt5.QtCore import QDate, QTimer

StylesSheet = """
/**************************GENERAL SECTION*******************************/
 QLineEdit{
    background-color:#FFFFFF;
    height:25px;
    border-radius:8px;
    border:1px solid #D1D0CE;
}

 QDateEdit{
    background-color:#FFFFFF;
    height:25px;
    border-radius:8px;
    border:1px solid #D1D0CE;
}
QComboBox{
    background-color:#FFFFFF;
    height:25px;
    border-radius:8px;
    border:1px solid #D1D0CE;
}
QPushButton{
    background-color:red;
    color:white;
    font-weight:bold;
    font-size:12px;
    height:40px;
}
QPushButton#logoutBTN{
    background-color:red;
    border-radius:4px;
    color:white;
}
QPushButton#logoutBTN:hover{
    background-color:#800517;
    border-radius:4px;
    color:white;
}

QLabel#backImg{
    border-radius:20px;
    padding:0px;   
}
QLabel#backImg:hover{
    background:white;
}

QWidget#dateSection{
    border-radius:4px;
    background:#A0CFEC;
}
QWidget#billSec2{
    border-radius:4px;
    background:#BDEDFF;
}

QLabel#billTitle{
    font-size:16px;
    font-weight:bold;
}
QPushButton#billOrderBTN{
    background:#ADDFFF;
    font-weight:bold;
    font-size:16px;
}
QLabel#searchTitle{
    font-size:12px;
    font-weight:bold;
    color:#008080;
}

QLabel#title{
    font-size:20px;
    font-weight:bold;
}

QLabel#gridImg:hover{    
}

QLineEdit#addDrugFields{
    margin-bottom:18px;
    height:80px;
}
QComboBox#addDrugFields{
    height:80px;
    background:white;
    margin-bottom:18px;
}

QDateEdit#addDrugFields{
    margin-bottom:18px;
    height:80px;
    background:white;
}
QLabel#pagesTitle{
    background: #006699;
    color:white;
    font-size:30px;
    font-weight:bold;
    height:60px;
    padding-left:20px;
    padding-right:20px;
    qproperty-alignment: AlignCenter;
}
#usernameLabel{
    color:white;
    font-size:15px;
    border:1px solid white;
    border-radius:4px;
    qproperty-alignment: AlignCenter;
}
#warning{
    background:#FFFFCC;
    color:white;
}
#warning QPushButton{
    background:#006699;
    color:white
}
#warning QPushButton:hover{
    background:red;
}
#error{
    background:#FCDFFF;
    color:white;
    qproperty-alignment: AlignCenter;
    font-size:14px;
}
#error QPushButton{
    background:#C11B17;
    color:white
}
#error QPushButton:hover{
    background:red;
}
#success{
    background:#C3FDB8;
    color:white;
}
#success QPushButton{
    background:#254117;
    color:white
}
#success QPushButton:hover{
    background:green;
}
/**************************LOGIN SECTION*******************************/
#loginBody{
    background-color:white;
}
QLabel#label{
    background: #006699;
    color:white;
    font-size:20px;
    font-weight:bold;
    border-radius:4px;
    border:1px solid #AFDCEC;
    height:60px;
    padding-left:20px;
    padding-right:20px;
    qproperty-alignment: AlignCenter;
}
#loginBTN{
    background:#006699;
    height:30px;
}
#loginBTN:hover{
    background:black;
}
QGroupBox#groupBox{ 
    color:#006699;
    border-color:#006699;
    font-weight:bold;
}
QLabel#loginEdit{
    height:28px;
    border-radius:4px;
    border-color:2px solid gray;
}
QLabel#pagesLabel{
    color:#151B54;
    font-size:14px;
    font-weight:bold;
}
#loginFooter{
    font-size:14px;
    font-style:Italics;
    color:#2B3856;
    font-weight:bold;
    border-top:2px solid #151B54;
    qproperty-alignment: AlignCenter;
}

/**********************ADMIN DASHBOARD SECTION **************************/
#adminMenuBody{
    background-color:white;
}
#gridImg{
    margin-right:54px;
    margin-left:54px;
    border-radius:40px;
}
#gridImg:hover{
    background:black;
}
QLabel#gridText{
    color:#461B7E;
    font-weight:bold;
    font-size:14px;
    text-shadow: 2px 2px white;
}
QLabel#title1{
    background: #006699;
    color:white;
    font-size:30px;
    font-weight:bold;
    border-radius:4px;
    border:1px solid #AFDCEC;
    height:60px;
    padding-left:20px;
    padding-right:20px;
    qproperty-alignment: AlignCenter;
}
QLabel#header1{
    color:#5E5A80;
    font-size:16px;
    font-weight:bold;
    qproperty-alignment: AlignCenter;
}
#adminLine{
    background:#E0B0FF;
}
#footerText{
    font-size:14px;
    font-style:Italics;
    color:#2B3856;
    font-weight:bold;
    qproperty-alignment: AlignCenter;
}
#restoreText{
    color :#9F000F;
    font-size:12px;
    font-weight:bold;
}
#backupBTN{
    background:#3EA055;
    font-size:16px;
    font-weight:bold;
}
#backupBTN:hover{
    background:#254117;
}
#restoreBTN{
    background:#9F000F;
    font-size:16px;
    font-weight:bold;
}
#restoreBTN:hover{
    background:red;
}
/**********************USER DASHBOARD SECTION **************************/

#gridImg2{
    margin-right:66px;
    margin-left:66px;
    border-radius:65px;
    
}
#gridImg2:hover{
    background:black;
}
#calSection{
    background-color:#9AFEFF;
    border-radius:4px;
}
#billBTN{
    background:#9AFEFF;
    color:black;
}
#billBTN:hover{
    background:#307D7E;
    color:white;
}
#innerSec{
    background:black;
    color:white; 
    padding-left:10px;
}
#innerSec2{
    background:black;
    color:white;
    border-top-left-radius:4px;
    border-top-right-radius:4px;
    padding-left:10px;
}
#saleLevel{
    color:black;
    font-weight:bold;
    font-size:12px;
}
#calBTN{
    font-size:12px;
    font-weight:bold;
    color:white;
    height:50px;
    background:red;
}
#calBTN:hover{
    background:#800517;
}
QPushButton#subOrderBTN{
    background:#006699;
    color:white;
    font-weight:bold;
    font-size:12px;
}
QPushButton#subOrderBTN:hover{
    background:#254117;
}
#subOrderBTN2{
    background:gray;
}
#userLabel{
    font-size:12px;
    color:black;
    font-weight:bold;
}
#userBTN{
    background:#006699;
    color:white;
    font-weight:bold;
    font-size:12px;
}
#userBTN:hover{
    background:black;
}
#changePassBTN{
    background:black;
    color:white;
}
#changePassBTN:hover{
    background:#006699;
}
/**********************ADD A DRUG SECTION **************************/
#adminPages{
    background-color:white;
}
QFrame#header{
    background-color:#006699;
    color:#FFFFFF;
    font-size:20px;
    font-weight:bold;
}
QLabel#subTitle{
    color:#151B54;
    font-size:16px;
    font-weight:bold;
    background:#00CCFF;
    border-bottom:2px solid black;
    qproperty-alignment: AlignCenter;
}
LineEdit#searchField{
    height:5px;
    background:red;
}
QLabel#searchLabel{
    color:#151B54;
    font-size:14px;
    qproperty-alignment: AlignCenter;
}
QLabel#staffLabel{
    color:#151B54;
    font-size:12px;
}
#line{
    background:#006699;
}
QHeaderView::section{
    background:#006699;
    color:white;
    font-size:13px;
}
#pagesBTN{
    background-color:#006699;
    color:#FFFFFF;
    font-weight:bold;
    font-size:20px;
    border-radius:20px;
}
#pagesBTN:hover{
    background-color:#151B54;
}
#profitBTN{
    background-color:red;
    color:#FFFFFF;
    font-weight:bold;
    font-size:16px;
}
#profitBTN:hover{
    background-color:#800517;
}
#adminTab{
    background:#E8E8E8;
}
QTabBar::tab {
    height:25px;
    font-size:12px;
    width:153px;
    color:#C6AEC7;
    font-weight:bold;
    background:black;
}
QTabBar::tab:selected {
    color:white;  
    border-bottom: 2px solid red ;
}

#adminDate{
   
    border: 1px solid #C8C8C8;
    font-weight:bold;
}
#graphBTN{
    background:red;
    font-weight:bold;
    border-radius:4px;
}
#graphBTN:hover{
    background:black;
}
#smallPages{
    background:#87AFC7;
    background:#B6B6B4;
}
#smallPagesLabel{
    color:white;
}
#sellLabel{
    font-size:12px;
    color:#006699;
    font-weight:bold;
}
#sellTitle{
    font-size:14px;
    background:#006699;
    color:white;
    font-weight:bold;
    border-radius:4px;
    qproperty-alignment: AlignCenter;  
}
#qtnLabel{
    font-size:16px;
    color:black;
    font-weight:bold;
    qproperty-alignment: AlignCenter; 
}
#sellBTN{
    color:white;
    font-weight:bold;
    background:#006699;
}
#sellBTN:hover{
    background:black;
}
#delBTNS{
    background:#98AFC7;
}
#delBTNS:hover{
    background:#006699;
}
#mtitle{
    color:#006699;
    font-weight:bold;
    font-size:16px;
    qproperty-alignment: AlignCenter; 
}
#loading2{
    font-size:16px;
    color:black;
}
#regForm QLineEdit{
    margin-bottom:12px;
}
#regForm QLabel{
    font-size:14px;
    color:black;
}
#regLabel{
    font-size:14px;
    color:black;
    qproperty-alignment: AlignCenter; 
    font-weight:bold;
}
#regHead{
    font-size:14px;
    color:#006699;
    font-weight:bold;
    border:1px solid white;
    border-radius:4px;
}
#regBTN{
    background:#006699;
    color:white;
    font-size:15px; 
}
#regBTN:HOVER{
    background:black;
}
"""

from mainStart import *
import pharmacyLoginController as PLC

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(StylesSheet)

    w = Login()
    w.show()

    sys.exit(app.exec_())